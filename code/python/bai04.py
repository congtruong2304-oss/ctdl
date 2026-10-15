import sys

def merge_sort_records(records, lo, hi, buffer):
    if lo >= hi:
        return
    
    mid = (lo + hi) // 2
    merge_sort_records(records, lo, mid, buffer)
    merge_sort_records(records, mid + 1, hi, buffer)
    
    i = lo
    j = mid + 1
    out = lo
    
    while i <= mid and j <= hi:
        # So sanh khoa (d2, id) de giu thu tu on dinh va duy nhat
        key_i = (records[i][0], records[i][1])
        key_j = (records[j][0], records[j][1])
        if key_i <= key_j:
            buffer[out] = records[i]
            i += 1
        else:
            buffer[out] = records[j]
            j += 1
        out += 1
        
    while i <= mid:
        buffer[out] = records[i]
        i += 1
        out += 1
        
    while j <= hi:
        buffer[out] = records[j]
        j += 1
        out += 1
        
    for k_idx in range(lo, hi + 1):
        records[k_idx] = buffer[k_idx]

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    
    # 1. Kiem tra so luong token toi thieu de doc n va k
    if len(tokens) < 2:
        print("ERROR: invalid data")
        sys.exit(1)
        
    try:
        n = int(tokens[0])
        k = int(tokens[1])
    except ValueError:
        print("ERROR: invalid data")
        sys.exit(1)
        
    # Kiem tra rang buoc n va k
    if not (1 <= n <= 2000) or not (1 <= k <= n):
        print("ERROR: invalid data")
        sys.exit(1)
        
    # Moi diem can 4 token (id, x, y, label), cuoi cung la qx, qy (2 token)
    expected_tokens = 2 + 4 * n + 2
    if len(tokens) != expected_tokens:
        print("ERROR: invalid data")
        sys.exit(1)
        
    idx = 2
    seen_ids = set()
    records = []
    
    for _ in range(n):
        try:
            pt_id = int(tokens[idx])
            px = int(tokens[idx + 1])
            py = int(tokens[idx + 2])
            label = tokens[idx + 3]
        except ValueError:
            print("ERROR: invalid data")
            sys.exit(1)
            
        # Kiem tra rang buoc id, label va toa do
        if pt_id <= 0 or pt_id > 10**6 or pt_id in seen_ids:
            print("ERROR: invalid data")
            sys.exit(1)
        seen_ids.add(pt_id)
        
        if label not in ("A", "B"):
            print("ERROR: invalid data")
            sys.exit(1)
            
        if not (0 <= px <= 10) or not (0 <= py <= 10):
            print("ERROR: invalid data")
            sys.exit(1)
            
        records.append((pt_id, px, py, label))
        idx += 4
        
    # Doc toa do diem truy van q
    try:
        qx = int(tokens[idx])
        qy = int(tokens[idx + 1])
    except ValueError:
        print("ERROR: invalid data")
        sys.exit(1)
        
    # 2. Tinh binh phuong khoang cach d2 cho tung mau
    # neighbors chua cac tuple: (d2, id, label)
    neighbors = []
    for pt_id, px, py, label in records:
        d2 = (px - qx) ** 2 + (py - qy) ** 2
        neighbors.append((d2, pt_id, label))
        
    # 3. Sap xep merge sort theo khoa (d2, id)
    buffer = [None] * n
    merge_sort_records(neighbors, 0, n - 1, buffer)
    
    # 4. Lay k diem dau tien va dem phieu
    votes_a = 0
    votes_b = 0
    
    print(f"NEIGHBORS {k}")
    for t in range(k):
        d2, pt_id, label = neighbors[t]
        print(f"{pt_id} {label} {d2}")
        if label == "A":
            votes_a += 1
        else:
            votes_b += 1
            
    print(f"VOTES A {votes_a} B {votes_b}")
    
    # Neu bang phieu thi chon A theo quy uoc
    prediction = "A" if votes_a >= votes_b else "B"
    print(f"PREDICT {prediction}")

if __name__ == "__main__":
    main()
