function la_chinh_phuong(n::Int)::Bool
    if n < 0
        return false
    end
    left = 0
    right = min(n, 1000000000)
    while left <= right
        mid = left + div(right - left, 2)
        sq = mid * mid
        if sq == n
            return true
        elseif sq < n
            left = mid + 1
        else
            right = mid - 1
        end
    end
    return false
end

function main()
    input_str = read(stdin, String)
    tokens = split(input_str)
    for token in tokens
        n = parse(Int, token)
        println(la_chinh_phuong(n) ? "YES" : "NO")
    end
end

main()
