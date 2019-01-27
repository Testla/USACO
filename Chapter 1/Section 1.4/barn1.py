"""
ID: hsfncd31
LANG: PYTHON3
TASK: barn1
"""
import os
import typing
import heapq


def main():
    base_filename = 'test' if os.name == 'nt' else 'barn1'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        m, s, c = map(int, get_line().split())
        occupied = [*sorted(int(get_line()) for _ in range(c))]
        gaps = [occupied[i + 1] - occupied[i] - 1 for i in range(len(occupied) - 1)]
        out_print(occupied[-1] + 1 - occupied[0] - sum(heapq.nlargest(m - 1, gaps)))


if __name__ == '__main__':
    main()
