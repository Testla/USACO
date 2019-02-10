/*
ID: hsfncd31
TASK: nuggets
LANG: C++                 
*/
#include <fstream>
#include <iostream>
#include <vector>

static const int MAX_N = 256;
bool is_possible[MAX_N * MAX_N + 1];

int gcd(int a, int b) {
    if (a < b)
        std::swap(a, b);
    for (int r; r = a % b; ) {
        a = b;
        b = r;
    }
    return b;
}

int main() {
    std::fstream in("nuggets.in", std::fstream::in), out("nuggets.out", std::fstream::out);

    int n;
    in >> n;
    std::vector<int> options;
    for (int _ = 0, x; _ < n; ++_) {
        in >> x;
        is_possible[x] = true;
        options.push_back(x);
    }

    bool all_possible = is_possible[1];
    int d = options[0];
    for (int x: options)
        d = gcd(d, x);
    bool infinite_impossible = (d != 1);
    if (all_possible || infinite_impossible) {
        out << "0\n";
        return 0;
    }

    std::vector<int> possible_numbers;
    int largest_impossible;
    for (int x = 1; ; ++x) {
        if (possible_numbers.size() >= (x + 1) / 2)
            break;
        if (is_possible[x]) {
            possible_numbers.push_back(x);
            continue;
        }
        for (int a: possible_numbers) {
            if (is_possible[x - a]) {
                is_possible[x] = true;
                possible_numbers.push_back(x);
                break;
            }
            if (a >= x / 2)
                break;
        }
        if (!is_possible[x])
            largest_impossible = x;
    }

    out << largest_impossible << '\n';

    in.close();
    out.close();
}
