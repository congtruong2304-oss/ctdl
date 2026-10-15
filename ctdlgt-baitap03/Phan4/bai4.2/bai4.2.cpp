#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

pair<int, int> tim_cap_tong_s(vector<int> a, int S) {
    // Buoc 1: Sap xep mang ton O(n log n)
    sort(a.begin(), a.end());

    // Buoc 2: Hai con tro ton O(n)
    int i = 0;
    int j = (int)a.size() - 1;

    while (i < j) {
        int tong = a[i] + a[j];
        if (tong == S) {
            return {a[i], a[j]};
        } else if (tong < S) {
            i++;  // Loai bo a[i]
        } else {
            j--;  // Loai bo a[j]
        }
    }

    return {-1, -1}; // Khong tim thay
}

int main() {
    vector<int> A = {8, 3, 5, 1, 9, 2};
    int S = 10;

    pair<int, int> res = tim_cap_tong_s(A, S);
    if (res.first != -1) {
        cout << "Tim thay cap co tong bang " << S << ": " 
             << res.first << " + " << res.second << " = " << S << endl;
    } else {
        cout << "Khong tim thay cap nao co tong bang " << S << endl;
    }

    return 0;
}
