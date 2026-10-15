import sys

def la_chinh_phuong(n: int) -> bool:
    if n < 0:
        return False
    left, right = 0, min(n, 10**9)
    while left <= right:
        mid = (left + right) // 2
        sq = mid * mid
        if sq == n:
            return True
        elif sq < n:
            left = mid + 1
        else:
            right = mid - 1
    return False

def main():
    input_data = sys.stdin.read().split()
    for token in input_data:
        n = int(token)
        print("YES" if la_chinh_phuong(n) else "NO")

if __name__ == "__main__":
    main()
