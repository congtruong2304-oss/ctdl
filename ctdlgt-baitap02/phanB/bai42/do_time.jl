using Printf
using Random

function ngay_tho(a, k, steps)
    max_sum = -10^18
    for i in 1:steps
        cur = sum(a[i:i+k-1])
        if cur > max_sum max_sum = cur end
    end
    return max_sum
end

function cua_so_truot(a, k)
    n = length(a)
    cur = sum(a[1:k])
    max_sum = cur
    for i in (k+1):n
        cur += a[i] - a[i-k]
        if cur > max_sum max_sum = cur end
    end
    return max_sum
end

function benchmark()
    # Warm-up JIT
    mock = rand(-10:10, 20)
    ngay_tho(mock, 5, 5); cua_so_truot(mock, 5)

    n = 1000000
    k = 1000
    Random.seed!(42)
    a = rand(-100:100, n)

    println("--- JULIA BENCHMARK (n=10^6, k=1000) ---")

    # Đo ngây thơ mẫu 5,000 bước
    sample_steps = 5000
    t_sample = @elapsed ngay_tho(a, k, sample_steps)
    t_ngay_tho = t_sample * ((n - k + 1) / sample_steps)

    # Đo cửa sổ trượt
    t_truot = @elapsed cua_so_truot(a, k)

    @printf("Ngay tho O(n*k) : %.4fs\n", t_ngay_tho)
    @printf("Cua so truot O(n): %.4fs\n", t_truot)
    @printf("Ti le nhanh hon : %.2f lan\n", t_ngay_tho / t_truot)
end

benchmark()
