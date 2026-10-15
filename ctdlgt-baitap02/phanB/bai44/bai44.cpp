#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <iomanip>
#include <algorithm>

using namespace std;

// Cách 2 của Bài 39: O(n^2)
long long cach2(const vector<int>& a) {
    int n = a.size();
    long long max_sum = a[0];
    for (int i = 0; i < n; ++i) {
        long long cur = 0;
        for (int j = i; j < n; ++j) {
            cur += a[j];
            if (cur > max_sum) max_sum = cur;
        }
    }
    return max_sum;
}

double do_thoi_gian(const vector<int>& a, int lap = 3) {
    double min_t = 1e9;
    for (int r = 0; r < lap; ++r) {
        auto t0 = chrono::steady_clock::now();
        volatile long long res = cach2(a);
        double giay = chrono::duration<double>(chrono::steady_clock::now() - t0).count();
        min_t = min(min_t, giay);
    }
    return min_t;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    mt19937 rng(42);
    uniform_int_distribution<int> dist(-100, 100);

    vector<int> Ns = {500, 1000, 2000, 4000};
    vector<double> times;

    cout << fixed << setprecision(6);
    cout << "--- C++ BENCHMARK O(n^2) ---\n";
    for (int n : Ns) {
        vector<int> a(n);
        for (int i = 0; i < n; ++i) a[i] = dist(rng);
        double t = do_thoi_gian(a, 3);
        times.push_back(t);
        cout << "n = " << n << " : " << t << "s\n";
    }

    cout << "\n--- TI LE TANG ---\n";
    for (size_t i = 1; i < times.size(); ++i) {
        cout << "n = " << Ns[i-1] << " -> " << Ns[i] << " : ti le = " 
             << setprecision(2) << times[i] / times[i-1] << "\n";
    }
    return 0;
}
