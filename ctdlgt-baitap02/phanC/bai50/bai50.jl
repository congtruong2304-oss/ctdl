using Random
using Printf

struct Mau
    x::Vector{Float64}
    y::Int
end

kc_euclid(u, v) = sqrt(sum((u .- v) .^ 2))

function phan_loai(q, D)
    min_dist = Inf
    best_nhan = -1
    for m in D
        dist = kc_euclid(q, m.x)
        if dist < min_dist
            min_dist = dist
            best_nhan = m.y
        end
    end
    return best_nhan
end

function sinh_du_lieu(n::Int, d::Int)
    D = Mau[]
    for _ in 1:n
        push!(D, Mau(rand(Float64, d), rand(0:2)))
    end
    return D
end

function main()
    Random.seed!(12345)
    d = 20
    q_size = 1000

    Q = [rand(Float64, d) for _ in 1:q_size]
    N_list = [1000, 10000, 100000]
    T = Float64[]

    # JIT warm-up
    D_warm = sinh_du_lieu(10, d)
    phan_loai(Q[1], D_warm)

    for n in N_list
        D = sinh_du_lieu(n, d)
        t = @elapsed for q in Q
            phan_loai(q, D)
        end
        push!(T, t)
        @printf("n = %d: %.4f s\n", n, t)
    end

    @printf("Ti le: T(10^4)/T(10^3) = %.2fx, T(10^5)/T(10^4) = %.2fx\n", T[2]/T[1], T[3]/T[2])
end

main()
