import sys

def luy_thua_mod(a: int, b: int, m: int) -> int:
    if m == 1:
        return 0
    r = 1 % m
    a %= m
    while b > 0:
        if b & 1:
            r = (r * a) % m
        a = (a * a) % m
        b >>= 1
    return r

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    idx = 0
    while idx < len(tokens):
        a = int(tokens[idx])
        b = int(tokens[idx + 1])
        m = int(tokens[idx + 2])
        idx += 3
        print(luy_thua_mod(a, b, m))

if __name__ == "__main__":
    main()
