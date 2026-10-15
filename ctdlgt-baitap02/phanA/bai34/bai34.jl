function dao_nguoc(n::Int)::Int
    sign = n < 0 ? -1 : 1
    m = abs(n)
    rev = 0
    while m > 0
        rev = rev * 10 + (m % 10)
        m = div(m, 10)
    end
    return sign * rev
end

function main()
    input_str = read(stdin, String)
    tokens = split(input_str)
    for token in tokens
        n = parse(Int, token)
        println(dao_nguoc(n))
    end
end

main()
