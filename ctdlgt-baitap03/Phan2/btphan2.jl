function sap_xep_chen!(a)
    n = length(a)
    for i in 2:n
        x = a[i]
        j = i - 1
        while j >= 1 && a[j] > x
            a[j + 1] = a[j]
            j -= 1
        end
        a[j + 1] = x
    end
    return a
end

A = [8, 3, 5, 1, 9, 2]
println("Ket qua: ", sap_xep_chen!(A))
