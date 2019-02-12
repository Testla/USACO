"""
ID: hsfncd31
LANG: PYTHON3
TASK: stall4
"""
import os
import typing
import collections
import itertools


def main():
    base_filename = 'test' if os.name == 'nt' else 'stall4'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n, m = map(int, get_line().split())
        # source 0, stalls 1 ... m, cows m + 1 ... m + n, sink m + n + 1
        source, sink = 0, m + n + 1
        graph = collections.defaultdict(lambda: collections.defaultdict(int))
        for stall in range(1, m + 1):
            graph[source][stall] = 1
        for cow in range(m + 1, m + 1 + n):
            for stall in itertools.islice(map(int, get_line().split()), 1, None):
                graph[stall][cow] = 1
            graph[cow][sink] = 1

        def _flow(current: int, sink: int, capacity_so_far: typing.Union[None, int], visited: typing.List[bool])\
                -> int:
            """ capacity_so_far use None for infinite"""
            visited[current] = True
            for neighbour, capacity in graph[current].items():
                if capacity > 0 and not visited[neighbour]:
                    new_capacity = min(capacity, capacity_so_far) if capacity_so_far is not None else capacity
                    if neighbour == sink:
                        result = new_capacity
                    else:
                        result = _flow(neighbour, sink, new_capacity, visited)
                    if result > 0:
                        graph[current][neighbour] -= result
                        graph[neighbour][current] += result
                        return result
            return 0

        def flow(source: int, sink: int) -> int:
            return _flow(source, sink, None, [False] * (n + m + 2))

        answer = 0
        while True:
            result = flow(source, sink)
            if result == 0:
                break
            answer += result

        out_print(answer)


if __name__ == '__main__':
    main()
