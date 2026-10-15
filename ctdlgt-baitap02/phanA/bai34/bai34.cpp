#include <iostream>
#include <cmath>

using namespace std;

long long dao_nguoc(long long n) {
    long long sign = (n < 0) ? -1 : 1;
    long long m = llabs(n);
    long long rev = 0;
    while (m > 0) {
        rev = rev * 10 + (m % 10);
        m /= 10;
    }
    return sign * rev;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n;
    while (cin >> n) {
        cout << dao_nguoc(n) << "\n";
    }
    return 0;
}
