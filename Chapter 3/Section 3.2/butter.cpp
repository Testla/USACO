/*
ID: hsfncd31
TASK: butter
LANG: C++                 
*/
#include <fstream>
#include <map>
#include <vector>
#include <queue>

std::vector<int> dijkstra(
        std::map<int, std::vector<std::pair<int, int>>> graph,
        int num_vertices, int source) {
    std::vector<int> distance(num_vertices, -1);
    distance[source] = 0;
    std::vector<bool> processed(num_vertices);
    // [(-distance, vertex)]
    std::priority_queue<std::pair<int, int>> q;
    q.push(std::make_pair(0, source));
    while (!q.empty()) {
        int v = q.top().second;
        q.pop();
        if (processed[v])
            continue;
        processed[v] = true;
        for (auto &kv: graph[v]) {
            int v2 = kv.first, l = kv.second;
            if (distance[v2] == -1 || distance[v] + l < distance[v2]) {
                distance[v2] = distance[v] + l;
                q.push(std::make_pair(-distance[v2], v2));
            }
        }
    }
    return distance;
}

int main() {
    std::fstream in("butter.in", std::fstream::in), out("butter.out", std::fstream::out);

    int num_cows, num_pastures, num_paths;
    in >> num_cows >> num_pastures >> num_paths;
    std::map<int, int> num_cows_in_pasture;
    for (int _ = 0; _ < num_cows; ++_) {
        int pasture;
        in >> pasture;
        num_cows_in_pasture[pasture - 1] += 1;
    }
    // { v: [(v2, l)] }
    std::map<int, std::vector<std::pair<int, int>>> graph;
    for (int _ = 0; _ < num_paths; ++_) {
        int a, b, l;
        in >> a >> b >> l;
        if (a == b)
            continue;
        a -= 1;
        b -= 1;
        graph[a].push_back(std::make_pair(b, l));
        graph[b].push_back(std::make_pair(a, l));
    }

    int answer = -1;
    for (int sugar_pasture = 0; sugar_pasture < num_pastures; ++sugar_pasture) {
        std::vector<int> distance = dijkstra(graph, num_pastures, sugar_pasture);
        int total_cost = 0;
        for (auto &kv: num_cows_in_pasture) {
            if (distance[kv.first] == -1) {
                total_cost = -1;
                break;
            }
            total_cost += distance[kv.first] * kv.second;
        }
        if (total_cost != -1 && (answer == -1 || total_cost < answer))
            answer = total_cost;
    }

    out << answer << '\n';

    in.close();
    out.close();
}
