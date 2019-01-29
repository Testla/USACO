"""
ID: hsfncd31
LANG: PYTHON3
TASK: frac1
"""
import os
import typing
import functools


def gcd(a: int, b: int) -> int:
    if a > b:
        a, b = b, a
    while a != 0:
        a, b = b % a, a
    return b


def coprime(a: int, b: int) -> bool:
    return bool(gcd(a, b) == 1)


def compare_fraction(a: typing.Tuple[int], b: typing.Tuple[int]) -> int:
    return a[0] * b[1] - a[1] * b[0]


def main():
    base_filename = 'test' if os.name == 'nt' else 'frac1'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        # [(numerator, denominator)]
        fractions = [(a, b) for b in range(1, n + 1) for a in range(b + 1) if coprime(a, b)]
        # the reason why 0/1 is included while 0/k are not is due to the implementation of co-prime...
        fractions.sort(key=functools.cmp_to_key(compare_fraction))
        for fraction in fractions:
            out_print('{}/{}'.format(*fraction))

if __name__ == '__main__':
    main()
