/*
ID: hsfncd31
TASK: stamps
LANG: C++                 
*/
#include <fstream>
#include <vector>
#include <algorithm>
#include <cstring>

static const int MAX_K = 200, MAX_STAMP = 10000;
int min_num_stamp_for_value[MAX_K * MAX_STAMP + 1 + 1];

int main() {
    std::fstream in("stamps.in", std::fstream::in), out("stamps.out", std::fstream::out);

    int k, n;
    std::vector<int> stamps;
    
    in >> k >> n;
    while (stamps.size() < n) {
        int stamp;
        in >> stamp;
        stamps.push_back(stamp);
    }

    std::sort(stamps.begin(), stamps.end());
    memset(min_num_stamp_for_value, -1, (stamps.back() * k + 1 + 1) * sizeof(int));
    min_num_stamp_for_value[0] = 0;
    for (int value = 1; ; ++value) {
        for (auto &stamp: stamps) {
            if (stamp > value)
                break;
            if (min_num_stamp_for_value[value - stamp] != -1
                    && min_num_stamp_for_value[value - stamp] < k
                    && (min_num_stamp_for_value[value] == -1
                        or min_num_stamp_for_value[value - stamp] + 1 < min_num_stamp_for_value[value]))
                min_num_stamp_for_value[value] = min_num_stamp_for_value[value - stamp] + 1;
        }
        if (min_num_stamp_for_value[value] == -1) {
            out << value - 1 << '\n';
            break;
        }
    }

    in.close();
    out.close();
}
