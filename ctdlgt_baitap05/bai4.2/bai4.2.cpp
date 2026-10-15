#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iomanip>

using namespace std;

struct HoatDong {
    string ten;
    int s;
    int f;
};

// Kiem tra 2 hoat dong co tuong thich (khong chong lan) hay khong
// Chiếm nua khoang [s, f), tuong thich khi f1 <= s2 hoac f2 <= s1
bool tuong_thich(const HoatDong& a, const HoatDong& b) {
    return (a.f <= b.s) || (b.f <= a.s);
}

// 1. Tieu chi Ket thuc som nhat
vector<string> ket_thuc_som_nhat(vector<HoatDong> ds) {
    sort(ds.begin(), ds.end(), [](const HoatDong& a, const HoatDong& b) {
        return a.f < b.f;
    });

    vector<string> chon;
    int last_f = -1;
    for (const auto& h : ds) {
        if (h.s >= last_f) {
            chon.push_back(h.ten);
            last_f = h.f;
        }
    }
    return chon;
}

// 2. Tieu chi Bat dau som nhat
vector<string> bat_dau_som_nhat(vector<HoatDong> ds) {
    sort(ds.begin(), ds.end(), [](const HoatDong& a, const HoatDong& b) {
        return a.s < b.s;
    });

    vector<string> chon;
    int last_f = -1;
    for (const auto& h : ds) {
        if (h.s >= last_f) {
            chon.push_back(h.ten);
            last_f = h.f;
        }
    }
    return chon;
}

// 3. Tieu chi Ngan nhat
vector<string> ngan_nhat(vector<HoatDong> ds) {
    sort(ds.begin(), ds.end(), [](const HoatDong& a, const HoatDong& b) {
        int len_a = a.f - a.s;
        int len_b = b.f - b.s;
        if (len_a != len_b) return len_a < len_b;
        return a.s < b.s;
    });

    vector<HoatDong> da_chon;
    for (const auto& h : ds) {
        bool ok = true;
        for (const auto& c : da_chon) {
            if (!tuong_thich(h, c)) {
                ok = false;
                break;
            }
        }
        if (ok) {
            da_chon.push_back(h);
        }
    }

    vector<string> res;
    for (const auto& h : da_chon) res.push_back(h.ten);
    // Sap xep lai thu tu ten H1..H10
    sort(res.begin(), res.end(), [](const string& a, const string& b) {
        return stoi(a.substr(1)) < stoi(b.substr(1));
    });
    return res;
}

// 4. Tieu chi It chong lan nhat (cai dat logic lap khop theo ban Python)
vector<string> it_chong_lan_nhat(vector<HoatDong> ds) {
    vector<HoatDong> con_lai = ds;
    vector<string> chon;

    while (!con_lai.empty()) {
        int min_overlap = 1e9;
        int best_idx = -1;

        for (int i = 0; i < (int)con_lai.size(); ++i) {
            int cnt = 0;
            for (int j = 0; j < (int)con_lai.size(); ++j) {
                if (i != j && !tuong_thich(con_lai[i], con_lai[j])) {
                    cnt++;
                }
            }
            if (cnt < min_overlap) {
                min_overlap = cnt;
                best_idx = i;
            }
        }

        HoatDong best_h = con_lai[best_idx];
        chon.push_back(best_h.ten);

        // Loc lai cac hoat dong con lai tuong thich voi best_h
        vector<HoatDong> tiep_theo;
        for (const auto& o : con_lai) {
            if (tuong_thich(best_h, o)) {
                tiep_theo.push_back(o);
            }
        }
        con_lai = tiep_theo;
    }

    sort(chon.begin(), chon.end(), [](const string& a, const string& b) {
        return stoi(a.substr(1)) < stoi(b.substr(1));
    });
    return chon;
}

// Tim so hoat dong nhieu nhat that su (Vet can tap con)
vector<string> toi_uu_vet_can(const vector<HoatDong>& ds) {
    int n = ds.size();
    vector<string> best_set;

    for (int mask = 0; mask < (1 << n); ++mask) {
        vector<HoatDong> sub;
        for (int i = 0; i < n; ++i) {
            if (mask & (1 << i)) {
                sub.push_back(ds[i]);
            }
        }

        bool ok = true;
        for (size_t i = 0; i < sub.size(); ++i) {
            for (size_t j = i + 1; j < sub.size(); ++j) {
                if (!tuong_thich(sub[i], sub[j])) {
                    ok = false;
                    break;
                }
            }
            if (!ok) break;
        }

        if (ok && sub.size() > best_set.size()) {
            best_set.clear();
            for (const auto& h : sub) best_set.push_back(h.ten);
        }
    }

    sort(best_set.begin(), best_set.end(), [](const string& a, const string& b) {
        return stoi(a.substr(1)) < stoi(b.substr(1));
    });
    return best_set;
}

string format_list(const vector<string>& list) {
    string res = "";
    for (size_t i = 0; i < list.size(); ++i) {
        res += list[i];
        if (i + 1 < list.size()) res += ", ";
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // Muoi hoat dong o Muc C
    vector<HoatDong> data = {
        {"H1", 1, 5},
        {"H2", 2, 5},
        {"H3", 2, 6},
        {"H4", 3, 4},
        {"H5", 4, 8},
        {"H6", 6, 9},
        {"H7", 8, 11},
        {"H8", 9, 14},
        {"H9", 11, 13},
        {"H10", 12, 15}
    };

    auto opt = toi_uu_vet_can(data);
    int max_count = opt.size();

    auto kq_kt = ket_thuc_som_nhat(data);
    auto kq_bd = bat_dau_som_nhat(data);
    auto kq_nn = ngan_nhat(data);
    auto kq_cl = it_chong_lan_nhat(data);

    vector<pair<string, vector<string>>> tieuchi = {
        {"Ket thuc som nhat", kq_kt},
        {"Bat dau som nhat", kq_bd},
        {"Ngan nhat", kq_nn},
        {"It chong lan nhat", kq_cl},
        {"So nhieu nhat that su", opt}
    };

    cout << left << setw(22) << "Tieu chi" << " | "
         << setw(20) << "Cac hoat dong duoc chon" << " | "
         << setw(6)  << "So HD" << " | "
         << "Co dat toi uu khong?\n";
    cout << string(75, '-') << "\n";

    for (const auto& tc : tieuchi) {
        int so_hd = tc.second.size();
        string str_hd = format_list(tc.second);
        string dat = (tc.first == "So nhieu nhat that su") ? "-" : ((so_hd == max_count) ? "Co" : "Khong");

        cout << left << setw(22) << tc.first << " | "
             << setw(20) << str_hd << " | "
             << setw(6)  << so_hd << " | "
             << dat << "\n";
    }

    return 0;
}
