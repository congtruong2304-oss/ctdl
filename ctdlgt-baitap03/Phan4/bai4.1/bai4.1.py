import math
from collections import Counter

def chuan_hoa_min_max(X):
    m = len(X[0])
    cmin = [min(hang[j] for hang in X) for j in range(m)]
    cmax = [max(hang[j] for hang in X) for j in range(m)]
    Z = []
    for hang in X:
        z = [(hang[j] - cmin[j]) / (cmax[j] - cmin[j]) if cmax[j] != cmin[j] else 0.0 for j in range(m)]
        Z.append(z)
    return Z, cmin, cmax

def khoang_cach(u, v):
    return math.sqrt(sum((p - q) ** 2 for p, q in zip(u, v)))

def k_lang_gieng(Z, y, z_moi, k):
    # Luu cap (khoang_cach, nhan) de khong dut lien he khi sap xep
    d = [(khoang_cach(Z[i], z_moi), y[i]) for i in range(len(Z))]
    d.sort(key=lambda t: t[0])
    phieu = Counter(nhan for _, nhan in d[:k])
    return phieu.most_common(1)[0][0]

# Du lieu huan luyen: [So bai nop, So phut]
X = [[2, 300], [3, 450], [4, 600], [15, 1800], [16, 2000], [18, 2400], [5, 2200], [17, 700]]
y = ["chua dat", "chua dat", "chua dat", "dat", "dat", "dat", "chua dat", "dat"]

Z, cmin, cmax = chuan_hoa_min_max(X)

# Mau can du doan: 14 bai, 800 phut
x_moi = [14, 800]
z_moi = [(x_moi[j] - cmin[j]) / (cmax[j] - cmin[j]) for j in range(len(x_moi))]

k = 3
ket_qua = k_lang_gieng(Z, y, z_moi, k)
print(f"Du doan cho mau {x_moi} voi K={k}: {ket_qua}")
