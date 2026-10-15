#include <iostream>
#include <vector>
#include <chrono>

using namespace std;

bool la_nguyen_to(int n) {
    if (n < 2) return false;
    for (int i = 2; 1LL * i * i <= n; ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

vector<int> sang_eratosthenes(int n) {
    vector<bool> check(n + 1, true);
    check[0] = check[1] = false;
    for (int p = 2; 1LL * p * p <= n; ++p) {
        if (check[p]) {
            for (int i = p * p; i <= n; i += p) {
                check[i] = false;
            }
        }
    }
    vector<int> primes;
    for (int p = 2; p <= n; ++p) {
        if (check[p]) primes.push_back(p);
    }
    return primes;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    while (cin >> n) {
        if (n <= 30) {
            vector<int> res = sang_eratosthenes(n);
            for (size_t i = 0; i < res.size(); ++i) {
                cout << res[i] << (i + 1 == res.size() ? "" : " ");
            }
            cout << "  (" << res.size() << " so)\n";
        } else if (n < 1000000) {
            vector<int> res = sang_eratosthenes(n);
            cout << "so luong = " << res.size() << "\n";
        } else {
            vector<int> res = sang_eratosthenes(n);
            long long tong = 0;
            for (int x : res) tong += x;
            cout << "so luong = " << res.size() << ", tong = " << tong << "\n";
        }
    }
    return 0;
}
