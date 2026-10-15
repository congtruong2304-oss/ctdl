import sys

def cua_so_truot(a: list, k: int):
    n = len(a)
    cur_sum = sum(a[:k])
    max_sum = cur_sum
    best_pos = 1

    for i in range(k, n):
        cur_sum += a[i] - a[i - k]
        if cur_sum > max_sum:
            max_sum = cur_sum
            best_pos = i - k + 2

    return (max_sum, best_pos)

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    idx = 0
    while idx < len(tokens):
        n = int(tokens[idx])
        k = int(tokens[idx + 1])
        idx += 2
        a = [int(tokens[idx + i]) for i in range(n)]
        idx += n
        tong, pos = cua_so_truot(a, k)
        print(f"tong {tong}, bat dau tai vi tri {pos}")

if __name__ == "__main__":
    main()
