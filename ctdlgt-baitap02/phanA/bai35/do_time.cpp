#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>

using namespace std;

bool la_nguyen_to(int n) {
    if (n < 2) return false;
    for (int i = 2; 1LL * i * i <= n; ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

int sang(int n) {
    vector<bool> check(n + 1, true);
    check[0] = check[1] = false;
    for (int p = 2; 1LL * p * p <= n; ++p) {
        if (check[p]) {
            for (int i = p * p; i <= n; i += p) {
                check[i] = false;
            }
        }
    }
    int cnt = 0;
    for (int p = 2; p <= n; ++p) {
        if (check[p]) cnt++;
    }
    return cnt;
}

int main() {
    cout << fixed << setprecision(4);
    for (int n : {100000, 1000000}) {
        // Do kiem tra tung so
        auto t0 = chrono::steady_clock::now();
        int dem1 = 0;
        for (int i = 2; i <= n; ++i) {
            if (la_nguyen_to(i)) dem1++;
        }
        auto t1 = chrono::steady_clock::now();
        double t_kt = chrono::duration<double>(t1 - t0).count();

        // Do sang Eratosthenes
        t0 = chrono::steady_clock::now();
        int dem2 = sang(n);
        t1 = chrono::steady_clock::now();
        double t_sang = chrono::duration<double>(t1 - t0).count();

        // In ket qua (dung bien dem1, dem2 de tranh bi trinh bien dich toi uu bo qua)
        cout << "n = " << n << ": Kiem tra = " << t_kt << "s, Sang = " << t_sang 
             << "s (so luong: " << dem1 << " - " << dem2 << ")\n";
    }
    return 0;
}
