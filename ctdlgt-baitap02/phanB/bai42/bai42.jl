function cua_so_truot(a, k)
    n = length(a)
    cur_sum = sum(a[1:k])
    max_sum = cur_sum
    best_pos = 1

    for i in (k + 1):n
        cur_sum += a[i] - a[i - k]
        if cur_sum > max_sum
            max_sum = cur_sum
            best_pos = i - k + 1
        end
    end
    return (max_sum, best_pos)
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
        k = parse(Int, tokens[idx + 1])
        idx += 2
        a = [parse(Int, tokens[idx + i - 1]) for i in 1:n]
        idx += n
        tong, pos = cua_so_truot(a, k)
        println("tong $(tong), bat dau tai vi tri $(pos)")
    end
end

main()
