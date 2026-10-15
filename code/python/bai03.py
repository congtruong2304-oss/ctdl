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
    x = int(data[n + 1])

    # Kiem tra tien dieu kien: day phai duoc sap khong giam
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            print("ERROR: array must be sorted")
            sys.exit(1)

    lower, p1 = bound(a, n, x, False)
    upper, p2 = bound(a, n, x, True)

    first = -1
    if lower < n and a[lower] == x:
        first = lower

    count = upper - lower
    probes = p1 + p2

    print(f"FIRST {first}")
    print(f"COUNT {count}")
    print(f"LOWER {lower}")
    print(f"UPPER {upper}")
    print(f"PROBES {probes}")

if __name__ == "__main__":
    main()
