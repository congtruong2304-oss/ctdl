def tim_cap_tong_s(a, S):
    # Buoc 1: Sap xep mang ton O(n log n)
    a_sap_xep = sorted(a)
    
    # Buoc 2: Ky thuat hai con tro ton O(n)
    i = 0
    j = len(a_sap_xep) - 1
    
    while i < j:
        tong = a_sap_xep[i] + a_sap_xep[j]
        if tong == S:
            return a_sap_xep[i], a_sap_xep[j]
        elif tong < S:
            i += 1  # Loai bo a[i], tang tong
        else:
            j -= 1  # Loai bo a[j], giam tong
            
    return None

A = [8, 3, 5, 1, 9, 2]
S = 10
ket_qua = tim_cap_tong_s(A, S)

if ket_qua:
    print(f"Tim thay cap co tong bang {S}: {ket_qua[0]} + {ket_qua[1]} = {S}")
else:
    print(f"Khong tim thay cap nao co tong bang {S}")
