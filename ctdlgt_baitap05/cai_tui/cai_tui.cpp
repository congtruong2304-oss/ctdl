#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
#include <algorithm>
#include <numeric>

using namespace std;

// Cấu trúc trả về gồm: bảng f, giá trị lớn nhất, và danh sách các đồ vật được chọn
struct KetQua {
    vector<vector<int>> f;
    int max_val;
    vector<int> chon;
};

KetQua cai_tui(const vector<int> &w, const vector<int> &v, int W) {
    int n = w.size();
    // Bảng f kích thước (n + 1) x (W + 1) khởi tạo toàn bộ giá trị 0
    vector<vector<int>> f(n + 1, vector<int>(W + 1, 0));

    // Điền bảng quy hoạch động
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= W; j++) {
            f[i][j] = f[i - 1][j]; // Phương án không lấy đồ vật i
            if (w[i - 1] <= j) {   // Nếu còn đủ sức chứa thì thử lấy đồ vật i
                f[i][j] = max(f[i][j], f[i - 1][j - w[i - 1]] + v[i - 1]);
            }
        }
    }

    // Truy vết từ ô f[n][W]
    vector<int> chon;
    int j = W;
    for (int i = n; i > 0; i--) {
        if (f[i][j] != f[i - 1][j]) { // Giá trị thay đổi => đồ vật i đã được chọn
            chon.push_back(i);
            j -= w[i - 1];            // Trả lại sức chứa
        }
    }

    reverse(chon.begin(), chon.end()); // Đảo lại theo thứ tự từ 1 đến n
    return {f, f[n][W], chon};
}

int main() {
    // Tối ưu hóa nhập xuất
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Bộ dữ liệu chuẩn mục A
    int n = 5;
    int W = 11;
    vector<string> ten = {"A", "B", "C", "D", "E"};
    vector<int> w = {2, 3, 4, 5, 7};
    vector<int> v = {3, 7, 9, 12, 16};

    KetQua kq = cai_tui(w, v, W);

    // 1. In toàn bộ bảng f (6 hàng x 12 cột = 72 ô)
    cout << "=== BANG QUY HOACH DONG f[i][j] ===\n";
    cout << left << setw(10) << "f[i][j]";
    for (int j = 0; j <= W; j++) {
        cout << right << setw(4) << j;
    }
    cout << "\n" << string(10 + 4 * (W + 1), '-') << "\n";

    for (int i = 0; i <= n; i++) {
        string nhan = (i == 0) ? "i=0" : "i=" + to_string(i) + " (" + ten[i - 1] + ")";
        cout << left << setw(10) << nhan;
        for (int j = 0; j <= W; j++) {
            cout << right << setw(4) << kq.f[i][j];
        }
        cout << "\n";
    }
    cout << string(10 + 4 * (W + 1), '-') << "\n";

    // 2. In giá trị lớn nhất
    cout << "\nGia tri lon nhat f[" << n << "][" << W << "] = " << kq.max_val << "\n";

    // 3. In tập đồ vật được chọn sau khi truy vết
    cout << "Tap do vat duoc chon: [";
    int tong_w = 0, tong_v = 0;
    for (size_t idx = 0; idx < kq.chon.size(); idx++) {
        int item_idx = kq.chon[idx] - 1;
        tong_w += w[item_idx];
        tong_v += v[item_idx];
        cout << "'" << ten[item_idx] << "'" << (idx + 1 < kq.chon.size() ? ", " : "");
    }
    cout << "] (cac chi so: [";
    for (size_t idx = 0; idx < kq.chon.size(); idx++) {
        cout << kq.chon[idx] << (idx + 1 < kq.chon.size() ? ", " : "");
    }
    cout << "])\n";

    cout << "Tong trong luong: " << tong_w << "/" << W << "\n";
    cout << "Tong gia tri: " << tong_v << "\n";

    return 0;
}
