function tim_cap_tong_s(a, S)
    # Buoc 1: Sap xep mang ton O(n log n)
    a_sap_xep = sort(a)
    
    # Buoc 2: Hai con tro ton O(n), chi so tu 1
    i = 1
    j = length(a_sap_xep)
    
    while i < j
        tong = a_sap_xep[i] + a_sap_xep[j]
        if tong == S
            return (a_sap_xep[i], a_sap_xep[j])
        elseif tong < S
            i += 1  # Loai bo a[i]
        else
            j -= 1  # Loai bo a[j]
        end
    end
    
    return nothing
end

A = [8, 3, 5, 1, 9, 2]
S = 10
ket_qua = tim_cap_tong_s(A, S)

if ket_qua !== nothing
    println("Tim thay cap co tong bang ", S, ": ", ket_qua[1], " + ", ket_qua[2], " = ", S)
else
    println("Khong tim thay cap nao co tong bang ", S)
end
