import sys
import random

def cach1(a: list) -> int:
    n = len(a)
    max_sum = a[0]
    for i in range(n):
        for j in range(i, n):
            cur = sum(a[i:j+1])
            if cur > max_sum:
                max_sum = cur
    return max_sum

def cach2(a: list) -> int:
    n = len(a)
    max_sum = a[0]
    for i in range(n):
        cur = 0
        for j in range(i, n):
            cur += a[j]
            if cur > max_sum:
                max_sum = cur
    return max_sum

def kadane(a: list) -> int:
    max_sum = a[0]
    cur_sum = a[0]
    for x in a[1:]:
        cur_sum = max(x, cur_sum + x)
        max_sum = max(max_sum, cur_sum)
    return max_sum

def kiem_thu_tu_dong(so_lan=1000):
    for _ in range(so_lan):
        n = random.randint(1, 30)
        a = [random.randint(-100, 100) for _ in range(n)]
        res1 = cach1(a)
        res2 = cach2(a)
        res3 = kadane(a)
        if not (res1 == res2 == res3):
            print(f"FAILED voi mang: {a}")
            return False
    print(f"SUCCESS: Da vuot qua {so_lan}/{so_lan} test ngau nhien!")
    return True

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
        print(kadane(a))

if __name__ == "__main__":
    main()
