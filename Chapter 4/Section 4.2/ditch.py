"""
ID: hsfncd31
LANG: PYTHON3
TASK: ditch
"""
import os
import typing
import collections


def main():
    base_filename = 'test' if os.name == 'nt' else 'ditch'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        # swap naming of n and m for convention
        m, n = map(int, get_line().split())
        graph = collections.defaultdict(lambda: collections.defaultdict(int))
        for _ in range(m):
            s, e, c = map(int, get_line().split())
            # There are edges with same (s, e) in Case#10
            graph[s][e] += c

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
            return _flow(source, sink, None, [False] * (n + 1))

        answer = 0
        while True:
            result = flow(1, n)
            if result == 0:
                break
            answer += result

        out_print(answer)


if __name__ == '__main__':
    main()
