#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

long long cach1(const vector<int>& a) {
    int n = a.size();
    long long max_sum = a[0];
    for (int i = 0; i < n; ++i) {
        for (int j = i; j < n; ++j) {
            long long cur = 0;
            for (int k = i; k <= j; ++k) {
                cur += a[k];
            }
            max_sum = max(max_sum, cur);
        }
    }
    return max_sum;
}

long long cach2(const vector<int>& a) {
    int n = a.size();
    long long max_sum = a[0];
    for (int i = 0; i < n; ++i) {
        long long cur = 0;
        for (int j = i; j < n; ++j) {
            cur += a[j];
            max_sum = max(max_sum, cur);
        }
    }
    return max_sum;
}

long long kadane(const vector<int>& a) {
    int n = a.size();
    long long max_sum = a[0];
    long long cur_sum = a[0];
    for (int i = 1; i < n; ++i) {
        cur_sum = max((long long)a[i], cur_sum + a[i]);
        max_sum = max(max_sum, cur_sum);
    }
    return max_sum;
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
        cout << kadane(a) << "\n";
    }
    return 0;
}
