import sys
import math

def khoang_cach(u: list, v: list) -> float:
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(u, v)))

def lang_gieng_gan_nhat(q: list, D: list):
    min_dist = float('inf')
    best_label = ""
    best_idx = -1

    for i, item in enumerate(D, start=1):
        dist = khoang_cach(q, item["x"])
        if dist < min_dist:
            min_dist = dist
            best_label = item["y"]
            best_idx = i

    return (best_label, min_dist, best_idx)

def main():
    # Tập dữ liệu mẫu huấn luyện chuẩn bài thực hành 1.3
    D = [
        {"x": [1.4, 0.2], "y": "Setosa"},
        {"x": [1.3, 0.2], "y": "Setosa"},
        {"x": [1.5, 0.2], "y": "Setosa"},
        {"x": [4.7, 1.4], "y": "Versicolor"},
        {"x": [4.5, 1.5], "y": "Versicolor"},
        {"x": [4.9, 1.5], "y": "Versicolor"},
        {"x": [6.0, 2.5], "y": "Virginica"},
        {"x": [5.8, 2.1], "y": "Virginica"},
    ]

    tokens = sys.stdin.read().split()
    if not tokens:
        return

    idx = 0
    while idx < len(tokens):
        q = [float(tokens[idx]), float(tokens[idx + 1])]
        idx += 2
        nhan, dist, chi_so = lang_gieng_gan_nhat(q, D)
        if dist < 1e-9:
            print(f"{nhan} — trung dung mau {chi_so}, khoang cach 0")
        else:
            d_str = f"{dist:.1f}" if abs(dist - round(dist, 1)) < 1e-5 else f"{dist:.4f}"
            print(f"{nhan} — lang gieng la mau {chi_so}, khoang cach {d_str}")

if __name__ == "__main__":
    main()
