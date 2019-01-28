"""
ID: hsfncd31
LANG: PYTHON3
TASK: combo
"""
import os
import typing
import itertools


def main():
    base_filename = 'test' if os.name == 'nt' else 'combo'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        john = [int(s) for s in get_line().split()]
        master = [int(s) for s in get_line().split()]
        possible_settings = set()
        for delta in itertools.product(*(list(range(-2, 2 + 1)) for _ in range(3))):
            possible_settings.add(tuple((john[position] + delta[position] + n) % n for position in range(3)))
            possible_settings.add(tuple((master[position] + delta[position] + n) % n for position in range(3)))
        out_print(len(possible_settings))


if __name__ == '__main__':
    main()
