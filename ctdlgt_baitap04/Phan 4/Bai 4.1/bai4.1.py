import sys

# Định nghĩa lớp Đồ vật
class DoVat:
    def __init__(self, ten, w, v):
        self.ten = ten
        self.w = w
        self.v = v
        self.don_gia = v / w

def tinh_can_tren(i, w_con_lai, v_hien_tai, danh_sach, n):
    """Tính cận trên theo bài toán cái túi phân số (Fractional Knapsack)"""
    can = v_hien_tai
    w_tam = w_con_lai
    for k in range(i, n):
        if danh_sach[k].w <= w_tam:
            w_tam -= danh_sach[k].w
            can += danh_sach[k].v
        else:
            # Lấy một phần phân số của vật k
            can += danh_sach[k].don_gia * w_tam
            break
    return can

def giai_cai_tui(danh_sach, W, co_cat_nhanh=True):
    n = len(danh_sach)
    so_nut = 0
    max_val = 0
    best_chon = [0] * n
    x = [0] * n

    def quay_lui(i, w_hien_tai, v_hien_tai):
        nonlocal so_nut, max_val, best_chon
        so_nut += 1

        # Cập nhật kỷ lục giá trị tốt nhất khi tìm thấy nghiệm hợp lệ
        if v_hien_tai > max_val:
            max_val = v_hien_tai
            best_chon = x[:]

        if i == n:
            return

        # Nhánh 1: CHỌN vật i (x[i] = 1) - ưu tiên xét trước vì đồ vật đã sắp theo v/w giảm dần
        if w_hien_tai + danh_sach[i].w <= W:
            x[i] = 1
            quay_lui(i + 1, w_hien_tai + danh_sach[i].w, v_hien_tai + danh_sach[i].v)
            x[i] = 0  # Hoàn tác

        # Nhánh 2: KHÔNG CHỌN vật i (x[i] = 0)
        x[i] = 0
        w_con_lai = W - w_hien_tai
        if co_cat_nhanh:
            # Tính cận trên: chỉ rẽ nhánh nếu tiềm năng lớn hơn kỷ lục hiện tại
            ub = tinh_can_tren(i + 1, w_con_lai, v_hien_tai, danh_sach, n)
            if ub > max_val:
                quay_lui(i + 1, w_hien_tai, v_hien_tai)
        else:
            # Không cắt nhánh: duyệt hết
            quay_lui(i + 1, w_hien_tai, v_hien_tai)

    quay_lui(0, 0, 0)
    return max_val, best_chon, so_nut

if __name__ == "__main__":
    # Sức chứa của túi
    W = 14

    # Bộ 6 đồ vật ở mục C của đề bài (có thể chỉnh sửa trọng lượng w và giá trị v nếu cần)
    # Định dạng: DoVat(Tên, Khối lượng w, Giá trị v)
    ds_goc = [
        DoVat("A", 4, 12),
        DoVat("B", 7, 25),
        DoVat("C", 3, 7),
        DoVat("D", 3, 8),
        DoVat("E", 3, 9),
        DoVat("F", 10, 21)
    ]

    # BẮT BUỘC: Sắp xếp danh sách đồ vật theo tỉ số v/w giảm dần
    ds_sap_xep = sorted(ds_goc, key=lambda item: item.don_gia, reverse=True)

    print("=== THỨ TỰ ĐỒ VẬT SAU KHI SẮP XẾP THEO v/w GIẢM DẦN ===")
    for idx, item in enumerate(ds_sap_xep):
        print(f"{idx+1}. Vật {item.ten}: w = {item.w}, v = {item.v}, v/w = {item.don_gia:.3f}")

    # Chạy chế độ 1: CÓ cắt nhánh
    max_val_cat, chon_cat, nut_cat = giai_cai_tui(ds_sap_xep, W, co_cat_nhanh=True)

    # Chạy chế độ 2: KHÔNG cắt nhánh
    max_val_khong, chon_khong, nut_khong = giai_cai_tui(ds_sap_xep, W, co_cat_nhanh=False)

    print("\n" + "="*50)
    print(f"Sức chứa W = {W}")
    print(f"Giá trị lớn nhất: {max_val_cat}")
    tap_vat = [ds_sap_xep[i].ten for i in range(len(ds_sap_xep)) if chon_cat[i] == 1]
    print(f"Tập đồ vật được chọn: {tap_vat} (Tổng w = {sum(ds_sap_xep[i].w for i in range(len(ds_sap_xep)) if chon_cat[i] == 1)})")
    print(f"Số nút khi CÓ cắt nhánh: {nut_cat}")
    print(f"Số nút khi KHÔNG cắt nhánh: {nut_khong}")
    print(f"Số nút giảm được: {nut_khong / nut_cat:.2f} lần")
