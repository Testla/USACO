"""
ID: hsfncd31
LANG: PYTHON3
TASK: fence9
"""
import os
import typing


def main():
    base_filename = 'test' if os.name == 'nt' else 'fence9'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n, m, p = map(int, get_line().split())
        # o, a, b = (0, 0), (p, 0), (n, m)
        # ob: x = y * n / m
        # ab:
        # Ax + By + C = 0
        # (p, 0) -> C = -Ap
        # nA + mB + C = 0
        # A(n - p) = -mB
        # let B = n - p, A = -m, C = mp
        # -mx + (n - p)y + mp = 0
        # x = (n - p)y / m + p

        answer = 0
        for y in range(m - 1, 0, -1):
            # [left_x, right_x]
            left_x = (y * n + m) // m
            right_x = ((n - p) * y - 1) // m + p
            answer += right_x + 1 - left_x

        out_print(answer)


if __name__ == '__main__':
    main()
