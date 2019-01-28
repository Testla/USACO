"""
ID: hsfncd31
LANG: PYTHON3
TASK: skidesign
"""
import os
import typing


def main():
    base_filename = 'test' if os.name == 'nt' else 'skidesign'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        hills = [int(get_line()) for _ in range(n)]
        lowest_cost = None
        for minimum in range(min(hills), max(hills) - 17):
            cost = 0
            for hill in hills:
                if hill < minimum:
                    cost += (minimum - hill) ** 2
                elif hill > minimum + 17:
                    cost += (hill - minimum - 17) ** 2
            if lowest_cost is None or cost < lowest_cost:
                lowest_cost = cost
        out_print(0 if lowest_cost is None else lowest_cost)


if __name__ == '__main__':
    main()
