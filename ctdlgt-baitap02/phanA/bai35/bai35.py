import sys

def la_nguyen_to(n: int) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def sang(n: int) -> list:
    check = [True] * (n + 1)
    check[0] = check[1] = False
    p = 2
    while p * p <= n:
        if check[p]:
            for i in range(p * p, n + 1, p):
                check[i] = False
        p += 1
    return [p for p in range(2, n + 1) if check[p]]

def main():
    input_data = sys.stdin.read().split()
    for token in input_data:
        n = int(token)
        if n <= 30:
            res = sang(n)
            print(f"{' '.join(map(str, res))}  ({len(res)} so)")
        elif n < 1000000:
            res = sang(n)
            print(f"so luong = {len(res)}")
        else:
            res = sang(n)
            print(f"so luong = {len(res)}, tong = {sum(res)}")

if __name__ == "__main__":
    main()
