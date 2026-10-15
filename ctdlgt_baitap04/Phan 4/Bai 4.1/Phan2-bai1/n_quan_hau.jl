function giai_n_quan_hau(n)
    x = zeros(Int, n)             # x[i] là cột của quân hậu ở hàng i (1..n)
    cot = falses(n)               # cột đã bị chiếm
    cheo1 = falses(2n)            # đường chéo xuôi: i + j
    cheo2 = falses(2n)            # đường chéo ngược: i - j + n
    
    so_loi_giai = 0
    so_nut = 0
    loi_giai_dau = Int[]

    function dat_hau(i)
        so_nut += 1               # Mỗi lần gọi hàm đệ quy tính là một nút

        if i > n
            so_loi_giai += 1
            if isempty(loi_giai_dau)
                loi_giai_dau = copy(x)
            end
            return
        end

        for j in 1:n              # Julia đánh chỉ số từ 1
            if !cot[j] && !cheo1[i + j] && !cheo2[i - j + n]
                x[i] = j
                cot[j] = cheo1[i + j] = cheo2[i - j + n] = true
                dat_hau(i + 1)
                cot[j] = cheo1[i + j] = cheo2[i - j + n] = false  # Hoàn tác
            end
        end
    end

    dat_hau(1)                    # Lời gọi ban đầu từ hàng 1

    println("Số nút đã duyệt: ", so_nut)
    println("Số lời giải: ", so_loi_giai)

    if !isempty(loi_giai_dau)
        println("Lời giải đầu tiên: ", loi_giai_dau)
        println("Bàn cờ của lời giải đầu tiên (. là ô trống, Q là quân hậu):")
        for r in 1:n
            dong = fill(".", n)
            dong[loi_giai_dau[r]] = "Q"
            println(join(dong, " "))
        end
    else
        println("Không có lời giải nào.")
    end
end

print("Nhập n: ")
n = parse(Int, readline())
giai_n_quan_hau(n)
