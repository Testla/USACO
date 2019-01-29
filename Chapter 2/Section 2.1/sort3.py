"""
ID: hsfncd31
LANG: PYTHON3
TASK: sort3
"""
import os
import typing


def main():
    base_filename = 'test' if os.name == 'nt' else 'sort3'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        sequence = [int(get_line()) for _ in range(n)]
        number_of_type = [None, *(sequence.count(i) for i in range(1, 2 + 1))]
        # first swap all 1s to the 1-zone, then swap 2 and 3 if necessary
        # #swaps = not 1 in 1-zone + (total number of 2 - (min(2 in 1-zone, 1 in 2-zone) + 2 in 2-zone))
        zone = {
            1: sequence[:number_of_type[1]],
            2: sequence[number_of_type[1]: number_of_type[1] + number_of_type[2]],
        }
        answer = sequence[number_of_type[1]:].count(1)\
            + (number_of_type[2]
               - (min(zone[1].count(2), zone[2].count(1))
                  + zone[2].count(2)))
        out_print(answer)


if __name__ == '__main__':
    main()
