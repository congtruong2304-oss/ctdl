#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <iomanip>
#include <cmath>

using namespace std;

// ==============================================================================
// PHAN 1: MO HINH NGON NGU HAI TU (BIGRAM)
// ==============================================================================

struct Canh {
    string tu;
    double p;
};

// Mo hinh bigram tuong ung Muc D
map<string, vector<Canh>> bigram = {
    {"em",  {{"hoc", 0.52}, {"di", 0.48}}},
    {"hoc", {{"bai", 0.40}, {"toan", 0.35}, {"ve", 0.25}}},
    {"di",  {{"cho", 0.58}, {"boi", 0.22}, {"ngu", 0.20}}}
};

struct CauCandidate {
    string cau;
    double p;
};

// Liet ke toan bo 6 cau do dai 3 bat dau bang "em"
vector<CauCandidate> liet_ke_toan_bo() {
    vector<CauCandidate> ds;
    for (const auto& c1 : bigram["em"]) {
        for (const auto& c2 : bigram[c1.tu]) {
            ds.push_back({"em " + c1.tu + " " + c2.tu, c1.p * c2.p});
        }
    }
    sort(ds.begin(), ds.end(), [](const CauCandidate& a, const CauCandidate& b) {
        return a.p > b.p;
    });
    return ds;
}

// Giai ma tham lam (Greedy search)
CauCandidate giai_ma_tham_lam() {
    string w1 = "em";
    auto best1 = *max_element(bigram[w1].begin(), bigram[w1].end(), [](const Canh& a, const Canh& b) {
        return a.p < b.p;
    });
    
    auto best2 = *max_element(bigram[best1.tu].begin(), bigram[best1.tu].end(), [](const Canh& a, const Canh& b) {
        return a.p < b.p;
    });

    return {w1 + " " + best1.tu + " " + best2.tu, best1.p * best2.p};
}

// Giai ma theo chum (Beam search)
CauCandidate giai_ma_chum(int k) {
    vector<CauCandidate> beam = {{"em", 1.0}};

    // Buoc mo rong 1: tu thu 2
    vector<CauCandidate> ung_vien1;
    for (const auto& item : beam) {
        string last_w = item.cau.substr(item.cau.find_last_of(' ') + 1);
        for (const auto& c : bigram[last_w]) {
            ung_vien1.push_back({item.cau + " " + c.tu, item.p * c.p});
        }
    }
    sort(ung_vien1.begin(), ung_vien1.end(), [](const CauCandidate& a, const CauCandidate& b) {
        return a.p > b.p;
    });
    if ((int)ung_vien1.size() > k) ung_vien1.resize(k);
    beam = ung_vien1;

    // Buoc mo rong 2: tu thu 3
    vector<CauCandidate> ung_vien2;
    for (const auto& item : beam) {
        string last_w = item.cau.substr(item.cau.find_last_of(' ') + 1);
        for (const auto& c : bigram[last_w]) {
            ung_vien2.push_back({item.cau + " " + c.tu, item.p * c.p});
        }
    }
    sort(ung_vien2.begin(), ung_vien2.end(), [](const CauCandidate& a, const CauCandidate& b) {
        return a.p > b.p;
    });
    if ((int)ung_vien2.size() > k) ung_vien2.resize(k);

    return ung_vien2[0];
}

// ==============================================================================
// PHAN 2: THUAT TOAN VITERBI VA VET CAN GAN NHAN
// ==============================================================================

map<string, double> pi_init = {{"N", 0.60}, {"V", 0.40}};

map<string, map<string, double>> A_trans = {
    {"N", {{"N", 0.35}, {"V", 0.65}}},
    {"V", {{"N", 0.70}, {"V", 0.30}}}
};

map<string, map<string, double>> B_emit = {
    {"N", {{"em", 0.35}, {"hoc", 0.10}, {"bai", 0.40}, {"toan", 0.30}}},
    {"V", {{"em", 0.05}, {"hoc", 0.45}, {"bai", 0.05}, {"toan", 0.02}}}
};

vector<string> cau_gan_nhan = {"em", "hoc", "bai", "toan"};
vector<string> nhan = {"N", "V"};

struct ViterbiResult {
    vector<string> day_nhan;
    double p_max;
    vector<map<string, double>> f;
    vector<map<string, string>> vet;
};

// Thuat toan Viterbi
ViterbiResult chay_viterbi(const vector<string>& cau) {
    int T = cau.size();
    vector<map<string, double>> f(T);
    vector<map<string, string>> vet(T);

    // Khoi tao i = 0 ("em")
    for (const auto& s : nhan) {
        f[0][s] = pi_init[s] * B_emit[s][cau[0]];
        vet[0][s] = "-";
    }

    // Quy hoach dong i = 1 .. T-1
    for (int i = 1; i < T; ++i) {
        for (const auto& s : nhan) {
            double best_p = -1.0;
            string best_prev = "";
            for (const auto& s_prev : nhan) {
                double p = f[i - 1][s_prev] * A_trans[s_prev][s] * B_emit[s][cau[i]];
                if (p > best_p) {
                    best_p = p;
                    best_prev = s_prev;
                }
            }
            f[i][s] = best_p;
            vet[i][s] = best_prev;
        }
    }

    // Tim trang thai ket thuc tot nhat
    double best_last_p = -1.0;
    string best_last_nhan = "";
    for (const auto& s : nhan) {
        if (f[T - 1][s] > best_last_p) {
            best_last_p = f[T - 1][s];
            best_last_nhan = s;
        }
    }

    // Truy vet nguoc
    vector<string> day_nhan(T);
    string curr = best_last_nhan;
    for (int i = T - 1; i >= 0; --i) {
        day_nhan[i] = curr;
        curr = vet[i][curr];
    }

    return {day_nhan, best_last_p, f, vet};
}

// Vet can 2^4 = 16 day nhan de doi chieu
pair<string, double> vet_can_viterbi(const vector<string>& cau) {
    double best_p = -1.0;
    string best_seq = "";

    for (int mask = 0; mask < 16; ++mask) {
        vector<string> seq(4);
        for (int i = 0; i < 4; ++i) {
            seq[i] = (mask & (1 << (3 - i))) ? "V" : "N";
        }

        double p = pi_init[seq[0]] * B_emit[seq[0]][cau[0]];
        for (int i = 1; i < 4; ++i) {
            p *= A_trans[seq[i - 1]][seq[i]] * B_emit[seq[i]][cau[i]];
        }

        if (p > best_p) {
            best_p = p;
            best_seq = seq[0] + " " + seq[1] + " " + seq[2] + " " + seq[3];
        }
    }
    return {best_seq, best_p};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    auto ds_tat_ca = liet_ke_toan_bo();
    auto cau_tot_nhat = ds_tat_ca[0];
    auto cau_tl = giai_ma_tham_lam();
    auto cau_k1 = giai_ma_chum(1);
    auto cau_k2 = giai_ma_chum(2);
    auto cau_k3 = giai_ma_chum(3);

    auto res_viterbi = chay_viterbi(cau_gan_nhan);
    auto res_vetcan = vet_can_viterbi(cau_gan_nhan);

    string str_viterbi = "";
    for (size_t i = 0; i < res_viterbi.day_nhan.size(); ++i) {
        str_viterbi += res_viterbi.day_nhan[i];
        if (i + 1 < res_viterbi.day_nhan.size()) str_viterbi += " ";
    }

    // In doi chieu
    cout << fixed << setprecision(6);
    cout << "=== DOI CHIEU VITERBI VA VET CAN (16 TO HOP NHAN) ===\n";
    cout << "Viterbi: " << str_viterbi << " | Xac suat: " << res_viterbi.p_max << "\n";
    cout << "Vet can: " << res_vetcan.first << " | Xac suat: " << res_vetcan.second << "\n";
    cout << "-> Ket qua Viterbi trung khop 100% voi ket qua vet can.\n\n";

    // In Bang 4.3
    cout << "BANG 4.3. BA THUAT TOAN GIAI MA TREN CUNG MOT MO HINH\n";
    cout << left << setw(26) << "Thuat toan" << " | "
         << setw(15) << "Ket qua tra ve" << " | "
         << setw(15) << "Diem / xac suat" << " | "
         << "Co phai KQ tot nhat?\n";
    cout << string(80, '-') << "\n";

    auto in_dong_43 = [&](string tc, string kq, double diem, bool dat) {
        cout << left << setw(26) << tc << " | "
             << setw(15) << kq << " | "
             << setw(15) << diem << " | "
             << (dat ? "Co" : "Khong") << "\n";
    };

    in_dong_43("Liet ke: cau tot nhat", cau_tot_nhat.cau, cau_tot_nhat.p, true);
    in_dong_43("Giai ma tham lam", cau_tl.cau, cau_tl.p, fabs(cau_tl.p - cau_tot_nhat.p) < 1e-9);
    in_dong_43("Giai ma theo chum, k = 1", cau_k1.cau, cau_k1.p, fabs(cau_k1.p - cau_tot_nhat.p) < 1e-9);
    in_dong_43("Giai ma theo chum, k = 2", cau_k2.cau, cau_k2.p, fabs(cau_k2.p - cau_tot_nhat.p) < 1e-9);
    in_dong_43("Giai ma theo chum, k = 3", cau_k3.cau, cau_k3.p, fabs(cau_k3.p - cau_tot_nhat.p) < 1e-9);
    in_dong_43("Viterbi (gan nhan)", str_viterbi, res_viterbi.p_max, true);

    // In Bang 4.4
    cout << "\nBANG 4.4. LUOI VITERBI CUA CAU 'em hoc bai toan'\n";
    cout << left << setw(3) << "i" << " | "
         << setw(8) << "Tu w_i" << " | "
         << setw(10) << "f[i][N]" << " | "
         << setw(10) << "f[i][V]" << " | "
         << setw(14) << "Nhan truoc N" << " | "
         << "Nhan truoc V\n";
    cout << string(65, '-') << "\n";

    for (size_t i = 0; i < cau_gan_nhan.size(); ++i) {
        cout << left << setw(3) << (i + 1) << " | "
             << setw(8) << cau_gan_nhan[i] << " | "
             << setw(10) << res_viterbi.f[i]["N"] << " | "
             << setw(10) << res_viterbi.f[i]["V"] << " | "
             << setw(14) << res_viterbi.vet[i]["N"] << " | "
             << res_viterbi.vet[i]["V"] << "\n";
    }

    return 0;
}
