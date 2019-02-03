"""
ID: hsfncd31
LANG: PYTHON3
TASK: agrinet
"""
import os
import typing
import itertools
import heapq


class DisjointSet(object):
    def __init__(self, size: int):
        self.father = list(range(size))

    def get_ancestor(self, x: int) -> int:
        if self.father[x] != x:
            self.father[x] = self.get_ancestor(self.father[x])
        return self.father[x]

    def union(self, a: int, b: int) -> None:
        self.father[self.get_ancestor(b)] = self.get_ancestor(a)

    def query(self, a: int, b: int) -> bool:
        return bool(self.get_ancestor(a) == self.get_ancestor(b))

def main():
    base_filename = 'test' if os.name == 'nt' else 'agrinet'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        # [(d, i, j)]
        edges = []
        for i in range(n):
            distances = []
            while len(distances) != n:
                distances.extend(map(int, get_line().split()))
            for j, d in enumerate(itertools.islice(distances, i + 1, None), i + 1):
                heapq.heappush(edges, (d, i, j))
        num_edges_added = 0
        disjoint_set = DisjointSet(n)
        answer = 0
        while num_edges_added < n - 1:
            d, i, j = heapq.heappop(edges)
            if not disjoint_set.query(i, j):
                disjoint_set.union(i, j)
                answer += d
                num_edges_added += 1
        out_print(answer)


if __name__ == '__main__':
    main()
