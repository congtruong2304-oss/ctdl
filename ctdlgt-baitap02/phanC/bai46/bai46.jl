using Printf

khoang_cach(u, v) = sqrt(sum((u .- v) .^ 2))

function lang_gieng_gan_nhat(q, D)
    min_dist = Inf
    best_label = ""
    best_idx = -1

    for i in 1:length(D)
        dist = khoang_cach(q, D[i][:x])
        if dist < min_dist
            min_dist = dist
            best_label = D[i][:y]
            best_idx = i
        end
    end
    return (best_label, min_dist, best_idx)
end

function main()
    D = [
        (x = [1.4, 0.2], y = "Setosa"),
        (x = [1.3, 0.2], y = "Setosa"),
        (x = [1.5, 0.2], y = "Setosa"),
        (x = [4.7, 1.4], y = "Versicolor"),
        (x = [4.5, 1.5], y = "Versicolor"),
        (x = [4.9, 1.5], y = "Versicolor"),
        (x = [6.0, 2.5], y = "Virginica"),
        (x = [5.8, 2.1], y = "Virginica")
    ]

    input_str = read(stdin, String)
    tokens = split(input_str)
    if isempty(tokens) return end

    idx = 1
    while idx <= length(tokens)
        q = [parse(Float64, tokens[idx]), parse(Float64, tokens[idx + 1])]
        idx += 2
        nhan, dist, chi_so = lang_gieng_gan_nhat(q, D)
        if dist < 1e-9
            println("$(nhan) — trung dung mau $(chi_so), khoang cach 0")
        else
            if abs(dist - round(dist, digits=1)) < 1e-5
                @printf("%s — lang gieng la mau %d, khoang cach %.1f\n", nhan, chi_so, dist)
            else
                @printf("%s — lang gieng la mau %d, khoang cach %.4f\n", nhan, chi_so, dist)
            end
        end
    end
end

main()
