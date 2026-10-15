#include <iostream>

using namespace std;

long long luy_thua_mod(long long a, long long b, long long m) {
    if (m == 1) return 0;
    long long r = 1 % m;
    a %= m;
    while (b > 0) {
        if (b & 1) {
            // Dùng __int128 để tránh tràn số khi nhân hai số long long trước khi mod m
            r = ((__int128)r * a) % m;
        }
        a = ((__int128)a * a) % m;
        b >>= 1;
    }
    return r;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long a, b, m;
    while (cin >> a >> b >> m) {
        cout << luy_thua_mod(a, b, m) << "\n";
    }
    return 0;
}
