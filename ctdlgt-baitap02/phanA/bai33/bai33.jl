function phan_tich(n::Int)
    so_chu_so = 0
    tong_chu_so = 0
    while n > 0
        tong_chu_so += n % 10
        so_chu_so += 1
        n = div(n, 10)
    end
    return (so_chu_so, tong_chu_so)
end

function main()
    input_str = read(stdin, String)
    tokens = split(input_str)
    for token in tokens
        n = parse(Int, token)
        so_chu_so, tong_chu_so = phan_tich(n)
        println("$(so_chu_so) $(tong_chu_so)")
    end
end

main()
