using Printf

struct Mau
    id::Int
    x::Vector{Float64}
    y::String
end

kc_euclid(u, v) = sqrt(sum((u .- v) .^ 2))
kc_manhattan(u, v) = sum(abs.(u .- v))

function doc_du_lieu(ten_tep::String)
    duong_dan = ten_tep
    if !isfile(duong_dan)
        duong_dan = joinpath("..", "..", "data", ten_tep)
        if !isfile(duong_dan)
            duong_dan = joinpath("data", ten_tep)
        end
    end

    lines = readlines(duong_dan)
    first_parts = split(lines[1])
    n = parse(Int, first_parts[1])
    d = parse(Int, first_parts[2])

    D = Mau[]
    for i in 1:n
        parts = split(lines[i + 1])
        x = [parse(Float64, parts[j]) for j in 1:d]
        y = String(parts[d + 1])
        push!(D, Mau(i, x, y))
    end
    return (D, d)
end

function lang_gieng_gan_nhat(q, D; kc = kc_euclid, bo_qua_id = -1)
    min_dist = Inf
    best_nhan = ""
    best_id = -1

    for m in D
        if m.id == bo_qua_id
            continue
        end
        dist = kc(q, m.x)
        if dist < min_dist
            min_dist = dist
            best_nhan = m.y
            best_id = m.id
        end
    end
    return (best_nhan, min_dist, best_id)
end

function main()
    D, d = doc_du_lieu("hoa30.txt")

    q = [6.5, 3.0, 5.5, 2.0]
    re = lang_gieng_gan_nhat(q, D; kc = kc_euclid)
    rm = lang_gieng_gan_nhat(q, D; kc = kc_manhattan)

    println("Mau [6.5, 3.0, 5.5, 2.0]:")
    @printf("  Euclid:    %s (mau %d, kc %.4f)\n", re[1], re[3], re[2])
    @printf("  Manhattan: %s (mau %d, kc %.4f)\n", rm[1], rm[3], rm[2])

    dung_e, dung_m = 0, 0
    n = length(D)
    for m in D
        ke = lang_gieng_gan_nhat(m.x, D; kc = kc_euclid, bo_qua_id = m.id)
        km = lang_gieng_gan_nhat(m.x, D; kc = kc_manhattan, bo_qua_id = m.id)
        if ke[1] == m.y
            dung_e += 1
        end
        if km[1] == m.y
            dung_m += 1
        end
        if m.id == 26
            println("Mau 26 bi bo ra:")
            @printf("  Manhattan du doan: %s (mau %d, kc %.1f)\n", km[1], km[3], km[2])
        end
    end

    println("Do chinh xac LOO:")
    @printf("  Euclid:    %d/%d = %.2f%%\n", dung_e, n, dung_e / n * 100)
    @printf("  Manhattan: %d/%d = %.2f%%\n", dung_m, n, dung_m / n * 100)
end

main()
