"""
ID: hsfncd31
LANG: PYTHON3
TASK: fracdec
"""
import os
import typing
import itertools


def main():
    base_filename = 'test' if os.name == 'nt' else 'fracdec'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n, d = map(int, get_line().split())
        integer_part = n // d
        n %= d
        fractional_part = []
        # { modulo: position }
        modulo_position = dict()
        repeat_start = None
        while True:
            if n in modulo_position:
                repeat_start = modulo_position[n]
                break
            modulo_position[n] = len(fractional_part)
            n *= 10
            fractional_part.append(n // d)
            n %= d
            if n == 0:
                break
        answer = ''.join((
            str(integer_part),
            '.',
            *(str(x) for x in itertools.islice(fractional_part, repeat_start)),
            '' if repeat_start is None else '({})'.format(
                ''.join(str(x) for x in itertools.islice(fractional_part, repeat_start, None))),
        ))
        length_limit = 76
        out_print('\n'.join(answer[p: p + length_limit] for p in range(0, len(answer), length_limit)))

if __name__ == '__main__':
    main()
