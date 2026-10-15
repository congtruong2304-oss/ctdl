#include <iostream>
#include <vector>
#include <climits>

using namespace std;

long long dem = 0;

long long fib_de_quy(int n) {
    dem++;
    if (n <= 0) return 0;
    if (n <= 2) return 1; // Base case chuẩn theo đề
    return fib_de_quy(n - 1) + fib_de_quy(n - 2);
}

long long fib_ghi_nho_helper(int n, vector<long long>& memo) {
    if (n <= 0) return 0;
    if (n <= 2) return 1;
    if (memo[n] != -1) return memo[n];
    return memo[n] = fib_ghi_nho_helper(n - 1, memo) + fib_ghi_nho_helper(n - 2, memo);
}

long long fib_ghi_nho(int n) {
    if (n <= 0) return 0;
    vector<long long> memo(n + 1, -1);
    return fib_ghi_nho_helper(n, memo);
}

long long fib_lap(int n) {
    if (n <= 0) return 0;
    if (n <= 2) return 1;
    if (n > 92) return -1;

    long long prev2 = 1, prev1 = 1, cur = 0;
    for (int i = 3; i <= n; ++i) {
        if (LLONG_MAX - prev1 < prev2) return -1;
        cur = prev1 + prev2;
        prev2 = prev1;
        prev1 = cur;
    }
    return cur;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    while (cin >> n) {
        if (n <= 30) {
            dem = 0;
            long long f = fib_de_quy(n);
            cout << "F = " << f << ", so loi goi = " << dem << "\n";
        } else {
            long long f = fib_lap(n);
            if (f == -1) {
                cout << "tran long long\n";
            } else {
                cout << "F = " << f << "\n";
            }
        }
    }
    return 0;
}
