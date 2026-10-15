function giai_thua(n::Int)
    if n < 0
        return "TRAN SO"
    end
    # Dùng big(n) để tính chính xác trước khi so sánh với typemax(Int64)
    val = factorial(big(n))
    if val > typemax(Int64)
        return "TRAN SO"
    else
        return Int64(val)
    end
end

function main()
    input_str = read(stdin, String)
    tokens = split(input_str)
    for token in tokens
        n = parse(Int, token)
        println(giai_thua(n))
    end
end

main()
