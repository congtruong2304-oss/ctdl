function chuan_hoa(X)
    n, m = size(X)
    cmin = [minimum(X[:, j]) for j in 1:m]
    cmax = [maximum(X[:, j]) for j in 1:m]
    Z = similar(X, Float64)
    for j in 1:m
        khoang = cmax[j] - cmin[j]
        for i in 1:n
            Z[i, j] = khoang == 0 ? 0.0 : (X[i, j] - cmin[j]) / khoang
        end
    end
    return Z, cmin, cmax
end

khoang_cach(u, v) = sqrt(sum((u .- v) .^ 2))

function k_lang_gieng(Z, y, z_moi, k)
    n = size(Z, 1)
    d = [khoang_cach(Z[i, :], z_moi) for i in 1:n]
    
    # Dung sortperm de sap xep mang chi so theo khoang cach tang dan
    thu_tu = sortperm(d)
    
    phieu = Dict{String, Int}()
    for i in thu_tu[1:k]
        phieu[y[i]] = get(phieu, y[i], 0) + 1
    end
    return argmax(phieu)
end

# Du lieu huan luyen
X = [
    2.0 300.0;
    3.0 450.0;
    4.0 600.0;
    15.0 1800.0;
    16.0 2000.0;
    18.0 2400.0;
    5.0 2200.0;
    17.0 700.0
]
y = ["chua dat", "chua dat", "chua dat", "dat", "dat", "dat", "chua dat", "dat"]

Z, cmin, cmax = chuan_hoa(X)

x_moi = [14.0, 800.0]
z_moi = (x_moi .- cmin) ./ (cmax .- cmin)

k = 3
ket_qua = k_lang_gieng(Z, y, z_moi, k)
println("Du doan cho mau (14, 800) voi K=", k, ": ", ket_qua)
