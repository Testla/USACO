"""
ID: hsfncd31
LANG: PYTHON3
TASK: butter
TLE at Case#9
"""
import os
import typing
import collections
import heapq


def dijkstra(graph: typing.DefaultDict[int, typing.List[typing.Tuple[int, int]]], num_vertices: int, source: int)\
        -> typing.List[typing.Union[int, None]]:
    processed = set()
    distance = [None] * num_vertices
    distance[source] = 0
    # (distance, vertex), may have duplicate vertex
    nearest_vertices = [(0, source)]
    while len(nearest_vertices):
        _, v = heapq.heappop(nearest_vertices)
        if v in processed:
            continue
        processed.add(v)
        for v2, l in graph[v]:
            if distance[v2] is None or distance[v] + l < distance[v2]:
                distance[v2] = distance[v] + l
                heapq.heappush(nearest_vertices, (distance[v2], v2))
    return distance


def main():
    base_filename = 'test' if os.name == 'nt' else 'butter'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        num_cows, num_pastures, num_paths = map(int, get_line().split())
        num_cows_in_pasture = collections.defaultdict(int)
        for _ in range(num_cows):
            num_cows_in_pasture[int(get_line()) - 1] += 1
        # adjacent linked list
        # { v1: [(v2, length)] }
        graph = collections.defaultdict(list)
        for _ in range(num_paths):
            a, b, l = map(int, get_line().split())
            if a == b:
                continue
            a -= 1
            b -= 1
            graph[a].append((b, l))
            graph[b].append((a, l))

        answer = -1  # I'd like to use None but PyCharm gives warning
        for sugar_pasture in range(num_pastures):
            distance = dijkstra(graph, num_pastures, sugar_pasture)
            total_cost = 0
            for pasture, num_cows_grazing in num_cows_in_pasture.items():
                if distance[pasture] is None:
                    total_cost = -1
                    break
                total_cost += distance[pasture] * num_cows_grazing
            if total_cost != -1 and (answer == -1 or total_cost < answer):
                answer = total_cost

        out_print(answer)


if __name__ == '__main__':
    main()
