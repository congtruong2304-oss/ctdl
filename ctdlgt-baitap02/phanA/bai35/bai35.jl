using Printf

function la_nguyen_to(n::Int)::Bool
    if n < 2
        return false
    end
    i = 2
    while i * i <= n
        if n % i == 0
            return false
        end
        i += 1
    end
    return true
end

function sang(n::Int)
    check = fill(true, n + 1)
    check[1] = false # Julia chỉ số từ 1 (tương ứng số 0)
    check[2] = false # tương ứng số 1
    p = 2
    while p * p <= n
        if check[p + 1]
            for i in (p * p):p:n
                check[i + 1] = false
            end
        end
        p += 1
    end
    primes = Int[]
    for p in 2:n
        if check[p + 1]
            push!(primes, p)
        end
    end
    return primes
end

function main()
    input_str = read(stdin, String)
    tokens = split(input_str)
    for token in tokens
        n = parse(Int, token)
        if n <= 30
            res = sang(n)
            println(join(res, " ") * "  ($(length(res)) so)")
        elseif n < 1000000
            res = sang(n)
            println("so luong = $(length(res))")
        else
            res = sang(n)
            println("so luong = $(length(res)), tong = $(sum(res))")
        end
    end
end

main()
