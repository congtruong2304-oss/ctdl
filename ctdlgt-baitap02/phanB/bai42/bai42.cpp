#include <iostream>
#include <vector>

using namespace std;

pair<long long, int> cua_so_truot(const vector<int>& a, int k) {
    int n = a.size();
    long long cur_sum = 0;
    for (int i = 0; i < k; ++i) {
        cur_sum += a[i];
    }

    long long max_sum = cur_sum;
    int best_pos = 1; // Danh so tu 1

    for (int i = k; i < n; ++i) {
        cur_sum += a[i] - a[i - k];
        if (cur_sum > max_sum) {
            max_sum = cur_sum;
            best_pos = i - k + 2;
        }
    }
    return {max_sum, best_pos};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, k;
    while (cin >> n >> k) {
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        pair<long long, int> res = cua_so_truot(a, k);
        cout << "tong " << res.first << ", bat dau tai vi tri " << res.second << "\n";
    }
    return 0;
}
