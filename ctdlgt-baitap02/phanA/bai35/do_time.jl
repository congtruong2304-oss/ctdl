using Printf

function la_nguyen_to(n::Int)::Bool
    if n < 2 return false end
    i = 2
    while i * i <= n
        if n % i == 0 return false end
        i += 1
    end
    return true
end

function sang(n::Int)::Int
    check = fill(true, n + 1)
    p = 2
    while p * p <= n
        if check[p + 1]
            for i in (p * p):p:n
                check[i + 1] = false
            end
        end
        p += 1
    end
    cnt = 0
    for p in 2:n
        if check[p + 1] cnt += 1 end
    end
    return cnt
end

function benchmark()
    # JIT warm-up
    for i in 2:10 la_nguyen_to(i) end
    sang(10)

    for n in [100000, 1000000]
        # Do kiem tra tung so
        t0 = time_ns()
        dem1 = 0
        for i in 2:n
            if la_nguyen_to(i) dem1 += 1 end
        end
        t_kt = (time_ns() - t0) / 1e9

        # Do sang Eratosthenes
        t0 = time_ns()
        dem2 = sang(n)
        t_sang = (time_ns() - t0) / 1e9

        @printf("n = %d: Kiem tra = %.4fs, Sang = %.4fs (so luong: %d - %d)\n", n, t_kt, t_sang, dem1, dem2)
    end
end

benchmark()
