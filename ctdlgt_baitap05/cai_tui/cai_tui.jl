# ==============================================================================
# BÀI TOÁN CÁI TÚI 0/1 BẰNG QUY HOẠCH ĐỘNG (cai_tui.jl)
#
# QUY ƯỚC CHỈ SỐ TRONG BẢN JULIA:
# - Mảng và ma trận trong Julia đánh chỉ số từ 1.
# - Bảng quy hoạch động toán học f có hàng 0..n và cột 0..W.
# - Do đó, trạng thái f[i][j] với i in 0..n và j in 0..W được ánh xạ thành:
#       f[i + 1, j + 1] trong ma trận Julia kích thước (n + 1) x (W + 1).
# ==============================================================================

using Printf

function cai_tui(w::Vector{Int}, v::Vector{Int}, W::Int)
    n = length(w)
    # Bảng f kích thước (n + 1) hàng x (W + 1) cột, khởi tạo toàn bộ 0
    f = zeros(Int, n + 1, W + 1)

    # Điền bảng quy hoạch động
    for i in 1:n
        for j in 0:W
            # Không lấy đồ vật i (ánh xạ i-1 -> i, j -> j+1)
            f[i + 1, j + 1] = f[i, j + 1]
            
            # Thử lấy đồ vật i nếu sức chứa j còn đủ
            if w[i] <= j
                f[i + 1, j + 1] = max(f[i + 1, j + 1], f[i, j - w[i] + 1] + v[i])
            end
        end
    end

    # Truy vết từ ô góc dưới bên phải f[n + 1, W + 1]
    chon = Int[]
    j = W
    for i in n:-1:1
        # Nếu f[i+1, j+1] khác f[i, j+1] thì đồ vật i đã được chọn
        if f[i + 1, j + 1] != f[i, j + 1]
            push!(chon, i)
            j -= w[i] # Trừ phần sức chứa đã chiếm
        end
    end

    reverse!(chon) # Đảo lại theo thứ tự tăng dần từ 1 đến n
    return f, f[n + 1, W + 1], chon
end

function main()
    # Bộ dữ liệu chuẩn mục A
    n = 5
    W = 11
    ten = ["A", "B", "C", "D", "E"]
    w = [2, 3, 4, 5, 7]
    v = [3, 7, 9, 12, 16]

    f, max_val, chon = cai_tui(w, v, W)

    # 1. In toàn bộ bảng f (6 hàng x 12 cột = 72 ô)
    println("=== BANG QUY HOACH DONG f[i][j] ===")
    @printf("%-10s", "f[i][j]")
    for j in 0:W
        @printf("%4d", j)
    end
    println()
    println(repeat("-", 10 + 4 * (W + 1)))

    for i in 0:n
        nhan = i == 0 ? "i=0" : "i=$(i) ($(ten[i]))"
        @printf("%-10s", nhan)
        for j in 0:W
            @printf("%4d", f[i + 1, j + 1])
        end
        println()
    end
    println(repeat("-", 10 + 4 * (W + 1)))

    # 2. In giá trị lớn nhất
    println("\nGia tri lon nhat f[$n][$W] = $max_val")

    # 3. In tập đồ vật được chọn sau khi truy vết
    ten_duoc_chon = [ten[i] for i in chon]
    tong_w = sum(w[i] for i in chon)
    tong_v = sum(v[i] for i in chon)
    
    # Định dạng hiển thị mảng tên đồ vật theo chuẩn Python/C++
    str_ten = "[" * join(["'" * t * "'" for t in ten_duoc_chon], ", ") * "]"
    str_chi_so = "[" * join(chon, ", ") * "]"
    
    println("Tap do vat duoc chon: $str_ten (cac chi so: $str_chi_so)")
    println("Tong trong luong: $tong_w/$W")
    println("Tong gia tri: $tong_v")
end

main()
