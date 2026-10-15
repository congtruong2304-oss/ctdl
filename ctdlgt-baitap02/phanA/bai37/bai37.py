import sys

def dem(a: list):
    chan = 0
    le = 0
    am = 0
    for x in a:
        if x < 0:
            am += 1
        if x % 2 == 0:
            chan += 1
        else:
            le += 1
    return (chan, le, am)

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
        chan, le, am = dem(a)
        print(f"chan {chan}, le {le}, am {am}")

if __name__ == "__main__":
    main()
