"""
ID: hsfncd31
LANG: PYTHON3
TASK: runround
"""
import os
import typing
import itertools


def is_runaround(x: int) -> bool:
    digits = [int(c) for c in str(x)]
    if 0 in digits or len(set(digits)) != len(digits):
        return False
    visited = [False] * len(digits)
    p = 0
    while not visited[p]:
        visited[p] = True
        p = (p + digits[p]) % len(digits)
    return p == 0 and all(visited)


def main():
    base_filename = 'test' if os.name == 'nt' else 'runround'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        m = int(get_line())
        for x in itertools.count(m + 1):
            if is_runaround(x):
                out_print(x)
                break


if __name__ == '__main__':
    main()
