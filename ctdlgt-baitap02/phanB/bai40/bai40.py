import sys

def kadane_chi_so(a: list):
    max_sum = a[0]
    cur_sum = a[0]
    best_start = 1
    best_end = 1
    cur_start = 1

    for i in range(1, len(a)):
        if a[i] > cur_sum + a[i]:
            cur_sum = a[i]
            cur_start = i + 1
        else:
            cur_sum += a[i]

        if cur_sum > max_sum:
            max_sum = cur_sum
            best_start = cur_start
            best_end = i + 1

    return (max_sum, best_start, best_end)

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
        tong, dau, cuoi = kadane_chi_so(a)
        print(f"tong {tong}, doan [{dau}..{cuoi}]")

if __name__ == "__main__":
    main()
