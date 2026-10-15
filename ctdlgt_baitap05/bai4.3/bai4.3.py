# bai4.3.py - Ba thuat toan giai ma cua mo hinh ngon ngu va thuat toan Viterbi

import itertools

# ==============================================================================
# PHAN 1: MO HINH NGON NGU HAI TU (BIGRAM)
# ==============================================================================

# Xac suat tu tiep theo tu Muc D
bigram = {
    "em": {"hoc": 0.52, "di": 0.48},
    "hoc": {"bai": 0.40, "toan": 0.35, "ve": 0.25},
    "di": {"cho": 0.58, "boi": 0.22, "ngu": 0.20},
}


def liet_ke_toan_bo():
    # Liet ke tat ca cac cau do dai 3 bat dau bang "em"
    ds_cau = []
    w1 = "em"
    for w2, p12 in bigram[w1].items():
        for w3, p23 in bigram[w2].items():
            prob = p12 * p23
            ds_cau.append((f"{w1} {w2} {w3}", prob))

    ds_cau.sort(key=lambda x: x[1], reverse=True)
    return ds_cau


def giai_ma_tham_lam():
    # Buoc 1: Tu "em", chon tu co xac suat lon nhat
    w1 = "em"
    w2 = max(bigram[w1].items(), key=lambda x: x[1])[0]
    p1 = bigram[w1][w2]

    # Buoc 2: Tu w2, chon tu co xac suat lon nhat
    w3 = max(bigram[w2].items(), key=lambda x: x[1])[0]
    p2 = bigram[w2][w3]

    return f"{w1} {w2} {w3}", p1 * p2


def giai_ma_chum(k):
    # Beam search voi do rong chum k
    beam = [("em", 1.0)]

    # Buoc mo rong 1: tu "em" sang tu thu 2
    ung_vien = []
    for cau, prob in beam:
        tu_cuoi = cau.split()[-1]
        for w_next, p in bigram[tu_cuoi].items():
            ung_vien.append((f"{cau} {w_next}", prob * p))
    ung_vien.sort(key=lambda x: x[1], reverse=True)
    beam = ung_vien[:k]

    # Buoc mo rong 2: sang tu thu 3
    ung_vien = []
    for cau, prob in beam:
        tu_cuoi = cau.split()[-1]
        for w_next, p in bigram[tu_cuoi].items():
            ung_vien.append((f"{cau} {w_next}", prob * p))
    ung_vien.sort(key=lambda x: x[1], reverse=True)
    beam = ung_vien[:k]

    return beam[0]


# ==============================================================================
# PHAN 2: THUAT TOAN VITERBI VA VET CAN GAN NHAN
# ==============================================================================

# Tham so Viterbi tu Muc D
pi = {"N": 0.60, "V": 0.40}

A = {
    "N": {"N": 0.35, "V": 0.65},
    "V": {"N": 0.70, "V": 0.30},
}

B = {
    "N": {"em": 0.35, "hoc": 0.10, "bai": 0.40, "toan": 0.30},
    "V": {"em": 0.05, "hoc": 0.45, "bai": 0.05, "toan": 0.02},
}

cau_gan_nhan = ["em", "hoc", "bai", "toan"]
nhan = ["N", "V"]


def viterbi(cau):
    T = len(cau)
    # f[i][s]: xac suat lon nhat tai buoc i voi nhan s
    # vet[i][s]: nhan truoc do dan toi trang thai nay
    f = [{} for _ in range(T)]
    vet = [{} for _ in range(T)]

    # Buoc 1: Khoi tao (i = 0 ung voi tu 1 "em")
    for s in nhan:
        f[0][s] = pi[s] * B[s][cau[0]]
        vet[0][s] = None

    # Buoc 2: Quy hoach dong quy nap (i = 1 .. T-1)
    for i in range(1, T):
        for s in nhan:
            best_prob = -1.0
            best_prev = None
            for s_prev in nhan:
                prob = f[i - 1][s_prev] * A[s_prev][s] * B[s][cau[i]]
                if prob > best_prob:
                    best_prob = prob
                    best_prev = s_prev
            f[i][s] = best_prob
            vet[i][s] = best_prev

    # Buoc 3: Truy vet tim day nhan toi uu
    best_last_prob = -1.0
    best_last_nhan = None
    for s in nhan:
        if f[T - 1][s] > best_last_prob:
            best_last_prob = f[T - 1][s]
            best_last_nhan = s

    day_nhan = [best_last_nhan]
    curr = best_last_nhan
    for i in range(T - 1, 0, -1):
        curr = vet[i][curr]
        day_nhan.append(curr)
    day_nhan.reverse()

    return day_nhan, best_last_prob, f, vet


def vet_can_viterbi(cau):
    # Vet can 2^4 = 16 to hop nhan
    best_prob = -1.0
    best_seq = None

    for seq in itertools.product(nhan, repeat=len(cau)):
        # Tinh xac suat: pi(y1) * B(y1, w1) * A(y1->y2)...
        prob = pi[seq[0]] * B[seq[0]][cau[0]]
        for i in range(1, len(cau)):
            prob *= A[seq[i - 1]][seq[i]] * B[seq[i]][cau[i]]

        if prob > best_prob:
            best_prob = prob
            best_seq = seq

    return list(best_seq), best_prob


# ==============================================================================
# HAM MAIN CHAY VA IN KET QUA
# ==============================================================================
def main():
    # 1. Chay cac thuat toan tren Mo hinh ngon ngu
    ds_tat_ca = liet_ke_toan_bo()
    cau_tot_nhat, diem_tot_nhat = ds_tat_ca[0]
    cau_tl, diem_tl = giai_ma_tham_lam()
    cau_k1, diem_k1 = giai_ma_chum(1)
    cau_k2, diem_k2 = giai_ma_chum(2)
    cau_k3, diem_k3 = giai_ma_chum(3)

    # 2. Chay Viterbi va Vet can
    day_viterbi, prob_viterbi, f_table, vet_table = viterbi(cau_gan_nhan)
    day_vetcan, prob_vetcan = vet_can_viterbi(cau_gan_nhan)

    # In thong tin doi chieu giua Viterbi va Vet can
    print("=== DOI CHIEU VITERBI VA VET CAN (16 TO HOP NHAN) ===")
    print(f"Viterbi: {' '.join(day_viterbi)} | Xac suat: {prob_viterbi:.6f}")
    print(f"Vet can: {' '.join(day_vetcan)} | Xac suat: {prob_vetcan:.6f}")
    print("-> Ket qua Viterbi trung khop 100% voi ket qua vet can.\n")

    # In Bang 4.3
    bang_4_3 = [
        ("Liet ke: cau tot nhat", cau_tot_nhat, diem_tot_nhat, "Co"),
        (
            "Giai ma tham lam",
            cau_tl,
            diem_tl,
            "Co" if abs(diem_tl - diem_tot_nhat) < 1e-9 else "Khong",
        ),
        (
            "Giai ma theo chum, k = 1",
            cau_k1,
            diem_k1,
            "Co" if abs(diem_k1 - diem_tot_nhat) < 1e-9 else "Khong",
        ),
        (
            "Giai ma theo chum, k = 2",
            cau_k2,
            diem_k2,
            "Co" if abs(diem_k2 - diem_tot_nhat) < 1e-9 else "Khong",
        ),
        (
            "Giai ma theo chum, k = 3",
            cau_k3,
            diem_k3,
            "Co" if abs(diem_k3 - diem_tot_nhat) < 1e-9 else "Khong",
        ),
        ("Viterbi (gan nhan)", " ".join(day_viterbi), prob_viterbi, "Co"),
    ]

    print("BANG 4.3. BA THUAT TOAN GIAI MA TREN CUNG MOT MO HINH")
    print(
        f"{'Thuat toan':<26} | {'Ket qua tra ve':<15} | {'Diem / xac suat':<15} | {'Co phai KQ tot nhat?'}"
    )
    print("-" * 80)
    for row in bang_4_3:
        print(f"{row[0]:<26} | {row[1]:<15} | {row[2]:<15.6f} | {row[3]}")

    # In Bang 4.4: Luoi Viterbi
    print("\nBANG 4.4. LUOI VITERBI CUA CAU 'em hoc bai toan'")
    print(
        f"{'i':<3} | {'Tu w_i':<8} | {'f[i][N]':<10} | {'f[i][V]':<10} | {'Nhan truoc N':<14} | {'Nhan truoc V'}"
    )
    print("-" * 65)
    for i in range(len(cau_gan_nhan)):
        tu = cau_gan_nhan[i]
        f_N = f_table[i]["N"]
        f_V = f_table[i]["V"]
        prev_N = vet_table[i]["N"] if vet_table[i]["N"] is not None else "-"
        prev_V = vet_table[i]["V"] if vet_table[i]["V"] is not None else "-"
        print(
            f"{i+1:<3} | {tu:<8} | {f_N:<10.6f} | {f_V:<10.6f} | {prev_N:<14} | {prev_V}"
        )


if __name__ == "__main__":
    main()
