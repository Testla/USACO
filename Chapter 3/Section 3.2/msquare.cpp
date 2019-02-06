/*
ID: hsfncd31
TASK: msquare
LANG: C++                 
*/
/*
For DFID, we don't have to keep the board,
so it may not be much slower.
But there is a trap for DFID, that if we keep track of what states have
been visited, we can't use a single global visited record for each depth.
Say that the answer's path is S0 -> S1 -> ... Sn,
if some state Si (0 < i < n) appears before Sj (0 < j < i) in DFS order,
then we won't enter Si from Si-1 on the correct path
(since it's already visited by that time),
making the search ends possibly deeper than the answer
*/
#include <fstream>
#include <algorithm>
#include <array>
#include <vector>
#include <bitset>

static const size_t Board_Size = 8;
typedef std::array<int, Board_Size> Board;
typedef std::array<int, Board_Size> Transformation;
static const Transformation Transformations[] = {
    {7, 6, 5, 4, 3, 2, 1, 0},
    {3, 0, 1, 2, 5, 6, 7, 4},
    {0, 6, 1, 3, 4, 2, 5, 7}
};
static Transformation Reverse_transformations[sizeof(Transformations) / sizeof(*Transformations)];
static const char *Tranformation_names = "ABC";
static constexpr int factorial[] = { 1, 1, 2, 6, 24, 120, 720, 5040, 40320 };

int cantor_expansion(Board board) {
    int result = 0;
    for (size_t i = 0; i < board.size(); ++i) {
        int smaller = 0;
        for (size_t j = i + 1; j < board.size(); ++j)
            if (board[j] < board[i])
                smaller += 1;
        result += factorial[board.size() - 1 - i] * smaller;
    }
    return result;
}

void apply_transformation(Board &board, const Transformation &transformation) {
    static Board temp;
    for (size_t i = 0; i < board.size(); ++i)
        temp[i] = board[transformation[i]];
    board.swap(temp);
}

bool _dfid(const Board &target, Board &current, int remaining_depth,
        std::vector<int> &sequence, std::vector<std::bitset<factorial[Board_Size]>> &visited) {
    for (size_t t = 0; t < sizeof(Transformations) / sizeof(*Transformations); ++t) {
        apply_transformation(current, Transformations[t]);
        int cantor_number = cantor_expansion(current);
        if (!visited[remaining_depth].test(cantor_number)) {
            visited[remaining_depth].set(cantor_number);
            sequence.push_back(t);
            bool result;
            if (remaining_depth == 1)
                result = (current == target);
            else
                result = _dfid(target, current, remaining_depth - 1, sequence, visited);
            if (result)
                return result;
            sequence.pop_back();
        }
        apply_transformation(current, Reverse_transformations[t]);
    }
    return false;
}

// Return success or not.
bool dfid(const Board &target, int depth, std::vector<int> &sequence) {
    Board initial_board{0, 1, 2, 3, 4, 5, 6, 7};
    std::vector<std::bitset<factorial[Board_Size]>> visited(depth);
    return (depth > 1) ? _dfid(target, initial_board, depth - 1, sequence, visited) : (initial_board == target);
}


int main() {
    std::fstream in("msquare.in", std::fstream::in), out("msquare.out", std::fstream::out);

    Board target;
    for (size_t i = 0; i < target.size(); ++i) {
        in >> target[i];
        target[i] -= 1;
    }

    // calculate Reverse_transformations
    for (size_t i = 0; i < sizeof(Transformations) / sizeof(*Transformations); ++i)
        for (size_t j = 0; j < Board_Size; ++j)
            Reverse_transformations[i][j] =
                std::find(Transformations[i].begin(), Transformations[i].end(), j)
                - Transformations[i].begin();

    std::vector<int> sequence;
    for (int depth = 1; ; ++depth) {
        if (dfid(target, depth, sequence)) {
            out << sequence.size() << '\n';
            for (auto &t: sequence)
                out << Tranformation_names[t];
            out << '\n';
            break;
        }
    }

    in.close();
    out.close();
}
