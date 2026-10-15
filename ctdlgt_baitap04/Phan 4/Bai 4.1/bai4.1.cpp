#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;

struct DoVat {
    string ten;
    int w;
    int v;
    double don_gia; // v / w
};

int W = 14;
int n;
vector<DoVat> ds;

int max_val = 0;
int so_nut = 0;
vector<int> x;
vector<int> best_chon;

// Tính cận trên bằng tham lam phân số (Fractional Knapsack)
double tinh_can_tren(int i, int w_con_lai, int v_hien_tai) {
    double can = v_hien_tai;
    int w_tam = w_con_lai;
    for (int k = i; k < n; k++) {
        if (ds[k].w <= w_tam) {
            w_tam -= ds[k].w;
            can += ds[k].v;
        } else {
            // Lấy một phần phân số của vật k
            can += ds[k].don_gia * w_tam;
            break;
        }
    }
    return can;
}

void quay_lui(int i, int w_hien_tai, int v_hien_tai, bool co_cat_nhanh) {
    so_nut++;

    // Cập nhật giá trị kỷ lục tạm thời
    if (v_hien_tai > max_val) {
        max_val = v_hien_tai;
        best_chon = x;
    }

    if (i == n) return;

    // Nhánh 1: CHỌN vật i (x[i] = 1) - ưu tiên xét trước vì đã sắp v/w giảm dần
    if (w_hien_tai + ds[i].w <= W) {
        x[i] = 1;
        quay_lui(i + 1, w_hien_tai + ds[i].w, v_hien_tai + ds[i].v, co_cat_nhanh);
        x[i] = 0; // Hoàn tác
    }

    // Nhánh 2: KHÔNG CHỌN vật i (x[i] = 0)
    x[i] = 0;
    int w_con_lai = W - w_hien_tai;
    if (co_cat_nhanh) {
        // Cắt nhánh: chỉ xét tiếp nếu cận trên còn tiềm năng vượt qua max_val
        double ub = tinh_can_tren(i + 1, w_con_lai, v_hien_tai);
        if (ub > max_val) {
            quay_lui(i + 1, w_hien_tai, v_hien_tai, co_cat_nhanh);
        }
    } else {
        // Không cắt nhánh: duyệt hết mọi cấu hình hợp lệ
        quay_lui(i + 1, w_hien_tai, v_hien_tai, co_cat_nhanh);
    }
}

int main() {
    // Khởi tạo danh sách 6 đồ vật mục C
    ds = {
        {"A", 4, 12, 12.0 / 4},
        {"B", 7, 25, 25.0 / 7},
        {"C", 3, 7, 7.0 / 3},
        {"D", 3, 8, 8.0 / 3},
        {"E", 3, 9, 9.0 / 3},
        {"F", 10, 21, 21.0 / 10}
    };
    n = ds.size();

    // BẮT BUỘC: Sắp xếp các đồ vật theo tỉ số v/w giảm dần
    sort(ds.begin(), ds.end(), [](const DoVat& a, const DoVat& b) {
        return a.don_gia > b.don_gia;
    });

    cout << "=== THU TU DO VAT SAU KHI SAP XEP THEO v/w GIAM DAN ===\n";
    for (int i = 0; i < n; i++) {
        cout << i + 1 << ". Vat " << ds[i].ten 
             << ": w = " << ds[i].w 
             << ", v = " << ds[i].v 
             << ", v/w = " << fixed << setprecision(3) << ds[i].don_gia << "\n";
    }

    // Chế độ 1: CÓ cắt nhánh
    max_val = 0;
    so_nut = 0;
    x.assign(n, 0);
    best_chon.assign(n, 0);
    quay_lui(0, 0, 0, true);
    int nut_cat = so_nut;
    int max_val_cat = max_val;
    vector<int> best_chon_cat = best_chon;

    // Chế độ 2: KHÔNG cắt nhánh
    max_val = 0;
    so_nut = 0;
    x.assign(n, 0);
    best_chon.assign(n, 0);
    quay_lui(0, 0, 0, false);
    int nut_khong = so_nut;

    cout << "\n==================================================\n";
    cout << "Suc chua W = " << W << "\n";
    cout << "Gia tri lon nhat: " << max_val_cat << "\n";
    cout << "Tap do vat duoc chon: [";
    bool first = true;
    int tong_w = 0;
    for (int i = 0; i < n; i++) {
        if (best_chon_cat[i] == 1) {
            if (!first) cout << ", ";
            cout << "'" << ds[i].ten << "'";
            tong_w += ds[i].w;
            first = false;
        }
    }
    cout << "] (Tong w = " << tong_w << ")\n";
    cout << "So nut khi CO cat nhanh: " << nut_cat << "\n";
    cout << "So nut khi KHONG cat nhanh: " << nut_khong << "\n";
    cout << "So nut giam duoc: " << fixed << setprecision(2) << (double)nut_khong / nut_cat << " lan\n";

    return 0;
}
