"""
ID: hsfncd31
LANG: PYTHON3
TASK: cowtour
"""
import os
import typing
import itertools
import sys


def distance_between(a: typing.Tuple[int, int], b: typing.Tuple[int, int]) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** (1 / 2)


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
    base_filename = 'test' if os.name == 'nt' else 'cowtour'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        pastures = \
            [tuple(int(s) for s in get_line().split()) for _ in range(n)]  # type: typing.List[typing.Tuple[int, int]]
        adjacency = [[False if c == '0' else True for c in get_line()] for _ in range(n)]

        # Floyd-Warshall
        distance = [[None] * n for _ in range(n)]
        for i in range(n):
            distance[i][i] = 0
        for i in range(n):
            for j in range(i + 1, n):
                if adjacency[i][j]:
                    distance[i][j] = distance[j][i] = distance_between(pastures[i], pastures[j])
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distance[i][k] is not None and distance[k][j] is not None\
                            and (distance[i][j] is None or distance[i][k] + distance[k][j] < distance[i][j]):
                        distance[i][j] = distance[i][k] + distance[k][j]
        # maximum distance to another point in the same field
        max_distance = [max(d for d in distance[i] if d is not None) for i in range(n)]  # type: typing.List[float]

        # find fields
        disjoint_set = DisjointSet(n)
        fields = []  # type: typing.List[typing.Set[int]]
        field_of_ancestor = dict()
        for i in range(n):
            for j in range(i + 1, n):
                if distance[i][j] is not None:
                    disjoint_set.union(i, j)
        for i in range(n):
            ancestor = disjoint_set.get_ancestor(i)
            if ancestor not in field_of_ancestor:
                field_of_ancestor[ancestor] = len(fields)
                fields.append(set())
            fields[field_of_ancestor[ancestor]].add(i)

        # try every possible combinations
        answer = sys.maxsize
        for i, field in enumerate(fields):
            for another_field in itertools.islice(fields, i + 1, len(fields)):
                field_internal_diameter = max(max(max_distance[p] for p in f) for f in (field, another_field))
                inter_field_diameter = min(
                    max_distance[p1] + max_distance[p2] + distance_between(pastures[p1], pastures[p2])
                    for p1, p2 in itertools.product(field, another_field))
                new_diameter = max(field_internal_diameter, inter_field_diameter)
                answer = min(answer, new_diameter)
        out_print('%.6lf' % answer)

if __name__ == '__main__':
    main()
