"""
ID: hsfncd31
LANG: PYTHON3
TASK: preface
"""
import os
import typing
import collections


def roman_numeral(x: int) -> str:
    letters = ('IV', 'XL', 'CD', 'M')
    """ I II III IV V VI VII VIII IX X """
    components = []
    for power in range(3, 0 - 1, -1):
        digit = x % 10 ** (power + 1) // 10 ** power
        component = ''
        if digit <= 3:
            component = letters[power][0] * digit
        elif digit == 4:
            component = letters[power][0] + letters[power][1]
        elif digit <= 8:
            component = letters[power][1] + letters[power][0] * (digit - 5)
        else:
            # digit == 9
            component = letters[power][0] + letters[power + 1][0]
        components.append(component)
    return ''.join(components)


def main():
    base_filename = 'test' if os.name == 'nt' else 'preface'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        letters = 'IVXLCDM'
        count = collections.defaultdict(int)
        for x in range(1, n + 1):
            roman = roman_numeral(x)
            for letter in letters:
                count[letter] += roman.count(letter)

        for letter in letters:
            if count[letter] == 0:
                break
            out_print(letter, count[letter])

if __name__ == '__main__':
    main()
