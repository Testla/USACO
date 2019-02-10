"""
ID: hsfncd31
LANG: PYTHON3
TASK: nuggets
"""
import os
import typing
import functools
import math
import itertools


def main():
    base_filename = 'test' if os.name == 'nt' else 'nuggets'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        options = { int(get_line()) for _ in range(n) }

        # just a guess
        infinite_largest = bool(functools.reduce(math.gcd, options) != 1)
        all_possible = bool(min(options) == 1)
        if infinite_largest or all_possible:
            out_print('0')
            return

        # to find impossible numbers, start from 1, flag if all possible number smaller doesn't add up

        # maybe always try to generate smallest number that is larger than the largest generated

        # For any k, k = floor(k / 2) + ceil(k / 2).
        # So if [a, 2a] are all possible,
        # we can generate [2a, 4a], [4a, 8a] etc.
        # impossible_numbers = []
        # impossible_numbers_set = set()
        # for x in itertools.count(1):
        #     if impossible_numbers and x // 2 >= impossible_numbers[-1] + 1:
        #         out_print(impossible_numbers[-1])
        #         break
        #     possible = False
        #     if x in options:
        #         possible = True
        #     else:
        #         for i in range(2, x // 2 + 1):
        #             if i not in impossible_numbers and x - i not in impossible_numbers:
        #                 possible = True
        #                 break
        #     if not possible:
        #         impossible_numbers.append(x)
        #         impossible_numbers_set.add(x)

        # At any time, if size of possible numbers is bigger than half of the next number,
        # the next number must be possible, retaining the feature, making all subsequent numbers possible.

        # Say if initial numbers are a and a + 1, then [ka, k(a + 1)] will be possible,
        # from k = a - 1, all numbers in [ka, k(a + 1)) will be possible,
        # so (a - 2)a + a - 1 will be the largest impossible number.
        max_i = 256
        is_possible = [False] * (max_i ** 2 + 1)
        possible_numbers = []
        largest_impossible = None
        for x in itertools.count(1):
            if len(possible_numbers) >= (x + 1) // 2:
                # all larger numbers are possible
                break
            if x in options:
                is_possible[x] = True
                possible_numbers.append(x)
                continue
            for possible_number in possible_numbers:
                if possible_number > x // 2:
                    break
                if is_possible[x - possible_number]:
                    is_possible[x] = True
                    possible_numbers.append(x)
                    break
            if not is_possible[x]:
                largest_impossible = x

        out_print(largest_impossible)



if __name__ == '__main__':
    main()
