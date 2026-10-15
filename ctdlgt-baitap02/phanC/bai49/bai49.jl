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

function bo_mot_mau(D; kc = kc_euclid)
    n = length(D)
    so_dung = 0
    danh_sach_sai = []

    for i in 1:n
        min_dist = Inf
        best_nhan = ""
        best_id = -1

        for j in 1:n
            if i == j
                continue
            end
            dist = kc(D[i].x, D[j].x)
            if dist < min_dist
                min_dist = dist
                best_nhan = D[j].y
                best_id = D[j].id
            end
        end

        if best_nhan == D[i].y
            so_dung += 1
        else
            push!(danh_sach_sai, (D[i].id, D[i].y, best_nhan, best_id))
        end
    end
    return (so_dung, n, danh_sach_sai)
end

function main()
    D, d = doc_du_lieu("hoa30.txt")

    dung_e, n, sai_e = bo_mot_mau(D; kc = kc_euclid)
    dung_m, _, sai_m = bo_mot_mau(D; kc = kc_manhattan)

    msg_e = isempty(sai_e) ? " — khong mau nao sai" : ""
    @printf("Euclid: %d/%d = %.2f%%%s\n", dung_e, n, dung_e / n * 100, msg_e)

    msg_m = !isempty(sai_m) ? @sprintf(" — sai mau %d (that: %s, du doan: %s)", sai_m[1][1], sai_m[1][2], sai_m[1][3]) : ""
    @printf("Manhattan: %d/%d = %.2f%%%s\n", dung_m, n, dung_m / n * 100, msg_m)
end

main()
