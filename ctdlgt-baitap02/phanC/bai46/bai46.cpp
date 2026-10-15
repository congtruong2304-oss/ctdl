#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <iomanip>

using namespace std;

struct Mau {
    vector<double> x;
    string y;
};

double tinh_khoang_cach(const vector<double>& u, const vector<double>& v) {
    double sum = 0.0;
    for (size_t i = 0; i < u.size(); ++i) {
        double diff = u[i] - v[i];
        sum += diff * diff;
    }
    return sqrt(sum);
}

struct KetQua {
    string nhan;
    double kc;
    int chi_so;
};

KetQua lang_gieng_gan_nhat(const vector<double>& q, const vector<Mau>& D) {
    double min_dist = 1e18;
    string best_label = "";
    int best_idx = -1;

    for (size_t i = 0; i < D.size(); ++i) {
        double dist = tinh_khoang_cach(q, D[i].x);
        if (dist < min_dist) {
            min_dist = dist;
            best_label = D[i].y;
            best_idx = i + 1; // Đánh số thứ tự từ 1
        }
    }
    return {best_label, min_dist, best_idx};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<Mau> D = {
        {{1.4, 0.2}, "Setosa"},
        {{1.3, 0.2}, "Setosa"},
        {{1.5, 0.2}, "Setosa"},
        {{4.7, 1.4}, "Versicolor"},
        {{4.5, 1.5}, "Versicolor"},
        {{4.9, 1.5}, "Versicolor"},
        {{6.0, 2.5}, "Virginica"},
        {{5.8, 2.1}, "Virginica"}
    };

    double x1, x2;
    while (cin >> x1 >> x2) {
        vector<double> q = {x1, x2};
        KetQua res = lang_gieng_gan_nhat(q, D);
        
        if (res.kc < 1e-9) {
            cout << res.nhan << " - trung dung mau " << res.chi_so << ", khoang cach 0\n";
        } else {
            cout << res.nhan << " - lang gieng la mau " << res.chi_so << ", khoang cach ";
            if (abs(res.kc - round(res.kc * 10.0) / 10.0) < 1e-5) {
                cout << fixed << setprecision(1) << res.kc << "\n";
            } else {
                cout << fixed << setprecision(4) << res.kc << "\n";
            }
        }
    }
    return 0;
}
