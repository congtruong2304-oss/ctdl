# Chon hoat dong (tham lam): sap xep theo tieu chi roi quet, chon neu khong chong lan.
# 7 hoat dong ca 4 va hoat dong them (2, 5) o cuoi
HD = [(1, 7), (2, 7), (4, 6), (6, 12), (8, 13), (11, 14), (12, 16), (2, 5)]

def khoa(hd, tieu_chi):
    s, f = hd
    if tieu_chi == 1: return f        # ket thuc som nhat
    if tieu_chi == 2: return s        # bat dau som nhat
    return f - s                      # ngan nhat

def tuong_thich(hd, da_chon):
    s, f = hd
    for (s2, f2) in da_chon:
        if s < f2 and s2 < f:         # hai khoang thoi gian chong len nhau
            return False
    return True

def chon_hoat_dong(tieu_chi):
    thu_tu = sorted(HD, key=lambda hd: khoa(hd, tieu_chi))  # buoc sap xep
    da_chon = []
    for hd in thu_tu:
        if tuong_thich(hd, da_chon):
            da_chon.append(hd)
            print("Xet", hd, "-> CHON")
        else:
            print("Xet", hd, "-> bo, chong lan voi hoat dong da chon")
    return da_chon

def main():
    print("MSSV: N24DCDT102 | Ma ca: 4")
    print("Nhap tieu chi (1: ket thuc som nhat, 2: bat dau som nhat, 3: ngan nhat):")
    try:
        tieu_chi = int(input().strip())
    except (ValueError, EOFError):
        print("Du lieu khong hop le.")
        return
    if tieu_chi not in (1, 2, 3):
        print("Du lieu khong hop le.")
        return
    da_chon = chon_hoat_dong(tieu_chi)
    print("Cac hoat dong duoc chon:", " ".join(f"({s},{f})" for s, f in da_chon))
    print("Tong thoi gian su dung:", sum(f - s for s, f in da_chon))
    print("So hoat dong duoc chon:", len(da_chon))

if __name__ == "__main__":
    main()
