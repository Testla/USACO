/*
ID: hsfncd31
TASK: camelot
LANG: C++                 
*/
#include <fstream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cstdlib>
#include <cstring>
#include <cmath>

static const int MAX_R = 30, MAX_C = 26;
int knight_distance[MAX_R][MAX_C][MAX_R][MAX_C];

int main() {
    std::fstream in("camelot.in", std::fstream::in), out("camelot.out", std::fstream::out);

    int r, c;
    in >> r >> c;
    std::vector<std::pair<int, int>> chess;
    std::string column_string;
    for (int row, column; in >> column_string; ) {
        in >> row;
        row = r - row;
        column = column_string[0] - 'A';
        chess.push_back(std::make_pair(row, column));
    }
    std::pair<int, int> king = chess[0];
    std::vector<std::pair<int, int>> knights;
    std::copy(++chess.begin(), chess.end(), std::back_inserter(knights));
    std::vector<std::pair<int, int>> directions{
        { -2, -1 }, { -2, 1 },
        { -1, -2 }, { -1, 2 },
        { 1, -2 }, { 1, 2 },
        { 2, -1 }, { 2, 1 },
    };

    ::memset(knight_distance, -1, sizeof(knight_distance));
    for (int row = 0; row < r; ++row)
        for (int column = 0; column < c; ++column) {
            std::queue<std::pair<int, int>> q;
            q.push(std::make_pair(row, column));
            knight_distance[row][column][row][column] = 0;
            while (!q.empty()) {
                std::pair<int, int> current = q.front();
                q.pop();
                for (auto &d: directions) {
                    std::pair<int, int> to{current.first + d.first, current.second + d.second};
                    if (!(0 <= to.first && to.first < r && 0 <= to.second && to.second < c))
                        continue;
                    // int &target = knight_distance[row][column][to.first][to.second];
                    // if (target == -1) {
                    //     target = knight_distance[row][column][current.first][current.second] + 1;
                    //     q.push(to);
                    // }
                    if (knight_distance[row][column][to.first][to.second] == -1) {
                        knight_distance[row][column][to.first][to.second] = knight_distance[row][column][current.first][current.second] + 1;
                        q.push(to);
                    }
                }
            }
        }

    int sum_row = 0, sum_column = 0;
    for (auto &ch: chess) {
        sum_row += ch.first;
        sum_column += ch.second;
    }
    int center_row = ::round(sum_row * 1.0 / chess.size()), center_column = ::round(sum_column * 1.0 / chess.size());
    int search_range;
    if (chess.size() < 10)
        search_range = 100;
    else if (chess.size() < 30)
        search_range = 10;
    else
        search_range = 3;

    int answer = -1;
    // for (int gathering_row = 0; gathering_row < r; ++gathering_row)
    //     for (int gathering_column = 0; gathering_column < c; ++gathering_column) {
    for (int gathering_row = std::max(center_row - search_range, 0); gathering_row < std::min(center_row + search_range, r); ++gathering_row)
        for (int gathering_column = std::max(center_column - search_range, 0); gathering_column < std::min(center_column + search_range, c); ++gathering_column) {
            int sum_knights_move = 0;
            bool gathering_point_reachable = true;
            for (auto &knight: knights) {
                if (knight_distance[gathering_row][gathering_column][knight.first][knight.second] == -1) {
                    gathering_point_reachable = false;
                    break;
                }
                sum_knights_move += knight_distance[gathering_row][gathering_column][knight.first][knight.second];
            }
            if (!gathering_point_reachable)
                continue;
            for (int meeting_row = 0; meeting_row < r; ++meeting_row)
                for (int meeting_column = 0; meeting_column < c; ++meeting_column) {
                    int king_move = std::max(::abs(king.first - meeting_row), ::abs(king.second - meeting_column));
                    int post_meeting_move = knight_distance[gathering_row][gathering_column][meeting_row][meeting_column];
                    if (post_meeting_move == -1)
                        continue;
                    for (auto &meet_knight: knights) {
                        int old_knight_move = knight_distance[gathering_row][gathering_column][meet_knight.first][meet_knight.second];
                        int knight_meeting_move = knight_distance[meeting_row][meeting_column][meet_knight.first][meet_knight.second];
                        if (knight_meeting_move == -1)
                            continue;
                        int total_move = sum_knights_move - old_knight_move + king_move + knight_meeting_move + post_meeting_move;
                        if (answer == -1 || total_move < answer)
                            answer = total_move;
                    }
                }
            // In case of there's no knight, the king moves on his own.
            if (knights.size() == 0) {
                int king_alone_move = std::max(::abs(king.first - gathering_row), ::abs(king.second - gathering_column));
                if (answer == -1 || king_alone_move < answer)
                    answer = king_alone_move;
            }
        }

    out << answer << '\n';

    in.close();
    out.close();
}
