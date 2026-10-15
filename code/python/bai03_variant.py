import sys

def bound(a, n, x, upper):
    lo = 0
    hi = n
    probes = 0
    while lo < hi:
        mid = lo + (hi - lo) // 2
        probes += 1
        if not upper:
            move_right = (a[mid] < x)
        else:
            move_right = (a[mid] <= x)
            
        if move_right:
            lo = mid + 1
        else:
            hi = mid
    return lo, probes

def main():
    data = sys.stdin.read().split()
    if not data:
        return

    n = int(data[0])
    a = [int(data[i]) for i in range(1, n + 1)]
    L = int(data[n + 1])
    R = int(data[n + 2])

    # Kiem tra tien dieu kien: day phai duoc sap khong giam
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            print("ERROR: array must be sorted")
            sys.exit(1)

    # Neu khoang khong hop le thi so phan tu bang 0
    if L > R:
        print("COUNT_RANGE 0")
        print("LOWER_L NA")
        print("UPPER_R NA")
        return

    lower_L, _ = bound(a, n, L, False)
    upper_R, _ = bound(a, n, R, True)

    count_range = upper_R - lower_L

    print(f"COUNT_RANGE {count_range}")
    print(f"LOWER_L {lower_L}")
    print(f"UPPER_R {upper_R}")

if __name__ == "__main__":
    main()
