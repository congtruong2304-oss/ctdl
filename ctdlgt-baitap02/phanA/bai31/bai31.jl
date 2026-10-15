using Printf

function thong_ke(a)
    tong = Int64(a[1])
    nho_nhat = a[1]
    lon_nhat = a[1]
    n = length(a)
    
    for i in 2:n
        x = a[i]
        tong += x
        if x < nho_nhat
            nho_nhat = x
        end
        if x > lon_nhat
            lon_nhat = x
        end
    end
    
    trung_binh = tong / n
    return tong, trung_binh, nho_nhat, lon_nhat
end

function main()
    input_str = read(stdin, String)
    tokens = split(input_str)
    if isempty(tokens)
        return
    end
    n = parse(Int, tokens[1])
    a = [parse(Int64, tokens[i]) for i in 2:(n + 1)]
    
    tong, tb, mi, ma = thong_ke(a)
    @printf("%d %.4f %d %d\n", tong, tb, mi, ma)
end

main()
