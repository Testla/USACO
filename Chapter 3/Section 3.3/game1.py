"""
ID: hsfncd31
LANG: PYTHON3
TASK: game1
"""
import os
import typing


def main():
    base_filename = 'test' if os.name == 'nt' else 'game1'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        board = [int(s) for s in infile.read().split()]
        # best[i][j]: advantage of player who moves first in range [i, j)
        best = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            best[i][i] = 0
        for length in range(1, n + 1):
            for left in range(n - length + 1):
                best[left][left + length] = max(
                    board[left] - best[left + 1][left + length],
                    board[left + length - 1] - best[left][left + length - 1],
                )

        total = sum(board)
        advantage = best[0][n]
        # print(board)
        # print(total, advantage)
        out_print((total + advantage) // 2, (total - advantage) // 2)


if __name__ == '__main__':
    main()
