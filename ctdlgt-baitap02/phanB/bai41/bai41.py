import sys

def tich_lon_nhat_n2(a: list) -> int:
    n = len(a)
    ans = a[0]
    for i in range(n):
        cur = 1
        for j in range(i, n):
            cur *= a[j]
            if cur > ans:
                ans = cur
    return ans

def tich_lon_nhat(a: list) -> int:
    ans = a[0]
    max_prod = a[0]
    min_prod = a[0]

    for x in a[1:]:
        if x < 0:
            max_prod, min_prod = min_prod, max_prod
        max_prod = max(x, max_prod * x)
        min_prod = min(x, min_prod * x)
        ans = max(ans, max_prod)
    return ans

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    idx = 0
    while idx < len(tokens):
        n = int(tokens[idx])
        idx += 1
        a = [int(tokens[idx + i]) for i in range(n)]
        idx += n
        print(tich_lon_nhat(a))

if __name__ == "__main__":
    main()
