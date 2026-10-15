import sys
import math

LLONG_MAX = (1 << 63) - 1

def giai_thua(n: int):
    if n < 0:
        return None
    val = math.factorial(n)
    if val > LLONG_MAX:
        return "TRAN SO"
    return val

def main():
    input_data = sys.stdin.read().split()
    for token in input_data:
        n = int(token)
        print(giai_thua(n))

if __name__ == "__main__":
    main()
