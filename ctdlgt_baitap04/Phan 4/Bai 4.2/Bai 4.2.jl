function giai_tsp(cost_matrix; co_cat_nhanh=true)
    n = size(cost_matrix, 1)

    # 1. Tìm cạnh rẻ nhất toàn ma trận (bỏ qua đường chéo chính i == j)
    c_min = typemax(Int)
    for i in 1:n
        for j in 1:n
            if i != j
                c_min = min(c_min, cost_matrix[i, j])
            end
        end
    end

    visited = falses(n)
    visited[1] = true  # Xuất phát từ đỉnh 1 (tương ứng thành phố 0)
    path = zeros(Int, n + 1)
    path[1] = 1

    best_cost = typemax(Int)
    best_path = zeros(Int, n + 1)
    so_nut = 0

    # k: số đỉnh đã đi qua (1..n), curr_city: đỉnh hiện tại (1..n), curr_cost: chi phí đã tích lũy
    function quay_lui(k, curr_city, curr_cost)
        so_nut += 1

        # Đã đi qua đủ n đỉnh, khép góc quay về đỉnh xuất phát (đỉnh 1)
        if k == n
            canh_ve = cost_matrix[curr_city, 1]
            tong_chi_phi = curr_cost + canh_ve
            if tong_chi_phi < best_cost
                best_cost = tong_chi_phi
                path[n + 1] = 1
                best_path = copy(path)
            end
            return
        end

        for next_city in 1:n
            if !visited[next_city]
                cost_edge = cost_matrix[curr_city, next_city]
                next_cost = curr_cost + cost_edge

                # Số cạnh còn lại phải đi: (n - k) cạnh nối các đỉnh còn lại + 1 cạnh về đỉnh 1 = (n - k)
                so_canh_con_lai = n - k
                can_duoi = next_cost + so_canh_con_lai * c_min

                if co_cat_nhanh
                    # Cắt nhánh: chỉ đi tiếp nếu cận dưới nhỏ hơn kỷ lục hiện tại
                    if can_duoi < best_cost
                        visited[next_city] = true
                        path[k + 1] = next_city
                        quay_lui(k + 1, next_city, next_cost)
                        visited[next_city] = false  # Hoàn tác
                    end
                else
                    # Không cắt nhánh: duyệt vét cạn
                    visited[next_city] = true
                    path[k + 1] = next_city
                    quay_lui(k + 1, next_city, next_cost)
                    visited[next_city] = false  # Hoàn tác
                end
            end
        end
    end

    quay_lui(1, 1, 0)
    return c_min, best_cost, best_path, so_nut
end

function main()
    # Ma trận chi phí 5x5 ở mục D (chỉ số Julia 1..5)
    cost_matrix = [
         0  10  25  25  10;
         1   0  10  15   2;
         8   9   0  20  10;
        14  10  24   0  15;
        10   8  25  27   0
    ]

    # 1. Chạy CÓ cắt nhánh
    c_min, best_cost_cat, best_path_cat, nut_cat = giai_tsp(cost_matrix, co_cat_nhanh=true)

    # 2. Chạy KHÔNG cắt nhánh
    _, _, _, nut_khong = giai_tsp(cost_matrix, co_cat_nhanh=false)

    println("Canh re nhat toan ma tran c_min: ", c_min)
    println("Chi phi hanh trinh toi uu: ", best_cost_cat)

    # Hiển thị hành trình theo định dạng đỉnh 0..4 để khớp với đề bài
    hanh_trinh_hien_thi = [x - 1 for x in best_path_cat]
    println("Hanh trinh toi uu: ", join(hanh_trinh_hien_thi, " -> "))
    println("So nut khi CO cat nhanh: ", nut_cat)
    println("So nut khi KHONG cat nhanh: ", nut_khong)
end

main()
