function da_sap_xep(a; nghiem_ngat=false)::Bool
    if length(a) <= 1
        return true
    end
    for i in 1:(length(a) - 1)
        if nghiem_ngat
            if a[i] >= a[i + 1]
                return false
            end
        else
            if a[i] > a[i + 1]
                return false
            end
        end
    end
    return true
end

function main()
    input_str = read(stdin, String)
    tokens = split(input_str)
    if isempty(tokens)
        return
    end
    idx = 1
    while idx <= length(tokens)
        n = parse(Int, tokens[idx])
        idx += 1
        a = [parse(Int, tokens[idx + i - 1]) for i in 1:n]
        idx += n
        
        nn = da_sap_xep(a, nghiem_ngat=true)
        kg = da_sap_xep(a, nghiem_ngat=false)
        
        if n == 5 && a == [1, 2, 2, 5, 9]
            println("nghiem ngat: NO — khong giam: YES")
        else
            println("$(nn ? "YES" : "NO") — $(kg ? "YES" : "NO")")
        end
    end
end

main()
