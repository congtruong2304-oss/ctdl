# Day con giam dai nhat (quy hoach dong)
A = [18, 5, 27, 14, 9, 31, 12, 2, 22, 16]

def day_con_giam(n):
    # f[i]: do dai day con giam dai nhat ket thuc tai A[i]
    f = [1] * n
    truoc = [-1] * n

    for i in range(n):
        for j in range(i):
            if A[j] > A[i] and f[j] + 1 > f[i]:
                f[i] = f[j] + 1
                truoc[i] = j

    max_len = max(f)
    # Tim vi tri ket thuc cua day con giam dai nhat
    idx = f.index(max_len)
    
    # Truy vet tim lai day con
    kq = []
    curr = idx
    while curr != -1:
        kq.append(A[curr])
        curr = truoc[curr]
    kq.reverse()

    return max_len, kq, f

def main():
    print("MSSV: N24DCDT102 | Ma ca: 4")
    print("Nhap n (1..10):")
    try:
        n = int(input().strip())
    except (ValueError, EOFError):
        print("Du lieu khong hop le.")
        return
    if not 1 <= n <= len(A):
        print("Du lieu khong hop le.")
        return
    
    max_len, kq, f = day_con_giam(n)
    print("Bang f:", f)
    print("Do dai day con giam dai nhat:", max_len)
    print("Day con giam:", " ".join(map(str, kq)))

if __name__ == "__main__":
    main()
