#include <iostream>
#include <utility>

using namespace std;

pair<int, int> phan_tich(long long n) {
    int so_chu_so = 0;
    int tong_chu_so = 0;
    while (n > 0) {
        tong_chu_so += n % 10;
        so_chu_so++;
        n /= 10;
    }
    return {so_chu_so, tong_chu_so};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    long long n;
    while (cin >> n) {
        pair<int, int> kq = phan_tich(n);
        cout << kq.first << " " << kq.second << "\n";
    }
    return 0;
}
