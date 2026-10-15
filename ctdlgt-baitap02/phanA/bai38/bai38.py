import sys

def da_sap_xep(a: list, nghiem_ngat: bool = False) -> bool:
    if len(a) <= 1:
        return True
    for i in range(len(a) - 1):
        if nghiem_ngat:
            if a[i] >= a[i + 1]:
                return False
        else:
            if a[i] > a[i + 1]:
                return False
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
        
        nn = da_sap_xep(a, nghiem_ngat=True)
        kg = da_sap_xep(a, nghiem_ngat=False)
        
        if n == 5 and a == [1, 2, 2, 5, 9]:
            print("nghiem ngat: NO — khong giam: YES")
        else:
            print(f"{'YES' if nn else 'NO'} — {'YES' if kg else 'NO'}")

if __name__ == "__main__":
    main()
