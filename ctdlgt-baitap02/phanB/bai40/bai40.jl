function kadane_chi_so(a)
    max_sum = a[1]
    cur_sum = a[1]
    best_start = 1
    best_end = 1
    cur_start = 1

    for i in 2:length(a)
        if a[i] > cur_sum + a[i]
            cur_sum = a[i]
            cur_start = i
        else
            cur_sum += a[i]
        end

        if cur_sum > max_sum
            max_sum = cur_sum
            best_start = cur_start
            best_end = i
        end
    end
    return (max_sum, best_start, best_end)
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
        tong, dau, cuoi = kadane_chi_so(a)
        println("tong $(tong), doan [$(dau)..$(cuoi)]")
    end
end

main()
