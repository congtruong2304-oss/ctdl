#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int INF = 1e9;
const int N = 5;

// Ma trận chi phí 5 thành phố mục D
int cost_matrix[N][N] = {
    {0,  10, 25, 25, 10},
    {1,  0,  10, 15, 2},
    {8,  9,  0,  20, 10},
    {14, 10, 24, 0,  15},
    {10, 8,  25, 27, 0}
};

int c_min = INF;
int best_cost = INF;
int so_nut = 0;
vector<int> path(N + 1, 0);
vector<int> best_path(N + 1, 0);
vector<bool> visited(N, false);

void quay_lui(int k, int curr_city, int curr_cost, bool co_cat_nhanh) {
    so_nut++;

    // Đã thăm đủ N thành phố (k = N - 1), khép góc về thành phố 0
    if (k == N - 1) {
        int canh_ve = cost_matrix[curr_city][0];
        int tong_chi_phi = curr_cost + canh_ve;
        if (tong_chi_phi < best_cost) {
            best_cost = tong_chi_phi;
            path[N] = 0;
            best_path = path;
        }
        return;
    }

    for (int next_city = 0; next_city < N; next_city++) {
        if (!visited[next_city]) {
            int next_cost = curr_cost + cost_matrix[curr_city][next_city];
            // Số cạnh còn lại gồm: (N - 1 - k) cạnh tới các đỉnh chưa thăm + 1 cạnh khép góc về 0
            int so_canh_con_lai = N - (k + 1);
            int can_duoi = next_cost + so_canh_con_lai * c_min;

            if (co_cat_nhanh) {
                // Chỉ duyệt tiếp nếu cận dưới nhỏ hơn kỷ lục hiện tại
                if (can_duoi < best_cost) {
                    visited[next_city] = true;
                    path[k + 1] = next_city;
                    quay_lui(k + 1, next_city, next_cost, co_cat_nhanh);
                    visited[next_city] = false; // Hoàn tác
                }
            } else {
                // Không cắt nhánh: duyệt toàn bộ
                visited[next_city] = true;
                path[k + 1] = next_city;
                quay_lui(k + 1, next_city, next_cost, co_cat_nhanh);
                visited[next_city] = false; // Hoàn tác
            }
        }
    }
}

int main() {
    // 1. Tìm cạnh nhỏ nhất toàn ma trận (bỏ qua đường chéo chính i == j)
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i != j) {
                c_min = min(c_min, cost_matrix[i][j]);
            }
        }
    }

    // 2. Chạy chế độ CÓ cắt nhánh
    best_cost = INF;
    so_nut = 0;
    fill(visited.begin(), visited.end(), false);
    visited[0] = true;
    path[0] = 0;
    quay_lui(0, 0, 0, true);
    int nut_cat = so_nut;
    int chi_phi_toi_uu = best_cost;
    vector<int> hanh_trinh_toi_uu = best_path;

    // 3. Chạy chế độ KHÔNG cắt nhánh
    best_cost = INF;
    so_nut = 0;
    fill(visited.begin(), visited.end(), false);
    visited[0] = true;
    path[0] = 0;
    quay_lui(0, 0, 0, false);
    int nut_khong = so_nut;

    // In kết quả đúng chuẩn theo bảng yêu cầu của báo cáo
    cout << "Canh re nhat toan ma tran c_min: " << c_min << "\n";
    cout << "Chi phi hanh trinh toi uu: " << chi_phi_toi_uu << "\n";
    cout << "Hanh trinh toi uu: ";
    for (int i = 0; i <= N; i++) {
        cout << hanh_trinh_toi_uu[i] << (i == N ? "" : " -> ");
    }
    cout << "\n";
    cout << "So nut khi CO cat nhanh: " << nut_cat << "\n";
    cout << "So nut khi KHONG cat nhanh: " << nut_khong << "\n";

    return 0;
}
