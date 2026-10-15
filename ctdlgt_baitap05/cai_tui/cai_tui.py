def cai_tui(w, v, W, ten_do_vat=None):
    n = len(w)
    # Khởi tạo bảng f kích thước (n + 1) x (W + 1) toàn số 0
    f = [[0] * (W + 1) for _ in range(n + 1)]

    # Điền bảng theo công thức quy hoạch động
    for i in range(1, n + 1):
        for j in range(W + 1):
            f[i][j] = f[i - 1][j]  # Không lấy đồ vật i
            if w[i - 1] <= j:      # Nếu túi còn đủ chỗ, thử lấy đồ vật i
                f[i][j] = max(f[i][j], f[i - 1][j - w[i - 1]] + v[i - 1])

    # Truy vết tìm tập đồ vật được chọn từ ô f[n][W]
    chon = []
    j = W
    for i in range(n, 0, -1):
        if f[i][j] != f[i - 1][j]:  # Khác nhau => đồ vật i đã được lấy
            chon.append(i)
            j -= w[i - 1]           # Trừ đi sức chứa mà đồ vật i đã chiếm

    chon.reverse()  # Đảo lại để có thứ tự tăng dần từ 1 đến n
    return f, f[n][W], chon


def main():
    # Bộ dữ liệu chuẩn mục A
    n = 5
    W = 11
    ten = ["A", "B", "C", "D", "E"]
    w = [2, 3, 4, 5, 7]
    v = [3, 7, 9, 12, 16]

    f, max_val, chon = cai_tui(w, v, W, ten)

    # 1. In toàn bộ bảng f (6 hàng x 12 cột)
    print("=== BANG QUY HOACH DONG f[i][j] ===")
    header = f"{'f[i][j]':<10}" + "".join(f"{j:>4}" for j in range(W + 1))
    print(header)
    print("-" * len(header))

    for i in range(n + 1):
        nhan = "i=0" if i == 0 else f"i={i} ({ten[i - 1]})"
        row_str = f"{nhan:<10}" + "".join(f"{f[i][j]:>4}" for j in range(W + 1))
        print(row_str)

    print("-" * len(header))

    # 2. In giá trị lớn nhất
    print(f"\nGia tri lon nhat f[{n}][{W}] = {max_val}")

    # 3. In tập đồ vật được chọn sau khi truy vết
    ten_duoc_chon = [ten[i - 1] for i in chon]
    tong_w = sum(w[i - 1] for i in chon)
    print(f"Tap do vat duoc chon: {ten_duoc_chon} (cac chi so: {chon})")
    print(f"Tong trong luong: {tong_w}/{W}")
    print(f"Tong gia tri: {sum(v[i - 1] for i in chon)}")


if __name__ == "__main__":
    main()
