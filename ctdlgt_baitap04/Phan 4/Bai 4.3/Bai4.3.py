import time
import copy

def get_candidates(board, r, c):
    """Tìm tập hợp các số từ 1 đến 9 có thể điền hợp lệ vào ô (r, c)."""
    used = set(board[r]) # Hàng
    for i in range(9):   # Cột
        used.add(board[i][c])
    # Khối 3x3
    br, bc = (r // 3) * 3, (c // 3) * 3
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            used.add(board[i][j])
    return [num for num in range(1, 10) if num not in used]

# 1. Chiến lược Quét tuần tự
def find_empty_sequential(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None, None

def solve_sequential(board):
    call_count = 0

    def backtrack():
        nonlocal call_count
        call_count += 1
        
        r, c = find_empty_sequential(board)
        if r is None:
            return True # Đã điền kín bảng thành công
        
        for val in get_candidates(board, r, c):
            board[r][c] = val
            if backtrack():
                return True
            board[r][c] = 0 # Hoàn tác
        return False

    t_start = time.perf_counter()
    backtrack()
    t_end = time.perf_counter()
    return board, call_count, (t_end - t_start) * 1000

# 2. Chiến lược Heuristic MRV (Minimum Remaining Values)
def find_empty_mrv(board):
    min_candidates = 10
    best_r, best_c = None, None
    best_cands = []

    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                cands = get_candidates(board, r, c)
                # Phát hiện ngõ cụt ngay lập tức (ô trống không có giá trị hợp lệ nào)
                if len(cands) == 0:
                    return r, c, []
                if len(cands) < min_candidates:
                    min_candidates = len(cands)
                    best_r, best_c = r, c
                    best_cands = cands
                    if min_candidates == 1:
                        return best_r, best_c, best_cands
    return best_r, best_c, best_cands

def solve_mrv(board):
    call_count = 0

    def backtrack():
        nonlocal call_count
        call_count += 1

        r, c, cands = find_empty_mrv(board)
        if r is None:
            return True
        if not cands:
            return False

        for val in cands:
            board[r][c] = val
            if backtrack():
                return True
            board[r][c] = 0 # Hoàn tác
        return False

    t_start = time.perf_counter()
    backtrack()
    t_end = time.perf_counter()
    return board, call_count, (t_end - t_start) * 1000

if __name__ == "__main__":
    # Đề Sudoku 56 ô trống ở mục E (0 là ô trống)
    # Bạn chỉ cần dán ma trận 9x9 ở mục E của đề bài vào đây:
    grid_input = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    board_seq = copy.deepcopy(grid_input)
    sol_seq, calls_seq, t_seq = solve_sequential(board_seq)

    board_mrv = copy.deepcopy(grid_input)
    sol_mrv, calls_mrv, t_mrv = solve_mrv(board_mrv)

    print("=" * 45)
    print(f"{'Đại lượng':<25} | {'Quét tuần tự':<12} | {'MRV':<12}")
    print("-" * 55)
    print(f"{'Số lời gọi hàm đệ quy':<25} | {calls_seq:<12} | {calls_mrv:<12}")
    print(f"{'Thời gian chạy':<25} | {t_seq:<9.2f} ms | {t_mrv:<9.2f} ms")
    print(f"{'Lời giải tìm được':<25} | {'Giống nhau' if sol_seq == sol_mrv else 'Khác nhau'}")
    print("=" * 45)
