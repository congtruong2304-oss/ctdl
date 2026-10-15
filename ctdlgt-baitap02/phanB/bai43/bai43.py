import sys

dem = 0

def fib_de_quy(n: int) -> int:
    global dem
    dem += 1
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    return fib_de_quy(n - 1) + fib_de_quy(n - 2)

def fib_ghi_nho(n: int, bo_nho=None) -> int:
    if bo_nho is None:
        bo_nho = {}
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    if n in bo_nho:
        return bo_nho[n]
    bo_nho[n] = fib_ghi_nho(n - 1, bo_nho) + fib_ghi_nho(n - 2, bo_nho)
    return bo_nho[n]

def fib_lap(n: int):
    if n <= 0:
        return 0
    if n <= 2:
        return 1
    if n > 92:
        return "tran long long"
    
    prev2, prev1 = 1, 1
    for _ in range(3, n + 1):
        cur = prev1 + prev2
        prev2, prev1 = prev1, cur
    return cur

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    for token in tokens:
        n = int(token)
        if n <= 30:
            global dem
            dem = 0
            f = fib_de_quy(n)
            print(f"F = {f}, so loi goi = {dem}")
        else:
            f = fib_lap(n)
            if f == "tran long long":
                print("tran long long")
            else:
                print(f"F = {f}")

if __name__ == "__main__":
    main()
