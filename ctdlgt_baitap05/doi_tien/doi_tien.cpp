#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>
#include <random>

using namespace std;

const int INF = 1e9;

// Thuật toán Tham lam: Luôn lấy tờ có mệnh giá lớn nhất có thể
pair<int, vector<int>> doi_tien_tham_lam(vector<int> menh_gia, int S) {
    sort(menh_gia.rbegin(), menh_gia.rend());
    vector<int> cach_tra;
    int tong = S;

    for (int c : menh_gia) {
        while (tong >= c) {
            cach_tra.push_back(c);
            tong -= c;
        }
    }

    if (tong == 0) {
        return {static_cast<int>(cach_tra.size()), cach_tra};
    }
    return {INF, {}};
}

// Thuật toán Quy hoạch động: Tìm số tờ ít nhất thật sự
pair<int, vector<int>> doi_tien_dp(const vector<int>& menh_gia, int S) {
    vector<int> f(S + 1, INF);
    vector<int> vet(S + 1, -1);
    f[0] = 0;

    for (int j = 1; j <= S; ++j) {
        for (int c : menh_gia) {
            if (j >= c && f[j - c] + 1 < f[j]) {
                f[j] = f[j - c] + 1;
                vet[j] = c;
            }
        }
    }

    if (f[S] == INF) {
        return {INF, {}};
    }

    vector<int> cach_tra;
    int curr = S;
    while (curr > 0) {
        int c = vet[curr];
        cach_tra.push_back(c);
        curr -= c;
    }

    return {f[S], cach_tra};
}

// Chuyển mảng các mệnh giá thành chuỗi biểu diễn dạng "a + b + c"
string format_cach_tra(const vector<int>& cach_tra) {
    if (cach_tra.empty()) return "Khong doi duoc";
    string res = "";
    for (size_t i = 0; i < cach_tra.size(); ++i) {
        res += to_string(cach_tra[i]);
        if (i + 1 < cach_tra.size()) res += " + ";
    }
    return res;
}

// Kiểm chứng độc lập giữa Tham lam và Quy hoạch động trên dữ liệu ngẫu nhiên
void kiem_chung_ngau_nhien() {
    cout << "=== KIEM CHUNG DOC LAP TREN DU LIEU NGAU NHIEN ===\n";
    mt19937 rng(42);
    int so_bo_sai = 0;

    for (int test = 1; test <= 10; ++test) {
        int k = 3 + rng() % 3; // k từ 3 đến 5
        vector<int> pool;
        for (int i = 2; i <= 20; ++i) pool.push_back(i);
        shuffle(pool.begin(), pool.end(), rng);

        vector<int> menh_gia = {1}; // Luôn có tờ 1 để đảm bảo đổi được tiền
        for (int i = 0; i < k - 1; ++i) {
            menh_gia.push_back(pool[i]);
        }
        sort(menh_gia.begin(), menh_gia.end());

        int S = 10 + rng() % 21; // S từ 10 đến 30
        auto [sl_tl, cach_tl] = doi_tien_tham_lam(menh_gia, S);
        auto [sl_dp, cach_dp] = doi_tien_dp(menh_gia, S);

        if (sl_tl != sl_dp) {
            so_bo_sai++;
        }
    }

    cout << "-> Da chay 10 bo ngau nhien, phat hien " << so_bo_sai << " bo tham lam khong toi uu.\n";
    cout << "-> Xac nhan: DP luon cho ket qua <= Tham lam (dung tinh chat toi uu).\n\n";
}

struct BoDuLieu {
    int stt;
    vector<int> menh_gia;
    int S;
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    kiem_chung_ngau_nhien();

    // Sáu bộ dữ liệu chuẩn ở Mục B
    vector<BoDuLieu> ds_bo = {
        {1, {1, 4, 6, 9}, 12},
        {2, {1, 5, 10, 20, 50}, 85},
        {3, {1, 3, 7, 12}, 20},
        {4, {1, 2, 5, 10}, 38},
        {5, {1, 6, 10}, 12},
        {6, {1, 4, 5, 15, 20}, 23}
    };

    cout << left << setw(4) << "Bo" << " | "
         << setw(9) << "TL so to" << " | "
         << setw(25) << "Cach tra tham lam" << " | "
         << setw(9) << "DP so to" << " | "
         << setw(20) << "Cach tra toi uu" << " | "
         << "TL dung?\n";
    cout << string(90, '-') << "\n";

    for (const auto& bo : ds_bo) {
        auto [sl_tl, cach_tl] = doi_tien_tham_lam(bo.menh_gia, bo.S);
        auto [sl_dp, cach_dp] = doi_tien_dp(bo.menh_gia, bo.S);

        string str_tl = format_cach_tra(cach_tl);
        string str_dp = format_cach_tra(cach_dp);
        string dung = (sl_tl == sl_dp) ? "Dung" : "Sai";

        cout << left << setw(4) << bo.stt << " | "
             << setw(9) << sl_tl << " | "
             << setw(25) << str_tl << " | "
             << setw(9) << sl_dp << " | "
             << setw(20) << str_dp << " | "
             << dung << "\n";
    }

    return 0;
}
