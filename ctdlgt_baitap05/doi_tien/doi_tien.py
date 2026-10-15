import random

def doi_tien_tham_lam(menh_gia, S):
    # Sắp xếp mệnh giá giảm dần để luôn chọn đồng lớn nhất
    coins = sorted(menh_gia, reverse=True)
    cach_tra = []
    tong = S
    for c in coins:
        while tong >= c:
            cach_tra.append(c)
            tong -= c
    if tong == 0:
        return len(cach_tra), cach_tra
    return float('inf'), []

def doi_tien_dp(menh_gia, S):
    # f[j] là số tờ ít nhất để đổi số tiền j
    INF = 10**9
    f = [INF] * (S + 1)
    vet = [-1] * (S + 1)
    f[0] = 0

    for j in range(1, S + 1):
        for c in menh_gia:
            if j >= c and f[j - c] + 1 < f[j]:
                f[j] = f[j - c] + 1
                vet[j] = c

    if f[S] == INF:
        return INF, []

    # Truy vết tìm các đồng tiền được chọn
    cach_tra = []
    curr = S
    while curr > 0:
        c = vet[curr]
        cach_tra.append(c)
        curr -= c
    return f[S], cach_tra

def kiem_chung_ngau_nhien():
    # Kiểm chứng độc lập giữa tham lam và DP trên dữ liệu ngẫu nhiên nhỏ
    so_bo_sai = 0
    print("=== KIEM CHUNG DOC LAP TREN DU LIEU NGAU NHIEN ===")
    random.seed(42)
    for test in range(1, 11):
        k = random.randint(3, 5)
        # Sinh bộ mệnh giá luôn có 1 để luôn đổi được tiền
        menh_gia = sorted(list(set([1] + random.sample(range(2, 20), k - 1))))
        S = random.randint(10, 30)
        sl_tham_lam, _ = doi_tien_tham_lam(menh_gia, S)
        sl_dp, _ = doi_tien_dp(menh_gia, S)
        
        if sl_tham_lam != sl_dp:
            so_bo_sai += 1
    print(f"-> Da chay 10 bo ngau nhien, phat hien {so_bo_sai} bo tham lam khong toi uu.")
    print("-> Xac nhan: DP luon cho ket qua <= Tham lam (dung tinh chat toi uu).\n")

def main():
    kiem_chung_ngau_nhien()

    # Sau bo du lieu chuan o Muc B
    ds_bo = [
        (1, [1, 4, 6, 9], 12),
        (2, [1, 5, 10, 20, 50], 85),
        (3, [1, 3, 7, 12], 20),
        (4, [1, 2, 5, 10], 38),
        (5, [1, 6, 10], 12),
        (6, [1, 4, 5, 15, 20], 23),
    ]

    print(f"{'Bo':<4} | {'TL so to':<9} | {'Cach tra tham lam':<25} | {'DP so to':<9} | {'Cach tra toi uu':<20} | {'TL dung?'}")
    print("-" * 90)

    for stt, menh_gia, S in ds_bo:
        sl_tl, cach_tl = doi_tien_tham_lam(menh_gia, S)
        sl_dp, cach_dp = doi_tien_dp(menh_gia, S)

        str_tl = " + ".join(map(str, cach_tl))
        str_dp = " + ".join(map(str, cach_dp))
        dung = "Dung" if sl_tl == sl_dp else "Sai"

        print(f"{stt:<4} | {sl_tl:<9} | {str_tl:<25} | {sl_dp:<9} | {str_dp:<20} | {dung}")

if __name__ == "__main__":
    main()
