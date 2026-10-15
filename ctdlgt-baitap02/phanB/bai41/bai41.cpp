#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

long long tich_lon_nhat_n2(const vector<int>& a) {
    int n = a.size();
    long long ans = a[0];
    for (int i = 0; i < n; ++i) {
        long long cur = 1;
        for (int j = i; j < n; ++j) {
            cur *= a[j];
            ans = max(ans, cur);
        }
    }
    return ans;
}

long long tich_lon_nhat(const vector<int>& a) {
    int n = a.size();
    long long ans = a[0];
    long long max_prod = a[0];
    long long min_prod = a[0];

    for (int i = 1; i < n; ++i) {
        if (a[i] < 0) {
            swap(max_prod, min_prod);
        }
        max_prod = max((long long)a[i], max_prod * a[i]);
        min_prod = min((long long)a[i], min_prod * a[i]);
        ans = max(ans, max_prod);
    }
    return ans;
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
        cout << tich_lon_nhat(a) << "\n";
    }
    return 0;
}
