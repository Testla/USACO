"""
ID: hsfncd31
LANG: PYTHON3
TASK: ratios
TLE at Case#9
"""
import os
import typing
import math


def lcm(a: int, b: int) -> int:
    return a // math.gcd(a, b) * b


def main():
    base_filename = 'test' if os.name == 'nt' else 'ratios'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        matrix = [[0] * 4 for _ in range(3)]
        goal_ratio = [int(s) for s in get_line().split()]
        for i in range(3):
            matrix[i][3] = goal_ratio[i]
        for mixture in range(3):
            ratio = [int(s) for s in get_line().split()]
            for i in range(3):
                matrix[i][mixture] = ratio[i]

        # gauss elimination

        def scalar_multiply(vector: typing.List[int], scalar: int) -> typing.List[int]:
            return [x * scalar for x in vector]

        def add(a: typing.List[int], b: typing.List[int]) -> typing.List[int]:
            return [i + j for i, j in zip(a, b)]

        # step 1, to row-echelon form
        for column in range(3):
            for row in range(column + 1, 3):
                gcd = math.gcd(matrix[column][column], matrix[row][column])
                matrix[row] = add(scalar_multiply(matrix[row], matrix[column][column] // gcd),
                                  scalar_multiply(matrix[column], -1 * matrix[row][column] // gcd))
        # step 2
        for column in range(1, 3):
            for row in range(column - 1, 0 - 1, -1):
                gcd = math.gcd(matrix[column][column], matrix[row][column])
                matrix[row] = add(scalar_multiply(matrix[row], matrix[column][column] // gcd),
                                  scalar_multiply(matrix[column], -1 * matrix[row][column] // gcd))

        # simplify the three rows
        for i in range(3):
            gcd = math.gcd(matrix[i][i], matrix[i][3])
            if matrix[i][i] < 0:
                gcd *= -1
            matrix[i][i] //= gcd
            matrix[i][3] //= gcd

        f = lcm(matrix[0][0], lcm(matrix[1][1], matrix[2][2]))
        numbers = [matrix[i][3] * f // matrix[i][i] for i in range(3)]

        if not all(0 <= number < 100 for number in numbers):
            out_print('NONE')
            return

        out_print(*(*numbers, f))


if __name__ == '__main__':
    main()
