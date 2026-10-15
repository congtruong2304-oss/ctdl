#include <iostream>
#include <vector>

using namespace std;

void dem(const vector<int>& a, int &chan, int &le, int &am) {
    chan = 0;
    le = 0;
    am = 0;
    for (int x : a) {
        if (x < 0) am++;
        if (x % 2 == 0) chan++;
        else le++;
    }
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
        int chan = 0, le = 0, am = 0;
        dem(a, chan, le, am);
        cout << "chan " << chan << ", le " << le << ", am " << am << "\n";
    }
    return 0;
}
