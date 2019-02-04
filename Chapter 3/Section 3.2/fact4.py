"""
ID: hsfncd31
LANG: PYTHON3
TASK: fact4
"""
import os
import typing


def main():
    base_filename = 'test' if os.name == 'nt' else 'fact4'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        trail = 1
        # 5 ** 5 == 3125, so keep 5 digits
        for i in range(2, n + 1):
            trail *= i
            while trail >= 10 ** 5 and trail % 10 == 0:
                trail //= 10
            trail %= 10 ** 5
        while trail % 10 == 0:
            trail //= 10
        trail %= 10
        out_print(trail)

if __name__ == '__main__':
    main()
