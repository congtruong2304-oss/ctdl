#include <iostream>
#include <vector>
#include <random>
#include <chrono>
#include <cmath>
#include <iomanip>

using namespace std;

struct Mau {
    vector<double> x;
    int y;
};

inline double kc_euclid(const vector<double>& u, const vector<double>& v) {
    double sum = 0.0;
    for (size_t i = 0; i < u.size(); ++i) {
        double diff = u[i] - v[i];
        sum += diff * diff;
    }
    return sqrt(sum);
}

int phan_loai(const vector<double>& q, const vector<Mau>& D) {
    double min_dist = 1e18;
    int best_nhan = -1;
    for (const auto& m : D) {
        double dist = kc_euclid(q, m.x);
        if (dist < min_dist) {
            min_dist = dist;
            best_nhan = m.y;
        }
    }
    return best_nhan;
}

vector<Mau> sinh_du_lieu(int n, int d, mt19937& rng) {
    uniform_real_distribution<double> dist_x(0.0, 1.0);
    uniform_int_distribution<int> dist_y(0, 2);
    vector<Mau> D(n, {vector<double>(d), 0});
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < d; ++j) D[i].x[j] = dist_x(rng);
        D[i].y = dist_y(rng);
    }
    return D;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    mt19937 rng(12345);
    int d = 20;
    int q_size = 1000;

    // Sinh 1000 mau truy van
    vector<vector<double>> Q(q_size, vector<double>(d));
    uniform_real_distribution<double> dist_x(0.0, 1.0);
    for (int i = 0; i < q_size; ++i)
        for (int j = 0; j < d; ++j) Q[i][j] = dist_x(rng);

    vector<int> N_list = {1000, 10000, 100000};
    vector<double> T;

    for (int n : N_list) {
        vector<Mau> D = sinh_du_lieu(n, d, rng);

        auto t0 = chrono::high_resolution_clock::now();
        for (int i = 0; i < q_size; ++i) {
            phan_loai(Q[i], D);
        }
        auto t1 = chrono::high_resolution_clock::now();
        chrono::duration<double> elapsed = t1 - t0;
        T.push_back(elapsed.count());
        cout << "n = " << n << ": " << fixed << setprecision(4) << elapsed.count() << " s\n";
    }

    cout << "Ti le: T(10^4)/T(10^3) = " << fixed << setprecision(2) << T[1] / T[0] 
         << "x, T(10^5)/T(10^4) = " << T[2] / T[1] << "x\n";

    return 0;
}
