#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <cmath>
#include <iomanip>

using namespace std;

struct Mau {
    int id;
    vector<double> x;
    string y;
};

struct KetQuaSai {
    int id;
    string nhan_that;
    string nhan_du_doan;
};

double kc_euclid(const vector<double>& u, const vector<double>& v) {
    double sum = 0.0;
    for (size_t i = 0; i < u.size(); ++i) {
        double diff = u[i] - v[i];
        sum += diff * diff;
    }
    return sqrt(sum);
}

double kc_manhattan(const vector<double>& u, const vector<double>& v) {
    double sum = 0.0;
    for (size_t i = 0; i < u.size(); ++i) {
        sum += abs(u[i] - v[i]);
    }
    return sum;
}

vector<Mau> doc_du_lieu(const string& ten_tep, int& d) {
    ifstream fin(ten_tep);
    if (!fin.is_open()) fin.open("../../data/" + ten_tep);
    if (!fin.is_open()) fin.open("data/" + ten_tep);
    if (!fin.is_open()) {
        cerr << "Loi: Khong the mo tep " << ten_tep << "\n";
        exit(1);
    }
    int n;
    fin >> n >> d;
    vector<Mau> D(n);
    for (int i = 0; i < n; ++i) {
        D[i].id = i + 1;
        D[i].x.resize(d);
        for (int j = 0; j < d; ++j) fin >> D[i].x[j];
        fin >> D[i].y;
    }
    return D;
}

double do_chinh_xac_bo_mot_mau(const vector<Mau>& D, 
                              double (*kc)(const vector<double>&, const vector<double>&),
                              vector<KetQuaSai>& ds_sai) {
    int n = D.size();
    int so_dung = 0;
    ds_sai.clear();

    for (int i = 0; i < n; ++i) {
        double min_dist = 1e18;
        string best_nhan = "";

        for (int j = 0; j < n; ++j) {
            if (i == j) continue;
            double dist = kc(D[i].x, D[j].x);
            if (dist < min_dist) {
                min_dist = dist;
                best_nhan = D[j].y;
            }
        }

        if (best_nhan == D[i].y) {
            so_dung++;
        } else {
            ds_sai.push_back({D[i].id, D[i].y, best_nhan});
        }
    }
    return (double)so_dung / n;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int d;
    vector<Mau> D = doc_du_lieu("hoa30.txt", d);
    int n = D.size();

    vector<KetQuaSai> ds_sai_e, ds_sai_m;
    double acc_e = do_chinh_xac_bo_mot_mau(D, kc_euclid, ds_sai_e);
    double acc_m = do_chinh_xac_bo_mot_mau(D, kc_manhattan, ds_sai_m);

    cout << "Euclid: " << (int)(acc_e * n + 0.5) << "/" << n << " = " 
         << fixed << setprecision(2) << acc_e * 100 << "%";
    if (ds_sai_e.empty()) cout << " - khong mau nao sai\n";
    else cout << "\n";

    cout << "Manhattan: " << (int)(acc_m * n + 0.5) << "/" << n << " = " 
         << fixed << setprecision(2) << acc_m * 100 << "%";
    if (!ds_sai_m.empty()) {
        cout << " - sai mau " << ds_sai_m[0].id << " (that: " 
             << ds_sai_m[0].nhan_that << ", du doan: " << ds_sai_m[0].nhan_du_doan << ")\n";
    } else cout << "\n";

    return 0;
}
