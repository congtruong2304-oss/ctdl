function tich_lon_nhat_n2(a)
    n = length(a)
    ans = a[1]
    for i in 1:n
        cur = 1
        for j in i:n
            cur *= a[j]
            ans = max(ans, cur)
        end
    end
    return ans
end

function tich_lon_nhat(a)
    ans = a[1]
    max_prod = a[1]
    min_prod = a[1]

    for i in 2:length(a)
        x = a[i]
        if x < 0
            max_prod, min_prod = min_prod, max_prod
        end
        max_prod = max(x, max_prod * x)
        min_prod = min(x, min_prod * x)
        ans = max(ans, max_prod)
    end
    return ans
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
        println(tich_lon_nhat(a))
    end
end

main()
