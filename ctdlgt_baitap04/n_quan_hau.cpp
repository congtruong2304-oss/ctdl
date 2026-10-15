#include <iostream>
#include <vector>

using namespace std;

int N;
int so_loi_giai = 0;
int so_nut = 0;
vector<int> x;
vector<int> loi_giai_dau;
vector<bool> cot, cheo1, cheo2;

void dat_hau(int i) {
    so_nut++; // Mỗi lần gọi hàm đệ quy tính là một nút

    if (i == N) {
        so_loi_giai++;
        if (loi_giai_dau.empty()) {
            loi_giai_dau = x; // Lưu lại cấu hình lời giải đầu tiên
        }
        return;
    }

    for (int j = 0; j < N; j++) {
        if (!cot[j] && !cheo1[i + j] && !cheo2[i - j + N]) {
            x[i] = j;
            cot[j] = cheo1[i + j] = cheo2[i - j + N] = true;
            dat_hau(i + 1);
            cot[j] = cheo1[i + j] = cheo2[i - j + N] = false; // Hoàn tác
        }
    }
}

int main() {
    cout << "Nhap n: ";
    if (!(cin >> N) || N <= 0) return 0;

    x.assign(N, 0);
    cot.assign(N, false);
    cheo1.assign(2 * N, false);
    cheo2.assign(2 * N, false);

    dat_hau(0);

    cout << "So nut da duyet: " << so_nut << "\n";
    cout << "So loi giai: " << so_loi_giai << "\n";

    if (!loi_giai_dau.empty()) {
        cout << "Loi giai dau tien (dang chi so 1..n): [";
        for (int i = 0; i < N; i++) {
            cout << loi_giai_dau[i] + 1 << (i == N - 1 ? "" : ", ");
        }
        cout << "]\n";

        cout << "Ban co cua loi giai dau tien (. la o trong, Q la quan hau):\n";
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                cout << (loi_giai_dau[r] == c ? "Q " : ". ");
            }
            cout << "\n";
        }
    } else {
        cout << "Khong co loi giai nao.\n";
    }

    return 0;
}
