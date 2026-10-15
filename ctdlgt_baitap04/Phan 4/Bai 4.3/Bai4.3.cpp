#include <iostream>
#include <vector>
#include <chrono>
#include <iomanip>

using namespace std;
using namespace std::chrono;

const int N = 9;

// Kiểm tra số val có hợp lệ khi đặt vào ô (r, c) không
bool is_valid(const vector<vector<int>>& board, int r, int c, int val) {
    for (int i = 0; i < N; i++) {
        if (board[r][i] == val || board[i][c] == val) return false;
    }
    int br = (r / 3) * 3, bc = (c / 3) * 3;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (board[br + i][bc + j] == val) return false;
        }
    }
    return true;
}

// Lấy danh sách các ứng viên hợp lệ cho ô (r, c)
vector<int> get_candidates(const vector<vector<int>>& board, int r, int c) {
    vector<int> cands;
    for (int val = 1; val <= 9; val++) {
        if (is_valid(board, r, c, val)) {
            cands.push_back(val);
        }
    }
    return cands;
}

// ================= 1. QUÉT TUẦN TỰ =================
bool find_empty_sequential(const vector<vector<int>>& board, int& r, int& c) {
    for (r = 0; r < N; r++) {
        for (c = 0; c < N; c++) {
            if (board[r][c] == 0) return true;
        }
    }
    return false;
}

bool backtrack_sequential(vector<vector<int>>& board, long long& calls) {
    calls++;
    int r, c;
    if (!find_empty_sequential(board, r, c)) return true;

    vector<int> cands = get_candidates(board, r, c);
    for (int val : cands) {
        board[r][c] = val;
        if (backtrack_sequential(board, calls)) return true;
        board[r][c] = 0; // Hoàn tác
    }
    return false;
}

// ================= 2. HEURISTIC MRV =================
bool find_empty_mrv(const vector<vector<int>>& board, int& best_r, int& best_c, vector<int>& best_cands) {
    int min_cands = 10;
    bool found = false;

    for (int r = 0; r < N; r++) {
        for (int c = 0; c < N; c++) {
            if (board[r][c] == 0) {
                found = true;
                vector<int> cands = get_candidates(board, r, c);
                // Phát hiện ngõ cụt: ô trống không có giá trị hợp lệ
                if (cands.empty()) {
                    best_r = r;
                    best_c = c;
                    best_cands.clear();
                    return true;
                }
                if ((int)cands.size() < min_cands) {
                    min_cands = cands.size();
                    best_r = r;
                    best_c = c;
                    best_cands = cands;
                    if (min_cands == 1) return true;
                }
            }
        }
    }
    return found;
}

bool backtrack_mrv(vector<vector<int>>& board, long long& calls) {
    calls++;
    int r, c;
    vector<int> cands;
    if (!find_empty_mrv(board, r, c, cands)) return true;
    if (cands.empty()) return false;

    for (int val : cands) {
        board[r][c] = val;
        if (backtrack_mrv(board, calls)) return true;
        board[r][c] = 0; // Hoàn tác
    }
    return false;
}

int main() {
    vector<vector<int>> grid_input = {
        {5, 3, 0, 0, 7, 0, 0, 0, 0},
        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        {0, 9, 8, 0, 0, 0, 0, 6, 0},
        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        {7, 0, 0, 0, 2, 0, 0, 0, 6},
        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        {0, 0, 0, 0, 8, 0, 0, 7, 9}
    };

    // 1. Quét tuần tự
    auto board_seq = grid_input;
    long long calls_seq = 0;
    auto start_seq = high_resolution_clock::now();
    backtrack_sequential(board_seq, calls_seq);
    auto end_seq = high_resolution_clock::now();
    double time_seq = duration<double, milli>(end_seq - start_seq).count();

    // 2. MRV
    auto board_mrv = grid_input;
    long long calls_mrv = 0;
    auto start_mrv = high_resolution_clock::now();
    backtrack_mrv(board_mrv, calls_mrv);
    auto end_mrv = high_resolution_clock::now();
    double time_mrv = duration<double, milli>(end_mrv - start_mrv).count();

    // Kiểm tra tính đồng nhất của lời giải
    bool same_solution = (board_seq == board_mrv);

    cout << "=======================================================\n";
    cout << left << setw(26) << "Dai luong" << "| " 
         << setw(14) << "Quet tuan tu" << "| " 
         << setw(14) << "MRV" << "\n";
    cout << "-------------------------------------------------------\n";
    cout << left << setw(26) << "So loi goi ham de quy" << "| " 
         << setw(14) << calls_seq << "| " 
         << setw(14) << calls_mrv << "\n";
    cout << left << setw(26) << "Thoi gian chay" << "| " 
         << fixed << setprecision(2) << setw(11) << time_seq << " ms| " 
         << setw(11) << time_mrv << " ms\n";
    cout << left << setw(26) << "Loi giai tim duoc" << "| " 
         << (same_solution ? "Giong nhau" : "Khac nhau") << "\n";
    cout << "=======================================================\n";

    return 0;
}
