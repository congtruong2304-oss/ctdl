struct DoVat
    ten::String
    w::Int
    v::Int
    don_gia::Float64
end

function tinh_can_tren(i, w_con_lai, v_hien_tai, ds, n)
    can = Float64(v_hien_tai)
    w_tam = w_con_lai
    for k in i:n
        if ds[k].w <= w_tam
            w_tam -= ds[k].w
            can += ds[k].v
        else
            can += ds[k].don_gia * w_tam
            break
        end
    end
    return can
end

function giai_cai_tui(ds, W; co_cat_nhanh=true)
    n = length(ds)
    so_nut = 0
    max_val = 0
    best_chon = zeros(Int, n)
    x = zeros(Int, n)

    function quay_lui(i, w_hien_tai, v_hien_tai)
        so_nut += 1

        if v_hien_tai > max_val
            max_val = v_hien_tai
            best_chon = copy(x)
        end

        if i > n
            return
        end

        # Nhánh 1: CHỌN vật i (x[i] = 1) - chỉ số từ 1..n
        if w_hien_tai + ds[i].w <= W
            x[i] = 1
            quay_lui(i + 1, w_hien_tai + ds[i].w, v_hien_tai + ds[i].v)
            x[i] = 0 # Hoàn tác
        end

        # Nhánh 2: KHÔNG CHỌN vật i (x[i] = 0)
        x[i] = 0
        w_con_lai = W - w_hien_tai
        if co_cat_nhanh
            ub = tinh_can_tren(i + 1, w_con_lai, v_hien_tai, ds, n)
            if ub > max_val
                quay_lui(i + 1, w_hien_tai, v_hien_tai)
            end
        else
            quay_lui(i + 1, w_hien_tai, v_hien_tai)
        end
    end

    quay_lui(1, 0, 0) # Bắt đầu từ mức i = 1
    return max_val, best_chon, so_nut
end

function main()
    W = 14

    # Bộ 6 đồ vật mục C
    ds_goc = [
        DoVat("A", 4, 12, 12.0 / 4),
        DoVat("B", 7, 25, 25.0 / 7),
        DoVat("C", 3, 7, 7.0 / 3),
        DoVat("D", 3, 8, 8.0 / 3),
        DoVat("E", 3, 9, 9.0 / 3),
        DoVat("F", 10, 21, 21.0 / 10)
    ]

    # Sắp xếp đồ vật theo tỉ số v/w giảm dần
    ds = sort(ds_goc, by = x -> x.don_gia, rev = true)

    println("=== THỨ TỰ ĐỒ VẬT SAU KHI SẮP XẾP THEO v/w GIẢM DẦN ===")
    for (idx, item) in enumerate(ds)
        println("$(idx). Vật $(item.ten): w = $(item.w), v = $(item.v), v/w = $(round(item.don_gia, digits=3))")
    end

    # Chạy chế độ 1: CÓ cắt nhánh
    max_val_cat, best_chon_cat, nut_cat = giai_cai_tui(ds, W, co_cat_nhanh=true)

    # Chạy chế độ 2: KHÔNG cắt nhánh
    max_val_khong, _, nut_khong = giai_cai_tui(ds, W, co_cat_nhanh=false)

    println("\n" * "="^50)
    println("Sức chứa W = ", W)
    println("Giá trị lớn nhất: ", max_val_cat)

    tap_vat = [ds[i].ten for i in 1:length(ds) if best_chon_cat[i] == 1]
    tong_w = sum(ds[i].w for i in 1:length(ds) if best_chon_cat[i] == 1)
    println("Tập đồ vật được chọn: ", tap_vat, " (Tổng w = $(tong_w))")
    println("Số nút khi CÓ cắt nhánh: ", nut_cat)
    println("Số nút khi KHÔNG cắt nhánh: ", nut_khong)
    println("Số nút giảm được: ", round(nut_khong / nut_cat, digits=2), " lần")
end

main()
