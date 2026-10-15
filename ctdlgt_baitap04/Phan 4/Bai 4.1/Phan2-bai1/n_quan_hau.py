def giai_n_quan_hau(n):
    x = [0] * n  # x[i] lưu chỉ số cột (0..n-1) của quân hậu ở hàng i
    cot = [False] * n
    cheo1 = [False] * (2 * n)  # đường chéo chính: i + j
    cheo2 = [False] * (2 * n)  # đường chéo phụ: i - j + n

    so_loi_giai = 0
    so_nut = 0
    loi_giai_dau = None

    def dat_hau(i):
        nonlocal so_loi_giai, so_nut, loi_giai_dau
        so_nut += 1  # Mỗi lần gọi hàm đệ quy tính là một nút

        if i == n:
            so_loi_giai += 1
            if loi_giai_dau is None:
                loi_giai_dau = x[:]  # Lưu lại lời giải đầu tiên
            return

        for j in range(n):
            if not cot[j] and not cheo1[i + j] and not cheo2[i - j + n]:
                x[i] = j
                cot[j] = cheo1[i + j] = cheo2[i - j + n] = True
                dat_hau(i + 1)
                cot[j] = cheo1[i + j] = cheo2[i - j + n] = False  # Hoàn tác

    dat_hau(0)

    print(f"Số nút đã duyệt: {so_nut}")
    print(f"Số lời giải: {so_loi_giai}")

    if loi_giai_dau is not None:
        print(f"Lời giải đầu tiên (dạng chỉ số 1..n): {[v + 1 for v in loi_giai_dau]}")
        print("Bàn cờ của lời giải đầu tiên (. là ô trống, Q là quân hậu):")
        for hang in range(n):
            cot_hau = loi_giai_dau[hang]
            dong = ["."] * n
            dong[cot_hau] = "Q"
            print(" ".join(dong))
    else:
        print("Không có lời giải nào.")

if __name__ == "__main__":
    n = int(input("Nhập n: "))
    giai_n_quan_hau(n)
