using Printf

struct Mau
    id::Int
    x::Vector{Float64}
    y::String
end

khoang_cach(u, v) = sqrt(sum((u .- v) .^ 2))

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

function lang_gieng_gan_nhat(q, D)
    min_dist = Inf
    best_nhan = ""
    best_id = -1

    for m in D
        dist = khoang_cach(q, m.x)
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

    for line in eachline(stdin)
        parts = split(strip(line))
        if isempty(parts)
            continue
        end
        q = [parse(Float64, parts[j]) for j in 1:d]
        nhan, kc, m_id = lang_gieng_gan_nhat(q, D)
        @printf("%s — mau %d, khoang cach %.4f\n", nhan, m_id, kc)
    end
end

main()
