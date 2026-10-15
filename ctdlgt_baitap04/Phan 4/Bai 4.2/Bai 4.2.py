import sys

def giai_tsp(cost_matrix, co_cat_nhanh=True):
    n = len(cost_matrix)
    
    # Tìm cạnh rẻ nhất toàn ma trận (không xét đường chéo chính i == j)
    c_min = float('inf')
    for i in range(n):
        for j in range(n):
            if i != j:
                c_min = min(c_min, cost_matrix[i][j])

    visited = [False] * n
    visited[0] = True  # Xuất phát từ thành phố 0
    path = [0] * (n + 1)
    path[0] = 0
    
    best_cost = float('inf')
    best_path = []
    so_nut = 0

    # k: số đỉnh đã đi qua (0..n-1), curr_city: đỉnh hiện tại, curr_cost: chi phí đã đi
    def quay_lui(k, curr_city, curr_cost):
        nonlocal so_nut, best_cost, best_path
        so_nut += 1

        # Đã đi qua đủ n đỉnh (từ 0 đến n-1), khép góc về đỉnh 0
        if k == n - 1:
            canh_ve = cost_matrix[curr_city][0]
            tong_chi_phi = curr_cost + canh_ve
            if tong_chi_phi < best_cost:
                best_cost = tong_chi_phi
                path[n] = 0
                best_path = path[:]
            return

        for next_city in range(n):
            if not visited[next_city]:
                cost_edge = cost_matrix[curr_city][next_city]
                next_cost = curr_cost + cost_edge
                
                # Số cạnh còn phải đi: (n - 1 - k) cạnh tới đỉnh chưa thăm + 1 cạnh về 0 = n - (k + 1) + 1 = n - k
                so_canh_con_lai = n - (k + 1)
                can_duoi = next_cost + so_canh_con_lai * c_min

                if co_cat_nhanh:
                    # Chỉ đi tiếp nếu cận dưới có tiềm năng nhỏ hơn kỷ lục hiện tại
                    if can_duoi < best_cost:
                        visited[next_city] = True
                        path[k + 1] = next_city
                        quay_lui(k + 1, next_city, next_cost)
                        visited[next_city] = False # Hoàn tác
                else:
                    # Không cắt nhánh: duyệt vét cạn
                    visited[next_city] = True
                    path[k + 1] = next_city
                    quay_lui(k + 1, next_city, next_cost)
                    visited[next_city] = False # Hoàn tác

    quay_lui(0, 0, 0)
    return c_min, best_cost, best_path, so_nut

if __name__ == "__main__":
    # Ma trận chi phí 5 thành phố ở mục D (thay đổi số liệu tại đây nếu có bảng riêng)
    cost_matrix = [
        [0,  10, 25, 25, 10],
        [1,  0,  10, 15, 2],
        [8,  9,  0,  20, 10],
        [14, 10, 24, 0,  15],
        [10, 8,  25, 27, 0]
    ]

    # 1. Chạy CÓ cắt nhánh
    c_min, best_cost_cat, best_path_cat, nut_cat = giai_tsp(cost_matrix, co_cat_nhanh=True)
    
    # 2. Chạy KHÔNG cắt nhánh
    _, best_cost_khong, _, nut_khong = giai_tsp(cost_matrix, co_cat_nhanh=False)

    print(f"Cạnh rẻ nhất toàn ma trận c_min: {c_min}")
    print(f"Chi phí hành trình tối ưu: {best_cost_cat}")
    print(f"Hành trình tối ưu: {' -> '.join(map(str, best_path_cat))}")
    print(f"Số nút khi CÓ cắt nhánh: {nut_cat}")
    print(f"Số nút khi KHÔNG cắt nhánh: {nut_khong}")
