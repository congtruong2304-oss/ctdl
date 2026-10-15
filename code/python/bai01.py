import sys

def main():
    # Doc toan bo du lieu dau vao tu luong chuan
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    A = [int(data[i]) for i in range(1, n + 1)]
    x = int(data[n + 1])
    
    # 1. Thong ke: tong, nho nhat, lon nhat, so lan tham
    total = 0
    low = None
    high = None
    scan_visits = 0
    for val in A:
        scan_visits += 1
        total += val
        if low is None or val < low:
            low = val
        if high is None or val > high:
            high = val
            
    # 2. Tim tuan tu: vi tri dau tien va so phep so sanh
    first_idx = -1
    search_cmps = 0
    for i in range(n):
        search_cmps += 1
        if A[i] == x:
            first_idx = i
            break
            
    # 3. Dem cap chi so i < j
    pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            pairs += 1
            
    # 4. Vong nhan doi: i = 1, 2, 4, ... khong vuot n
    doublings = 0
    size = 1
    while size <= n:
        doublings += 1
        size *= 2
        
    # In ket qua theo dung dinh dang yeu cau
    print(f"SUM {total}")
    print(f"MIN {low if low is not None else 'NA'}")
    print(f"MAX {high if high is not None else 'NA'}")
    print(f"FIRST {first_idx}")
    print(f"SEARCH_CMPS {search_cmps}")
    print(f"PAIRS {pairs}")
    print(f"DOUBLINGS {doublings}")
    print(f"SCAN_VISITS {scan_visits}")

if __name__ == "__main__":
    main()
