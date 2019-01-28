"""
ID: hsfncd31
LANG: PYTHON3
TASK: crypt1
"""
import os
import typing


def main():
    base_filename = 'test' if os.name == 'nt' else 'crypt1'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        _ = int(get_line())
        digits = set(map(int, get_line().split()))
        def is_good_number(x: int) -> bool:
            return all(int(c) in digits for c in str(x))

        good_2_digit_number = set(filter(is_good_number, range(10 ** 1, 10 ** 2)))
        good_3_digit_number = set(filter(is_good_number, range(10 ** 2, 10 ** 3)))
        good_4_digit_number = set(filter(is_good_number, range(10 ** 3, 10 ** 4)))
        num_solution = 0
        for multiplier in good_3_digit_number:
            for multiplicand in good_2_digit_number:
                if multiplicand % 10 * multiplier in good_3_digit_number\
                        and multiplicand // 10 * multiplier in good_3_digit_number\
                        and multiplier * multiplicand in good_4_digit_number:
                    num_solution += 1
        out_print(num_solution)


if __name__ == '__main__':
    main()
