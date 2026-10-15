# ==============================================================================
# BÀI TOÁN ĐỔI TIỀN: THAM LAM SO VỚI QUY HOẠCH ĐỘNG (doi_tien.jl)
#
# QUY ƯỚC CHỈ SỐ TRONG BẢN JULIA:
# - Mảng trong Julia đánh chỉ số từ 1.
# - Mảng quy hoạch động f lưu số tờ ít nhất để đổi số tiền j (0 <= j <= S)
#   được ánh xạ thành: f[j + 1] với kích thước mảng là (S + 1).
# - Trạng thái f[0] = 0 ứng với f[1] = 0 trong Julia.
# ==============================================================================

using Printf
using Random

const INF = 1_000_000_000

# Thuật toán Tham lam: Luôn chọn đồng có mệnh giá lớn nhất có thể
function doi_tien_tham_lam(menh_gia::Vector{Int}, S::Int)
    coins = sort(menh_gia, rev=true)
    cach_tra = Int[]
    tong = S

    for c in coins
        while tong >= c
            push!(cach_tra, c)
            tong -= c
        end
    end

    if tong == 0
        return length(cach_tra), cach_tra
    end
    return INF, Int[]
end

# Thuật toán Quy hoạch động: Tìm số tờ ít nhất thật sự
function doi_tien_dp(menh_gia::Vector{Int}, S::Int)
    # f[j + 1] lưu số tờ ít nhất để đổi số tiền j
    f = fill(INF, S + 1)
    vet = fill(-1, S + 1)
    f[1] = 0 # Ứng với f[0] = 0

    for j in 1:S
        for c in menh_gia
            if j >= c && f[j - c + 1] + 1 < f[j + 1]
                f[j + 1] = f[j - c + 1] + 1
                vet[j + 1] = c
            end
        end
    end

    if f[S + 1] == INF
        return INF, Int[]
    end

    # Truy vết tìm các đồng tiền được chọn
    cach_tra = Int[]
    curr = S
    while curr > 0
        c = vet[curr + 1]
        push!(cach_tra, c)
        curr -= c
    end

    return f[S + 1], cach_tra
end

# Kiểm chứng độc lập giữa Tham lam và Quy hoạch động trên dữ liệu ngẫu nhiên
function kiem_chung_ngau_nhien()
    println("=== KIEM CHUNG DOC LAP TREN DU LIEU NGAU NHIEN ===")
    Random.seed!(42)
    so_bo_sai = 0

    for test in 1:10
        k = rand(3:5)
        # Sinh bộ mệnh giá luôn có đồng 1 để luôn đổi được tiền
        pool = collect(2:20)
        shuffle!(pool)
        menh_gia = sort(unique(vcat([1], pool[1:k-1])))

        S = rand(10:30)
        sl_tl, _ = doi_tien_tham_lam(menh_gia, S)
        sl_dp, _ = doi_tien_dp(menh_gia, S)

        if sl_tl != sl_dp
            so_bo_sai += 1
        end
    end

    println("-> Da chay 10 bo ngau nhien, phat hien $so_bo_sai bo tham lam khong toi uu.")
    println("-> Xac nhan: DP luon cho ket qua <= Tham lam (dung tinh chat toi uu).\n")
end

function main()
    kiem_chung_ngau_nhien()

    # Sáu bộ dữ liệu chuẩn ở Mục B
    ds_bo = [
        (1, [1, 4, 6, 9], 12),
        (2, [1, 5, 10, 20, 50], 85),
        (3, [1, 3, 7, 12], 20),
        (4, [1, 2, 5, 10], 38),
        (5, [1, 6, 10], 12),
        (6, [1, 4, 5, 15, 20], 23)
    ]

    @printf("%-4s | %-9s | %-25s | %-9s | %-20s | %s\n", 
            "Bo", "TL so to", "Cach tra tham lam", "DP so to", "Cach tra toi uu", "TL dung?")
    println(repeat("-", 90))

    for (stt, menh_gia, S) in ds_bo
        sl_tl, cach_tl = doi_tien_tham_lam(menh_gia, S)
        sl_dp, cach_dp = doi_tien_dp(menh_gia, S)

        str_tl = join(string.(cach_tl), " + ")
        str_dp = join(string.(cach_dp), " + ")
        dung = (sl_tl == sl_dp) ? "Dung" : "Sai"

        @printf("%-4d | %-9d | %-25s | %-9d | %-20s | %s\n", 
                stt, sl_tl, str_tl, sl_dp, str_dp, dung)
    end
end

main()
