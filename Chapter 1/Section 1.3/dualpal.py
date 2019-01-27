"""
ID: hsfncd31
LANG: PYTHON3
TASK: dualpal
"""
import os
import collections
import typing
import string
import itertools


def digit_character(x: int) -> str:
    if not hasattr(digit_character, 'dict'):
        digit_character.dict = string.digits + string.ascii_uppercase
    return digit_character.dict[x]


def base_k_string(x: int, base: int) -> str:
    result = []
    # actually I want do-while...
    while True:
        result.append(digit_character(x % base))
        x //= base
        if x == 0:
            break
    return ''.join(reversed(result))


def is_palindrome(s: str) -> bool:
    for i in range(0, len(s) // 2):
        if s[i] != s[-(i + 1)]:
            return False
    return True


def main():
    base_filename = 'test' if os.name == 'nt' else 'dualpal'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n, s = map(int, get_line().split())

        for x in itertools.count(s + 1):
            count = 0
            for base in range(2, 10 + 1):
                if is_palindrome(base_k_string(x, base)):
                    count += 1
                    if count == 2:
                        break
            if count == 2:
                out_print(x)
                n -= 1
                if n == 0:
                    break


if __name__ == '__main__':
    main()
