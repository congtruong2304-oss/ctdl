#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    if (!(cin >> n) || n <= 0) return 0;

    long long first_val;
    cin >> first_val;

    long long tong = first_val;
    long long nho_nhat = first_val;
    long long lon_nhat = first_val;

    for (int i = 1; i < n; ++i) {
        long long x;
        cin >> x;
        tong += x;
        if (x < nho_nhat) nho_nhat = x;
        if (x > lon_nhat) lon_nhat = x;
    }

    double trung_binh = (double)tong / n;

    cout << tong << " " 
         << fixed << setprecision(4) << trung_binh << " " 
         << nho_nhat << " " 
         << lon_nhat << "\n";

    return 0;
}
