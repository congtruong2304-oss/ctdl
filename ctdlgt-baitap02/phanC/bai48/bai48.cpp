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

struct KetQua {
    string nhan;
    double kc;
    int id_lang_gieng;
};

// Khoang cach Euclid
double kc_euclid(const vector<double>& u, const vector<double>& v) {
    double sum = 0.0;
    for (size_t i = 0; i < u.size(); ++i) {
        double diff = u[i] - v[i];
        sum += diff * diff;
    }
    return sqrt(sum);
}

// Khoang cach Manhattan
double kc_manhattan(const vector<double>& u, const vector<double>& v) {
    double sum = 0.0;
    for (size_t i = 0; i < u.size(); ++i) {
        sum += abs(u[i] - v[i]);
    }
    return sum;
}

// Doc du lieu tu tep van ban ho tro duong dan du phong
vector<Mau> doc_du_lieu(const string& ten_tep, int& d) {
    ifstream fin(ten_tep);
    if (!fin.is_open()) {
        fin.open("../../data/" + ten_tep);
        if (!fin.is_open()) fin.open("data/" + ten_tep);
    }
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
        for (int j = 0; j < d; ++j) {
            fin >> D[i].x[j];
        }
        fin >> D[i].y;
    }
    return D;
}

// 1-NN truyen ham khoang cach va chi so bo qua (phuc vu LOO)
KetQua lang_gieng_gan_nhat(const vector<double>& q, const vector<Mau>& D,
                           double (*kc)(const vector<double>&, const vector<double>&),
                           int bo_qua_id = -1) {
    double min_dist = 1e18;
    KetQua res = {"", 0.0, -1};

    for (const auto& m : D) {
        if (m.id == bo_qua_id) continue;
        double dist = kc(q, m.x);
        if (dist < min_dist) {
            min_dist = dist;
            res = {m.y, dist, m.id};
        }
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int d;
    vector<Mau> D = doc_du_lieu("hoa30.txt", d);

    // 1. Kiem tra mau moi (6.5, 3.0, 5.5, 2.0)
    vector<double> q = {6.5, 3.0, 5.5, 2.0};
    KetQua res_e = lang_gieng_gan_nhat(q, D, kc_euclid);
    KetQua res_m = lang_gieng_gan_nhat(q, D, kc_manhattan);

    cout << "Mau [6.5, 3.0, 5.5, 2.0]:\n";
    cout << "  Euclid:    " << res_e.nhan << " (mau " << res_e.id_lang_gieng << ", kc " << fixed << setprecision(4) << res_e.kc << ")\n";
    cout << "  Manhattan: " << res_m.nhan << " (mau " << res_m.id_lang_gieng << ", kc " << fixed << setprecision(4) << res_m.kc << ")\n";

    // 2. Danh gia Leave-One-Out
    int dung_e = 0, dung_m = 0;
    int n = D.size();
    for (int i = 0; i < n; ++i) {
        KetQua ke = lang_gieng_gan_nhat(D[i].x, D, kc_euclid, D[i].id);
        KetQua km = lang_gieng_gan_nhat(D[i].x, D, kc_manhattan, D[i].id);
        if (ke.nhan == D[i].y) dung_e++;
        if (km.nhan == D[i].y) dung_m++;
        if (D[i].id == 26) {
            cout << "Mau 26 bi bo ra:\n";
            cout << "  Manhattan du doan: " << km.nhan << " (mau " << km.id_lang_gieng << ", kc " << fixed << setprecision(1) << km.kc << ")\n";
        }
    }

    cout << "Do chinh xac LOO:\n";
    cout << "  Euclid:    " << dung_e << "/" << n << " = " << fixed << setprecision(2) << (dung_e * 100.0 / n) << "%\n";
    cout << "  Manhattan: " << dung_m << "/" << n << " = " << fixed << setprecision(2) << (dung_m * 100.0 / n) << "%\n";

    return 0;
}
