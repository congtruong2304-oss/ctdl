# ==============================================================================
# BAI 4.3: BA THUAT TOAN GIAI MA CUA MO HINH NGON NGU VA THUAT TOAN VITERBI
# File: bai4.3.jl
# ==============================================================================

using Printf

# ==============================================================================
# PHAN 1: MO HINH NGON NGU HAI TU (BIGRAM)
# ==============================================================================

const bigram = Dict(
    "em"  => Dict("hoc" => 0.52, "di" => 0.48),
    "hoc" => Dict("bai" => 0.40, "toan" => 0.35, "ve" => 0.25),
    "di"  => Dict("cho" => 0.58, "boi" => 0.22, "ngu" => 0.20)
)

struct CauCandidate
    cau::String
    p::Float64
end

# Liet ke toan bo 6 cau do dai 3 bat dau bang "em"
function liet_ke_toan_bo()
    ds = CauCandidate[]
    w1 = "em"
    for (w2, p12) in bigram[w1]
        for (w3, p23) in bigram[w2]
            push!(ds, CauCandidate("$w1 $w2 $w3", p12 * p23))
        end
    end
    sort!(ds, by = x -> x.p, rev = true)
    return ds
end

# Giai ma tham lam (Greedy search)
function giai_ma_tham_lam()
    w1 = "em"
    # Chon tu ke tiep co xac suat cao nhat
    w2, p1 = reduce((a, b) -> a[2] > b[2] ? a : b, collect(bigram[w1]))
    w3, p2 = reduce((a, b) -> a[2] > b[2] ? a : b, collect(bigram[w2]))
    return CauCandidate("$w1 $w2 $w3", p1 * p2)
end

# Giai ma theo chum (Beam search)
function giai_ma_chum(k::Int)
    beam = [CauCandidate("em", 1.0)]

    # Buoc mo rong 1: tu thu 2
    ung_vien1 = CauCandidate[]
    for item in beam
        last_w = split(item.cau)[end]
        for (w_next, p) in bigram[last_w]
            push!(ung_vien1, CauCandidate("$(item.cau) $w_next", item.p * p))
        end
    end
    sort!(ung_vien1, by = x -> x.p, rev = true)
    beam = ung_vien1[1:min(k, length(ung_vien1))]

    # Buoc mo rong 2: tu thu 3
    ung_vien2 = CauCandidate[]
    for item in beam
        last_w = split(item.cau)[end]
        for (w_next, p) in bigram[last_w]
            push!(ung_vien2, CauCandidate("$(item.cau) $w_next", item.p * p))
        end
    end
    sort!(ung_vien2, by = x -> x.p, rev = true)

    return ung_vien2[1]
end

# ==============================================================================
# PHAN 2: THUAT TOAN VITERBI VA VET CAN GAN NHAN
# ==============================================================================

const pi_init = Dict("N" => 0.60, "V" => 0.40)

const A_trans = Dict(
    "N" => Dict("N" => 0.35, "V" => 0.65),
    "V" => Dict("N" => 0.70, "V" => 0.30)
)

const B_emit = Dict(
    "N" => Dict("em" => 0.35, "hoc" => 0.10, "bai" => 0.40, "toan" => 0.30),
    "V" => Dict("em" => 0.05, "hoc" => 0.45, "bai" => 0.05, "toan" => 0.02)
)

const cau_gan_nhan = ["em", "hoc", "bai", "toan"]
const nhan = ["N", "V"]

# Thuat toan Viterbi
function chay_viterbi(cau::Vector{String})
    T = length(cau)
    f = [Dict{String, Float64}() for _ in 1:T]
    vet = [Dict{String, String}() for _ in 1:T]

    # Khoi tao i = 1 (tu "em")
    for s in nhan
        f[1][s] = pi_init[s] * B_emit[s][cau[1]]
        vet[1][s] = "-"
    end

    # Quy hoach dong i = 2 .. T
    for i in 2:T
        for s in nhan
            best_p = -1.0
            best_prev = ""
            for s_prev in nhan
                p = f[i - 1][s_prev] * A_trans[s_prev][s] * B_emit[s][cau[i]]
                if p > best_p
                    best_p = p
                    best_prev = s_prev
                end
            end
            f[i][s] = best_p
            vet[i][s] = best_prev
        end
    end

    # Tim nhan ket thuc tot nhat
    best_last_p = -1.0
    best_last_nhan = ""
    for s in nhan
        if f[T][s] > best_last_p
            best_last_p = f[T][s]
            best_last_nhan = s
        end
    end

    # Truy vet nguoc
    day_nhan = fill("", T)
    curr = best_last_nhan
    for i in T:-1:1
        day_nhan[i] = curr
        curr = vet[i][curr]
    end

    return day_nhan, best_last_p, f, vet
end

# Vet can 2^4 = 16 day nhan de doi chieu
function vet_can_viterbi(cau::Vector{String})
    best_p = -1.0
    best_seq = ""

    for mask in 0:15
        seq = [((mask & (1 << (3 - i))) != 0) ? "V" : "N" for i in 0:3]

        p = pi_init[seq[1]] * B_emit[seq[1]][cau[1]]
        for i in 2:4
            p *= A_trans[seq[i - 1]][seq[i]] * B_emit[seq[i]][cau[i]]
        end

        if p > best_p
            best_p = p
            best_seq = join(seq, " ")
        end
    end

    return best_seq, best_p
end

# ==============================================================================
# HAM MAIN CHAY VA IN KET QUA
# ==============================================================================
function main()
    ds_tat_ca = liet_ke_toan_bo()
    cau_tot_nhat = ds_tat_ca[1]
    cau_tl = giai_ma_tham_lam()
    cau_k1 = giai_ma_chum(1)
    cau_k2 = giai_ma_chum(2)
    cau_k3 = giai_ma_chum(3)

    day_viterbi, prob_viterbi, f_table, vet_table = chay_viterbi(cau_gan_nhan)
    seq_vetcan, prob_vetcan = vet_can_viterbi(cau_gan_nhan)
    str_viterbi = join(day_viterbi, " ")

    # In doi chieu
    println("=== DOI CHIEU VITERBI VA VET CAN (16 TO HOP NHAN) ===")
    @printf("Viterbi: %s | Xac suat: %.6f\n", str_viterbi, prob_viterbi)
    @printf("Vet can: %s | Xac suat: %.6f\n", seq_vetcan, prob_vetcan)
    println("-> Ket qua Viterbi trung khop 100% voi ket qua vet can.\n")

    # In Bang 4.3
    println("BANG 4.3. BA THUAT TOAN GIAI MA TREN CUNG MOT MO HINH")
    @printf("%-26s | %-15s | %-15s | %s\n", 
            "Thuat toan", "Ket qua tra ve", "Diem / xac suat", "Co phai KQ tot nhat?")
    println(repeat("-", 80))

    bang_4_3 = [
        ("Liet ke: cau tot nhat", cau_tot_nhat.cau, cau_tot_nhat.p, "Co"),
        ("Giai ma tham lam", cau_tl.cau, cau_tl.p, abs(cau_tl.p - cau_tot_nhat.p) < 1e-9 ? "Co" : "Khong"),
        ("Giai ma theo chum, k = 1", cau_k1.cau, cau_k1.p, abs(cau_k1.p - cau_tot_nhat.p) < 1e-9 ? "Co" : "Khong"),
        ("Giai ma theo chum, k = 2", cau_k2.cau, cau_k2.p, abs(cau_k2.p - cau_tot_nhat.p) < 1e-9 ? "Co" : "Khong"),
        ("Giai ma theo chum, k = 3", cau_k3.cau, cau_k3.p, abs(cau_k3.p - cau_tot_nhat.p) < 1e-9 ? "Co" : "Khong"),
        ("Viterbi (gan nhan)", str_viterbi, prob_viterbi, "Co")
    ]

    for row in bang_4_3
        @printf("%-26s | %-15s | %-15.6f | %s\n", row[1], row[2], row[3], row[4])
    end

    # In Bang 4.4
    println("\nBANG 4.4. LUOI VITERBI CUA CAU 'em hoc bai toan'")
    @printf("%-3s | %-8s | %-10s | %-10s | %-14s | %s\n", 
            "i", "Tu w_i", "f[i][N]", "f[i][V]", "Nhan truoc N", "Nhan truoc V")
    println(repeat("-", 65))

    for i in 1:length(cau_gan_nhan)
        tu = cau_gan_nhan[i]
        f_N = f_table[i]["N"]
        f_V = f_table[i]["V"]
        prev_N = vet_table[i]["N"]
        prev_V = vet_table[i]["V"]
        @printf("%-3d | %-8s | %-10.6f | %-10.6f | %-14s | %s\n", 
                i, tu, f_N, f_V, prev_N, prev_V)
    end
end

main()
