/*
ID: hsfncd31
TASK: range
LANG: C++                 
*/
#include <fstream>

int main() {
    std::fstream in("range.in", std::fstream::in), out("range.out", std::fstream::out);

    static const int MAX_N = 250;
    int n;
    std::string s;

    bool field[2][MAX_N][MAX_N];
    bool (&current)[MAX_N][MAX_N] = field[0], (&last)[MAX_N][MAX_N] = field[1];

    in >> n;
    for (int row = 0; row < n; ++row) {
        in >> s;
        for (int column = 0; column < n; ++column)
            current[row][column] = (s[column] == '1');
    }

    for (int size = 2; ; ++size) {
        int num_larger = 0;
        std::swap(current, last);
        for (int row = 0; row < n - size + 1; ++row)
            for (int column = 0; column < n - size + 1; ++column) {
                bool larger = (last[row][column] && last[row][column + 1] && last[row + 1][column] && last[row + 1][column + 1]);
                current[row][column] = larger;
                num_larger += larger;
            }
        if (num_larger)
            out << size << ' ' << num_larger << '\n';
        else
            break;
    }

    in.close();
    out.close();
}
