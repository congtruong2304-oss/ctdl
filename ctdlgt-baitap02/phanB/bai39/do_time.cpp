#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <iomanip>
#include <algorithm>

using namespace std;

long long cach1(const vector<int>& a) {
    int n = a.size();
    long long max_sum = a[0];
    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            long long cur = 0;
            for (int k = i; k <= j; ++k) cur += a[k];
            max_sum = max(max_sum, cur);
        }
    }
    return max_sum;
}

long long cach2(const vector<int>& a) {
    int n = a.size();
    long long max_sum = a[0];
    for (int i = 0; i < n; ++i) {
        long long cur = 0;
        for (int j = i; j < n; ++j) {
            cur += a[j];
            max_sum = max(max_sum, cur);
        }
    }
    return max_sum;
}

long long kadane(const vector<int>& a) {
    int n = a.size();
    long long max_sum = a[0];
    long long cur_sum = a[0];
    for (int i = 1; i < n; ++i) {
        cur_sum = max((long long)a[i], cur_sum + a[i]);
        max_sum = max(max_sum, cur_sum);
    }
    return max_sum;
}

int main() {
    mt19937 rng(42);
    uniform_int_distribution<int> dist(-100, 100);

    cout << fixed << setprecision(6);
    cout << "--- C++ BENCHMARK ---\n";
    for (int n : {200, 400, 800}) {
        vector<int> a(n);
        for (int i = 0; i < n; ++i) a[i] = dist(rng);

        // Cách 1: Chạy 5 lần lấy trung bình
        auto t0 = chrono::steady_clock::now();
        volatile long long res1 = 0;
        for (int r = 0; r < 5; ++r) res1 += cach1(a);
        double t_c1 = chrono::duration<double>(chrono::steady_clock::now() - t0).count() / 5.0;

        // Cách 2: Chạy 50 lần lấy trung bình
        t0 = chrono::steady_clock::now();
        volatile long long res2 = 0;
        for (int r = 0; r < 50; ++r) res2 += cach2(a);
        double t_c2 = chrono::duration<double>(chrono::steady_clock::now() - t0).count() / 50.0;

        // Cách 3: Chạy 10000 lần lấy trung bình
        t0 = chrono::steady_clock::now();
        volatile long long res3 = 0;
        for (int r = 0; r < 10000; ++r) res3 += kadane(a);
        double t_c3 = chrono::duration<double>(chrono::steady_clock::now() - t0).count() / 10000.0;

        cout << "n = " << n << " | Cach 1: " << t_c1 << "s | Cach 2: " << t_c2 << "s | Kadane: " << t_c3 << "s\n";
    }
    return 0;
}
