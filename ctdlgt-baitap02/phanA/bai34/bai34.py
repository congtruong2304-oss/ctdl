import sys

def dao_nguoc(n: int) -> int:
    sign = -1 if n < 0 else 1
    m = abs(n)
    rev = 0
    while m > 0:
        rev = rev * 10 + (m % 10)
        m //= 10
    return sign * rev

def main():
    input_data = sys.stdin.read().split()
    for token in input_data:
        n = int(token)
        print(dao_nguoc(n))

if __name__ == "__main__":
    main()
