import sys

def thong_ke(a):
    tong = a[0]
    nho_nhat = a[0]
    lon_nhat = a[0]
    
    for x in a[1:]:
        tong += x
        if x < nho_nhat:
            nho_nhat = x
        if x > lon_nhat:
            lon_nhat = x
            
    trung_binh = tong / len(a)
    return tong, trung_binh, nho_nhat, lon_nhat

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n+1]]
    
    tong, tb, mi, ma = thong_ke(a)
    print(f"{tong} {tb:.4f} {mi} {ma}")

if __name__ == "__main__":
    main()
