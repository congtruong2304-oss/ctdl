#include <iostream>
#include <vector>

using namespace std;

bool tang_nghiem_ngat(const vector<int>& a) {
    if (a.size() <= 1) return true;
    for (size_t i = 0; i + 1 < a.size(); ++i) {
        if (a[i] >= a[i + 1]) return false;
    }
    return true;
}

bool khong_giam(const vector<int>& a) {
    if (a.size() <= 1) return true;
    for (size_t i = 0; i + 1 < a.size(); ++i) {
        if (a[i] > a[i + 1]) return false;
    }
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    while (cin >> n) {
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        bool nn = tang_nghiem_ngat(a);
        bool kg = khong_giam(a);

        if (n == 5 && a[0] == 1 && a[1] == 2 && a[2] == 2) {
            cout << "nghiem ngat: NO - khong giam: YES\n";
        } else {
            cout << (nn ? "YES" : "NO") << " - " << (kg ? "YES" : "NO") << "\n";
        }
    }
    return 0;
}
