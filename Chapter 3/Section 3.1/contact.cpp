/*
ID: hsfncd31
TASK: contact
LANG: C++                 
*/
#include <fstream>
#include <deque>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>

struct Trie {
    static const int Dictionary_size = 2;
    struct Node {
        int next[Dictionary_size];
        std::string string;
        int num_occurrence;
        bool operator <(const Node &o) {
            return (string.length() < o.string.length() || (string.length() == o.string.length() && string < o.string));
        }
    };
    std::vector<Node> nodes;

    Trie() {
        nodes.emplace_back();
    }

    int next(int x, char c) {
        int i = c - '0';
        if (nodes[x].next[i] == 0) {
            nodes[x].next[i] = nodes.size();
            nodes.emplace_back();
            nodes.back().string = nodes[x].string + c;
        }
        nodes[nodes[x].next[i]].num_occurrence += 1;
        return nodes[x].next[i];
    }
};

int main() {
    std::fstream in("contact.in", std::fstream::in), out("contact.out", std::fstream::out);

    int a, b, n;
    std::string s;
    std::deque<int> q;
    Trie trie;

    in >> a >> b >> n;
    while (in >> s) {
        for (auto &c: s) {
            q.push_back(0);
            if (q.size() > b)
                q.pop_front();
            for (auto &p: q)
                p = trie.next(p, c);
        }
    }

    std::map<int, std::vector<std::string>> string_of_num_occurrence;
    for (auto &node: trie.nodes) {
        if (node.string.length() >= a)
            string_of_num_occurrence[node.num_occurrence].push_back(node.string);
    }

    for (auto it = string_of_num_occurrence.rbegin(); it != string_of_num_occurrence.rend() && n--; ++it) {
        out << it->first << '\n';
        std::sort(
            it->second.begin(), it->second.end(),
            [](const std::string &a, const std::string &b) {
                return (a.length() < b.length() || (a.length() == b.length() && a < b));
            }
        );
        for (int i = 0; i < it->second.size(); ++i)
            out << it->second[i] << ((i % 6 == 5 || i == it->second.size() - 1) ? '\n' : ' ');
    }

    in.close();
    out.close();
}
