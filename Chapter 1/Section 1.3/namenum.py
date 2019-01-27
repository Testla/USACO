"""
ID: hsfncd31
LANG: PYTHON3
TASK: namenum
"""
import os
import collections
import typing


def digit_of(c: str) -> str:
    o = ord(c)
    if o > ord('Q'):
        o -= 1
    return str((o - ord('A')) // 3 + 2)


def number_of(s: str):
    return ''.join(map(digit_of, s))


def main():
    base_filename = 'test' if os.name == 'nt' else 'namenum'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        words_of_number = collections.defaultdict(list)
        with open('dict.txt') as df:
            for line in df:
                word = line.rstrip('\n')
                words_of_number[number_of(word)].append(word)
        num = get_line()
        print(words_of_number)
        out_print('\n'.join(words_of_number.get(num, ('NONE',))))

if __name__ == '__main__':
    main()
