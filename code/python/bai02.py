import sys

def insertion_sort(a, n):
    comparisons = 0
    shifts = 0
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] <= key:
                break
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = key
    return comparisons, shifts

def merge_sort(a, lo, hi, buffer):
    if lo >= hi:
        return 0
    
    mid = (lo + hi) // 2
    cmps = 0
    cmps += merge_sort(a, lo, mid, buffer)
    cmps += merge_sort(a, mid + 1, hi, buffer)
    
    i = lo
    j = mid + 1
    out = lo
    
    while i <= mid and j <= hi:
        cmps += 1
        if a[i] <= a[j]:
            buffer[out] = a[i]
            i += 1
        else:
            buffer[out] = a[j]
            j += 1
        out += 1
        
    while i <= mid:
        buffer[out] = a[i]
        i += 1
        out += 1
        
    while j <= hi:
        buffer[out] = a[j]
        j += 1
        out += 1
        
    for k in range(lo, hi + 1):
        a[k] = buffer[k]
        
    return cmps

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    orig = [int(data[i]) for i in range(1, n + 1)]
    
    # Tao hai ban sao doc lap
    a_insert = orig.copy()
    a_merge = orig.copy()
    
    # 1. Chay Insertion Sort
    ins_cmps, ins_shifts = insertion_sort(a_insert, n)
    
    # 2. Chay Merge Sort
    buffer = [0] * n
    merge_cmps = merge_sort(a_merge, 0, n - 1, buffer) if n > 0 else 0
    
    # In ket qua theo dinh dang yeu cau
    print("INSERT " + " ".join(map(str, a_insert)))
    print(f"INSERT_CMPS {ins_cmps}")
    print(f"INSERT_SHIFTS {ins_shifts}")
    print("MERGE " + " ".join(map(str, a_merge)))
    print(f"MERGE_CMPS {merge_cmps}")

if __name__ == "__main__":
    main()
