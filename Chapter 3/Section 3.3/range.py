"""
ID: hsfncd31
LANG: PYTHON3
TASK: range
TLE at Case#7
"""
import os
import typing
import itertools


def main():
    base_filename = 'test' if os.name == 'nt' else 'range'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        # Mark the upper-left corner of each square.
        # Starting from size 2, four marks in a 2x2 square means a larger square.
        n = int(get_line())
        field = [[bool(c == '1') for c in get_line()] for _ in range(n)]
        current = field.copy()
        last = [[False] * n for _ in range(n)]
        for size in itertools.count(2):
            current, last = last, current
            num_larger = 0
            for row in range(n - size + 1):
                for column in range(n - size + 1):
                    larger_square = bool(last[row][column] and last[row][column + 1]
                                         and last[row + 1][column] and last[row + 1][column + 1])
                    current[row][column] = larger_square
                    num_larger += 1 if larger_square else 0
            if num_larger:
                out_print(size, num_larger)
            else:
                break


if __name__ == '__main__':
    main()
