"""
ID: hsfncd31
LANG: PYTHON3
TASK: fence
"""
import os
import typing
import collections
import heapq


def main():
    base_filename = 'test' if os.name == 'nt' else 'fence'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        # Well, the graph may contain two or more edge with same endpoints...

        f = int(get_line())
        # { v: heap[ v2 ] }
        graph = collections.defaultdict(list)
        # { v: { v2: times } }
        num_edges = collections.defaultdict(lambda: collections.defaultdict(int))
        for _ in range(f):
            i, j = map(int, get_line().split())
            heapq.heappush(graph[i], j)
            heapq.heappush(graph[j], i)
            num_edges[i][j] += 1
            num_edges[j][i] += 1

        start_vertex = None
        for vertex, edges in graph.items():
            if len(edges) % 2 == 1 and (start_vertex is None or vertex < start_vertex):
                # start at odd-degree vertex, if any
                start_vertex = vertex
        if start_vertex is None:
            start_vertex = min(v for v in graph)

        answer = []
        stack = [start_vertex]
        while len(stack):
            v = stack[-1]
            while graph[v] and num_edges[v][graph[v][0]] == 0:
                heapq.heappop(graph[v])
            if len(graph[v]) > 0:
                v2 = graph[v][0]
                num_edges[v][v2] -= 1
                num_edges[v2][v] -= 1
                stack.append(v2)
                continue
            answer.append(stack.pop())

        out_print(*reversed(answer), sep='\n')

if __name__ == '__main__':
    main()
