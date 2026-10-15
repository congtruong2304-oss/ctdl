# Day con tang dai nhat (quy hoach dong): f[i] = do dai day con tang dai nhat ket thuc dung tai a[i].
A = [3, 10, 2, 1, 20, 4, 6, 21, 8]

def day_con_tang(a):
    n = len(a)
    f = [1] * n          # co so: moi phan tu tu no la mot day con dai 1
    tu = [-1] * n        # tu[i] = chi so dung truoc i trong day con; -1 la khong co
    for i in range(n):
        for j in range(i):
            if a[j] < a[i] and f[j] + 1 > f[i]:
                f[i] = f[j] + 1
                tu[i] = j
        print(f"i = {i + 1}: a = {a[i]}, f = {f[i]}, tu = {tu[i] + 1 if tu[i] != -1 else 'khong'}")
    k = 0
    for i in range(n):
        if f[i] > f[k]: k = i    # vi tri dau tien dat max
    day = []
    while k != -1:               # truy vet nguoc theo tu
        day.append(a[k])
        k = tu[k]
    day.reverse()
    return max(f), day

def main():
    print("MSSV: DIEN_MSSV | Ma ca: DIEN_MA_CA")
    print(f"Nhap n (1..{len(A)}), so phan tu dau tien cua day duoc xet:")
    try:
        n = int(input().strip())
    except (ValueError, EOFError):
        print("Du lieu khong hop le.")
        return
    if not 1 <= n <= len(A):
        print("Du lieu khong hop le.")
        return
    a = A[:n]
    print("Day xet:", " ".join(map(str, a)))
    do_dai, day = day_con_tang(a)
    print("Do dai day con tang dai nhat:", do_dai)
    print("Mot day con tang dai nhat:", " ".join(map(str, day)))

if __name__ == "__main__":
    main()
