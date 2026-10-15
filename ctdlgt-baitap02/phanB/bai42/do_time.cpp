#include <iostream>
#include <vector>
#include <chrono>
#include <random>
#include <iomanip>

using namespace std;

// Cách ngây thơ O(n * k) - chạy thử trên 10000 cửa sổ rồi quy đổi
long long ngay_tho(const vector<int>& a, int k, int limit_steps) {
    long long max_sum = -1e18;
    for (int i = 0; i <= limit_steps; ++i) {
        long long cur = 0;
        for (int j = 0; j < k; ++j) {
            cur += a[i + j];
        }
        if (cur > max_sum) max_sum = cur;
    }
    return max_sum;
}

// Cửa sổ trượt O(n)
long long cua_so_truot(const vector<int>& a, int k) {
    int n = a.size();
    long long cur = 0;
    for (int i = 0; i < k; ++i) cur += a[i];
    long long max_sum = cur;
    for (int i = k; i < n; ++i) {
        cur += a[i] - a[i - k];
        if (cur > max_sum) max_sum = cur;
    }
    return max_sum;
}

int main() {
    int n = 1000000, k = 1000;
    mt19937 rng(42);
    uniform_int_distribution<int> dist(-100, 100);
    vector<int> a(n);
    for (int i = 0; i < n; ++i) a[i] = dist(rng);

    cout << fixed << setprecision(6);
    cout << "--- C++ BENCHMARK (n=10^6, k=1000) ---\n";

    // Đo ngây thơ (chạy mẫu 10,000 bước để tránh chờ quá lâu)
    int sample_steps = 10000;
    auto t0 = chrono::steady_clock::now();
    volatile long long r1 = ngay_tho(a, k, sample_steps);
    double t_sample = chrono::duration<double>(chrono::steady_clock::now() - t0).count();
    double t_ngay_tho = t_sample * ((double)(n - k + 1) / sample_steps);

    // Đo cửa sổ trượt
    t0 = chrono::steady_clock::now();
    volatile long long r2 = cua_so_truot(a, k);
    double t_truot = chrono::duration<double>(chrono::steady_clock::now() - t0).count();

    cout << "Ngay tho O(n*k) : " << t_ngay_tho << "s\n";
    cout << "Cua so truot O(n): " << t_truot << "s\n";
    cout << "Ti le nhanh hon : " << setprecision(2) << (t_ngay_tho / t_truot) << " lan\n";
    return 0;
}
