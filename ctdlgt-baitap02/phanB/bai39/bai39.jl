function cach1(a)
    n = length(a)
    max_sum = a[1]
    for i in 1:n
        for j in i:n
            cur = sum(a[i:j])
            if cur > max_sum
                max_sum = cur
            end
        end
    end
    return max_sum
end

function cach2(a)
    n = length(a)
    max_sum = a[1]
    for i in 1:n
        cur = 0
        for j in i:n
            cur += a[j]
            if cur > max_sum
                max_sum = cur
            end
        end
    end
    return max_sum
end

function kadane(a)
    max_sum = a[1]
    cur_sum = a[1]
    for i in 2:length(a)
        cur_sum = max(a[i], cur_sum + a[i])
        max_sum = max(max_sum, cur_sum)
    end
    return max_sum
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
        println(kadane(a))
    end
end

main()
