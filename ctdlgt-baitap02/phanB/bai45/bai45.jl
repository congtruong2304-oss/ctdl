function luy_thua_mod(a::Int, b::Int, m::Int)::Int
    if m == 1
        return 0
    end
    r = 1 % m
    # Dùng Int128 hoặc BigInt để tránh tràn tích số nguyên 64-bit
    a_cur = Int128(a % m)
    r_cur = Int128(r)
    m_128 = Int128(m)
    b_cur = b

    while b_cur > 0
        if (b_cur & 1) == 1
            r_cur = (r_cur * a_cur) % m_128
        end
        a_cur = (a_cur * a_cur) % m_128
        b_cur >>= 1
    end
    return Int(r_cur)
end

function main()
    input_str = read(stdin, String)
    tokens = split(input_str)
    if isempty(tokens)
        return
    end
    idx = 1
    while idx <= length(tokens)
        a = parse(Int, tokens[idx])
        b = parse(Int, tokens[idx + 1])
        m = parse(Int, tokens[idx + 2])
        idx += 3
        println(luy_thua_mod(a, b, m))
    end
end

main()
