"""
ID: hsfncd31
LANG: PYTHON3
TASK: palsquare
"""
import os
import collections
import typing
import string


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


def main():
    base_filename = 'test' if os.name == 'nt' else 'palsquare'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        base = int(get_line())
        for x in range(1, 300 + 1):
            s = base_k_string(x ** 2, base)
            if list(reversed(s)) == list(s):
                out_print(base_k_string(x, base), s)

if __name__ == '__main__':
    main()
