"""
ID: hsfncd31
LANG: PYTHON3
TASK: numtri
"""
import os
import typing


def main():
    base_filename = 'test' if os.name == 'nt' else 'numtri'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        highest = [int(get_line())]
        for i in range(2, n + 1):
            row = list(map(int, get_line().split()))
            new_highest = [
                row[0] + highest[0],
                *(max(highest[j - 1], highest[j]) + row[j] for j in range(1, i - 1)),
                row[i - 1] + highest[i - 2]
            ]
            highest = new_highest
        out_print(max(highest))


if __name__ == '__main__':
    main()
