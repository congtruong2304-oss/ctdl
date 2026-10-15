import sys
import os
import math

def khoang_cach(u: list, v: list) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))

def doc_du_lieu(ten_tep: str):
    duong_dan = ten_tep
    if not os.path.exists(duong_dan):
        duong_dan = os.path.join("..", "..", "data", ten_tep)
        if not os.path.exists(duong_dan):
            duong_dan = os.path.join("data", ten_tep)

    with open(duong_dan, "r", encoding="utf-8") as f:
        dong_dau = f.readline().split()
        n = int(dong_dau[0])
        d = int(dong_dau[1])

        D = []
        for i in range(1, n + 1):
            parts = f.readline().split()
            if not parts:
                continue
            x = [float(val) for val in parts[:d]]
            y = parts[d]
            D.append((i, x, y))
    return D, d

def lang_gieng_gan_nhat(q: list, D: list):
    min_dist = float('inf')
    best_nhan = ""
    best_id = -1

    for m_id, x, y in D:
        dist = khoang_cach(q, x)
        if dist < min_dist:
            min_dist = dist
            best_nhan = y
            best_id = m_id

    return best_nhan, min_dist, best_id

def main():
    D, d = doc_du_lieu("hoa30.txt")

    for line in sys.stdin:
        parts = line.strip().split()
        if not parts:
            continue
        q = [float(x) for x in parts[:d]]
        nhan, kc, m_id = lang_gieng_gan_nhat(q, D)
        print(f"{nhan} — mau {m_id}, khoang cach {kc:.4f}")

if __name__ == "__main__":
    main()
