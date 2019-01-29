"""
ID: hsfncd31
LANG: PYTHON3
TASK: hamming
"""
import os
import typing
import itertools


def hamming_distance(a: int, b: int) -> bool:
    d = a ^ b
    result = 0
    while d:
        result += 1
        d &= (d - 1)
    return result


def main():
    base_filename = 'test' if os.name == 'nt' else 'hamming'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n, b, d = map(int, get_line().split())
        answer = [0]
        for i in itertools.count(1):
            if all(hamming_distance(i, x) >= d for x in answer):
                answer.append(i)
                if len(answer) >= n:
                    break
        for i in range(0, n, 10):
            out_print(*answer[i: i + 10])


if __name__ == '__main__':
    main()
