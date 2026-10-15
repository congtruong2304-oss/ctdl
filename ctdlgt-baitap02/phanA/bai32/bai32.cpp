#include <iostream>
#include <algorithm>

using namespace std;

bool la_chinh_phuong(long long n) {
    if (n < 0) return false;
    long long left = 0, right = min(n, 1000000000LL);
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        long long sq = mid * mid;
        if (sq == n) {
            return true;
        } else if (sq < n) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n;
    while (cin >> n) {
        if (la_chinh_phuong(n)) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
    return 0;
}
