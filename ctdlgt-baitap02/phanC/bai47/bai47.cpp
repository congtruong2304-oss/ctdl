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
    double khoang_cach;
    int id_lang_gieng;
};

// Khoang cach Euclid giua hai vector d chieu
double khoang_cach(const vector<double>& u, const vector<double>& v) {
    double d2 = 0.0;
    for (size_t i = 0; i < u.size(); ++i) {
        double diff = u[i] - v[i];
        d2 += diff * diff;
    }
    return sqrt(d2);
}

// Doc du lieu tu tep van ban voi so dac trung d tuy y
vector<Mau> doc_du_lieu(const string& ten_tep, int &d) {
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

// Phan loai 1-NN cho vector q co so chieu tuy y
KetQua lang_gieng_gan_nhat(const vector<double>& q, const vector<Mau>& D) {
    double min_dist = 1e18;
    KetQua res = {"", 0.0, -1};

    for (const auto& m : D) {
        double dist = khoang_cach(q, m.x);
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

    double v;
    while (cin >> v) {
        vector<double> q(d);
        q[0] = v;
        for (int i = 1; i < d; ++i) {
            cin >> q[i];
        }

        KetQua ans = lang_gieng_gan_nhat(q, D);
        cout << ans.nhan << " — mau " << ans.id_lang_gieng << ", khoang cach " 
             << fixed << setprecision(4) << ans.khoang_cach << "\n";
    }
    return 0;
}
