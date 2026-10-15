using Printf
using Random

# Cách 2 của Bài 39: O(n^2)
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

function do_thoi_gian(a, lap::Int=3)::Float64
    min_t = 1e9
    for _ in 1:lap
        t = @elapsed cach2(a)
        if t < min_t
            min_t = t
        end
    end
    return min_t
end

function main()
    # JIT warm-up: goi truoc 1 lan de bien dich
    mock = [1, -2, 3, 4]
    cach2(mock)

    Random.seed!(42)
    Ns = [500, 1000, 2000, 4000]
    times = Float64[]

    println("--- JULIA BENCHMARK O(n^2) ---")
    for n in Ns
        a = rand(-100:100, n)
        t = do_thoi_gian(a, 3)
        push!(times, t)
        @printf("n = %d : %.6fs\n", n, t)
    end

    println("\n--- TI LE TANG ---")
    for i in 2:length(Ns)
        @printf("n = %d -> %d : ti le = %.2f\n", Ns[i-1], Ns[i], times[i] / times[i-1])
    end
end

main()
