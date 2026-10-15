# bai4.2.py - Chon hoat dong: bon tieu chi tham lam va giai thuat toi uu

def ket_thuc_som_nhat(ds):
    # Sap xep theo thoi gian ket thuc f_i
    ds_sorted = sorted(ds, key=lambda x: x['f'])
    chon = []
    last_f = -1
    for h in ds_sorted:
        if h['s'] >= last_f:
            chon.append(h['ten'])
            last_f = h['f']
    return chon

def bat_dau_som_nhat(ds):
    # Sap xep theo thoi gian bat dau s_i
    ds_sorted = sorted(ds, key=lambda x: x['s'])
    chon = []
    last_f = -1
    for h in ds_sorted:
        if h['s'] >= last_f:
            chon.append(h['ten'])
            last_f = h['f']
    return chon

def ngan_nhat(ds):
    # Chon lap: luon lay hoat dong co do dai ngan nhat tuong thich
    con_lai = sorted(ds, key=lambda x: (x['f'] - x['s'], x['s']))
    chon = []
    for h in con_lai:
        # Kiem tra tuong thich voi cac hoat dong da chon
        tuong_thich = True
        for c in chon:
            c_item = next(item for item in ds if item['ten'] == c)
            if not (h['f'] <= c_item['s'] or h['s'] >= c_item['f']):
                tuong_thich = False
                break
        if tuong_thich:
            chon.append(h['ten'])
    return sorted(chon, key=lambda x: int(x[1:]))

def it_chong_lan_nhat(ds):
    con_lai = list(ds)
    chon = []
    while con_lai:
        # Tinh so xung dot voi cac hoat dong con lai
        min_overlap = float('inf')
        best_h = None
        for h in con_lai:
            cnt = sum(1 for o in con_lai if o != h and not (h['f'] <= o['s'] or h['s'] >= o['f']))
            if cnt < min_overlap:
                min_overlap = cnt
                best_h = h
        chon.append(best_h['ten'])
        # Loai bo cac hoat dong xung dot voi best_h
        con_lai = [o for o in con_lai if (o['f'] <= best_h['s'] or o['s'] >= best_h['f'])]
    return sorted(chon, key=lambda x: int(x[1:]))

def toi_uu_vet_can(ds):
    # Quy hoach dong / Vet can tim so hoat dong nhieu nhat that su
    n = len(ds)
    best_set = []
    for mask in range(1 << n):
        sub = [ds[i] for i in range(n) if (mask & (1 << i))]
        # Kiem tra tuong thich tung doi mot
        ok = True
        for i in range(len(sub)):
            for j in range(i + 1, len(sub)):
                if not (sub[i]['f'] <= sub[j]['s'] or sub[j]['f'] <= sub[i]['s']):
                    ok = False
                    break
            if not ok:
                break
        if ok and len(sub) > len(best_set):
            best_set = [h['ten'] for h in sub]
    return sorted(best_set, key=lambda x: int(x[1:]))

def main():
    # Du lieu Muc C
    data = [
        {"ten": "H1",  "s": 1,  "f": 5},
        {"ten": "H2",  "s": 2,  "f": 5},
        {"ten": "H3",  "s": 2,  "f": 6},
        {"ten": "H4",  "s": 3,  "f": 4},
        {"ten": "H5",  "s": 4,  "f": 8},
        {"ten": "H6",  "s": 6,  "f": 9},
        {"ten": "H7",  "s": 8,  "f": 11},
        {"ten": "H8",  "s": 9,  "f": 14},
        {"ten": "H9",  "s": 11, "f": 13},
        {"ten": "H10", "s": 12, "f": 15},
    ]

    opt = toi_uu_vet_can(data)
    max_count = len(opt)

    kq_kt = ket_thuc_som_nhat(data)
    kq_bd = bat_dau_som_nhat(data)
    kq_nn = ngan_nhat(data)
    kq_cl = it_chong_lan_nhat(data)

    tieuchi = [
        ("Ket thuc som nhat", kq_kt),
        ("Bat dau som nhat", kq_bd),
        ("Ngan nhat", kq_nn),
        ("It chong lan nhat", kq_cl),
        ("So nhieu nhat that su", opt),
    ]

    print(f"{'Tieu chi':<22} | {'Cac hoat dong duoc chon':<20} | {'So HD':<6} | {'Co dat toi uu khong?'}")
    print("-" * 75)
    for tc, ds_chon in tieuchi:
        so_hd = len(ds_chon)
        str_hd = ", ".join(ds_chon)
        if tc == "So nhieu nhat that su":
            dat = "—"
        else:
            dat = "Co" if so_hd == max_count else "Khong"
        print(f"{tc:<22} | {str_hd:<20} | {so_hd:<6} | {dat}")

if __name__ == "__main__":
    main()
