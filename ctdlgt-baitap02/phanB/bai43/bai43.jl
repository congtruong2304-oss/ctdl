const DEM = Ref(0)

function fib_de_quy(n::Int)::Int64
    DEM[] += 1
    if n <= 0 return 0 end
    if n <= 2 return 1 end
    return fib_de_quy(n - 1) + fib_de_quy(n - 2)
end

function fib_ghi_nho_helper(n::Int, memo::Dict{Int, Int64})::Int64
    if n <= 0 return 0 end
    if n <= 2 return 1 end
    if haskey(memo, n) return memo[n] end
    memo[n] = fib_ghi_nho_helper(n - 1, memo) + fib_ghi_nho_helper(n - 2, memo)
    return memo[n]
end

function fib_ghi_nho(n::Int)::Int64
    memo = Dict{Int, Int64}()
    return fib_ghi_nho_helper(n, memo)
end

function fib_lap(n::Int)
    if n <= 0 return 0 end
    if n <= 2 return 1 end
    if n > 92 return "tran long long" end

    prev2 = Int64(1)
    prev1 = Int64(1)
    cur = Int64(0)
    for i in 3:n
        cur = prev1 + prev2
        prev2 = prev1
        prev1 = cur
    end
    return cur
end

function main()
    input_str = read(stdin, String)
    tokens = split(input_str)
    if isempty(tokens) return end

    for token in tokens
        n = parse(Int, token)
        if n <= 30
            DEM[] = 0
            f = fib_de_quy(n)
            println("F = $(f), so loi goi = $(DEM[])")
        else
            f = fib_lap(n)
            if f == "tran long long"
                println("tran long long")
            else
                println("F = $(f)")
            end
        end
    end
end

main()
