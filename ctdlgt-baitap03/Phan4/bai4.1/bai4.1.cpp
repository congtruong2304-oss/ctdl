#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>

using namespace std;

struct Mau {
    vector<double> x;
    string y;
};

double khoang_cach(const vector<double> &u, const vector<double> &v) {
    double s = 0;
    for (size_t j = 0; j < u.size(); j++) {
        s += (u[j] - v[j]) * (u[j] - v[j]);
    }
    return sqrt(s);
}

void chuan_hoa(vector<Mau> &D, vector<double> &cmin, vector<double> &cmax) {
    int m = D[0].x.size();
    cmin.assign(m, 1e18);
    cmax.assign(m, -1e18);
    for (const auto &mau : D) {
        for (int j = 0; j < m; j++) {
            cmin[j] = min(cmin[j], mau.x[j]);
            cmax[j] = max(cmax[j], mau.x[j]);
        }
    }
    for (auto &mau : D) {
        for (int j = 0; j < m; j++) {
            double khoang = cmax[j] - cmin[j];
            mau.x[j] = (khoang == 0) ? 0.0 : (mau.x[j] - cmin[j]) / khoang;
        }
    }
}

string k_lang_gieng(const vector<Mau> &D, const vector<double> &z, int k) {
    vector<pair<double, string>> d;
    for (const auto &mau : D) {
        d.push_back({khoang_cach(mau.x, z), mau.y});
    }
    sort(d.begin(), d.end(), [](const auto &p, const auto &q) {
        return p.first < q.first;
    });

    map<string, int> phieu;
    for (int i = 0; i < k; i++) phieu[d[i].second]++;

    string tot = "";
    int nhieu = -1;
    for (const auto &p : phieu) {
        if (p.second > nhieu) {
            nhieu = p.second;
            tot = p.first;
        }
    }
    return tot;
}

int main() {
    vector<Mau> D = {
        {{2, 300}, "chua dat"}, {{3, 450}, "chua dat"}, {{4, 600}, "chua dat"},
        {{15, 1800}, "dat"}, {{16, 2000}, "dat"}, {{18, 2400}, "dat"},
        {{5, 2200}, "chua dat"}, {{17, 700}, "dat"}
    };

    vector<double> cmin, cmax;
    chuan_hoa(D, cmin, cmax);

    vector<double> x_moi = {14, 800};
    vector<double> z_moi(x_moi.size());
    for (size_t j = 0; j < x_moi.size(); j++) {
        z_moi[j] = (x_moi[j] - cmin[j]) / (cmax[j] - cmin[j]);
    }

    int k = 3;
    string ket_qua = k_lang_gieng(D, z_moi, k);
    cout << "Du doan cho mau (14, 800) voi K=" << k << ": " << ket_qua << endl;

    return 0;
}
