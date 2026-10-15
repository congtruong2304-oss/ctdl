#include <iostream>
#include <climits>

using namespace std;

bool giai_thua(int n, long long &kq) {
    if (n < 0) return false;
    kq = 1;
    for (int i = 1; i <= n; ++i) {
        if (kq > LLONG_MAX / i) {
            return false;
        }
        kq *= i;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    while (cin >> n) {
        long long kq = 0;
        if (giai_thua(n, kq)) {
            cout << kq << "\n";
        } else {
            cout << "TRAN SO\n";
        }
    }
    return 0;
}
