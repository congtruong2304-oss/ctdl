using Printf
using Random

function cach1(a)
    n = length(a)
    max_sum = a[1]
    for i in 1:n
        for j in i:n
            cur = sum(a[i:j])
            if cur > max_sum max_sum = cur end
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
            if cur > max_sum max_sum = cur end
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

function benchmark()
    # Warm-up JIT
    mock = [1, -2, 3]
    cach1(mock); cach2(mock); kadane(mock)

    println("--- JULIA BENCHMARK ---")
    for n in [200, 400, 800]
        Random.seed!(42)
        a = rand(-100:100, n)

        t_c1 = @elapsed cach1(a)
        t_c2 = @elapsed cach2(a)
        t_c3 = (@elapsed for _ in 1:1000 kadane(a) end) / 1000

        @printf("n = %d | Cach 1: %.6fs | Cach 2: %.6fs | Kadane: %.8fs\n", n, t_c1, t_c2, t_c3)
    end
end

benchmark()
