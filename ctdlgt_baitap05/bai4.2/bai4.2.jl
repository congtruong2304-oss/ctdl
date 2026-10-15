# ==============================================================================
# BAI 4.2: CHON HOAT DONG - BON TIEU CHI THAM LAM VA THUAT TOAN TOI UU
# File: bai4.2.jl
# ==============================================================================

using Printf

struct HoatDong
    ten::String
    s::Int
    f::Int
end

# Kiem tra 2 hoat dong tuong thich (khong chong lan) tren nua khoang [s, f)
function tuong_thich(a::HoatDong, b::HoatDong)
    return (a.f <= b.s) || (b.f <= a.s)
end

# 1. Tieu chi Ket thuc som nhat
function ket_thuc_som_nhat(ds::Vector{HoatDong})
    ds_sorted = sort(ds, by = x -> x.f)
    chon = String[]
    last_f = -1
    for h in ds_sorted
        if h.s >= last_f
            push!(chon, h.ten)
            last_f = h.f
        end
    end
    return chon
end

# 2. Tieu chi Bat dau som nhat
function bat_dau_som_nhat(ds::Vector{HoatDong})
    ds_sorted = sort(ds, by = x -> x.s)
    chon = String[]
    last_f = -1
    for h in ds_sorted
        if h.s >= last_f
            push!(chon, h.ten)
            last_f = h.f
        end
    end
    return chon
end

# 3. Tieu chi Ngan nhat
function ngan_nhat(ds::Vector{HoatDong})
    ds_sorted = sort(ds, by = x -> (x.f - x.s, x.s))
    da_chon = HoatDong[]
    for h in ds_sorted
        ok = true
        for c in da_chon
            if !tuong_thich(h, c)
                ok = false
                break
            end
        end
        if ok
            push!(da_chon, h)
        end
    end

    res = [h.ten for h in da_chon]
    sort!(res, by = x -> parse(Int, x[2:end]))
    return res
end

# 4. Tieu chi It chong lan nhat (logic lap khop theo ban Python)
function it_chong_lan_nhat(ds::Vector{HoatDong})
    con_lai = copy(ds)
    chon = String[]

    while !isempty(con_lai)
        min_overlap = 1_000_000_000
        best_idx = -1

        for i in 1:length(con_lai)
            cnt = 0
            for j in 1:length(con_lai)
                if i != j && !tuong_thich(con_lai[i], con_lai[j])
                    cnt += 1
                end
            end
            if cnt < min_overlap
                min_overlap = cnt
                best_idx = i
            end
        end

        best_h = con_lai[best_idx]
        push!(chon, best_h.ten)

        # Loc lai cac hoat dong tuong thich voi best_h
        con_lai = [o for o in con_lai if tuong_thich(best_h, o)]
    end

    sort!(chon, by = x -> parse(Int, x[2:end]))
    return chon
end

# Tim so hoat dong nhieu nhat that su (Vet can tap con)
function toi_uu_vet_can(ds::Vector{HoatDong})
    n = length(ds)
    best_set = String[]

    for mask in 0:((1 << n) - 1)
        sub = [ds[i] for i in 1:n if (mask & (1 << (i - 1))) != 0]

        ok = true
        for i in 1:length(sub)
            for j in (i + 1):length(sub)
                if !tuong_thich(sub[i], sub[j])
                    ok = false
                    break
                end
            end
            if !ok
                break
            end
        end

        if ok && length(sub) > length(best_set)
            best_set = [h.ten for h in sub]
        end
    end

    sort!(best_set, by = x -> parse(Int, x[2:end]))
    return best_set
end

function main()
    # Muoi hoat dong o Muc C
    data = [
        HoatDong("H1", 1, 5),
        HoatDong("H2", 2, 5),
        HoatDong("H3", 2, 6),
        HoatDong("H4", 3, 4),
        HoatDong("H5", 4, 8),
        HoatDong("H6", 6, 9),
        HoatDong("H7", 8, 11),
        HoatDong("H8", 9, 14),
        HoatDong("H9", 11, 13),
        HoatDong("H10", 12, 15)
    ]

    opt = toi_uu_vet_can(data)
    max_count = length(opt)

    kq_kt = ket_thuc_som_nhat(data)
    kq_bd = bat_dau_som_nhat(data)
    kq_nn = ngan_nhat(data)
    kq_cl = it_chong_lan_nhat(data)

    tieuchi = [
        ("Ket thuc som nhat", kq_kt),
        ("Bat dau som nhat", kq_bd),
        ("Ngan nhat", kq_nn),
        ("It chong lan nhat", kq_cl),
        ("So nhieu nhat that su", opt)
    ]

    @printf("%-22s | %-20s | %-6s | %s\n", 
            "Tieu chi", "Cac hoat dong duoc chon", "So HD", "Co dat toi uu khong?")
    println(repeat("-", 75))

    for (tc, ds_chon) in tieuchi
        so_hd = length(ds_chon)
        str_hd = join(ds_chon, ", ")
        dat = (tc == "So nhieu nhat that su") ? "-" : ((so_hd == max_count) ? "Co" : "Khong")

        @printf("%-22s | %-20s | %-6d | %s\n", 
                tc, str_hd, so_hd, dat)
    end
end

main()
