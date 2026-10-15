#include <iostream>
#include <vector>

using namespace std;

struct KetQua {
    long long tong;
    int dau, cuoi; // danh so tu 1
};

KetQua kadane_chi_so(const vector<int>& a) {
    long long max_sum = a[0];
    long long cur_sum = a[0];
    int best_start = 1, best_end = 1;
    int cur_start = 1;

    for (size_t i = 1; i < a.size(); ++i) {
        if ((long long)a[i] > cur_sum + a[i]) {
            cur_sum = a[i];
            cur_start = i + 1;
        } else {
            cur_sum += a[i];
        }

        if (cur_sum > max_sum) {
            max_sum = cur_sum;
            best_start = cur_start;
            best_end = i + 1;
        }
    }
    return {max_sum, best_start, best_end};
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
        KetQua res = kadane_chi_so(a);
        cout << "tong " << res.tong << ", doan [" << res.dau << ".." << res.cuoi << "]\n";
    }
    return 0;
}
