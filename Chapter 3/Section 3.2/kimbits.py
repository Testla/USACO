"""
ID: hsfncd31
LANG: PYTHON3
TASK: kimbits
"""
import os
import typing


def main():
    base_filename = 'test' if os.name == 'nt' else 'kimbits'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n, l, i = map(int, get_line().split())
        max_n = 31
        # dp[a][b]: length is a bits, b or fewer bits that are '1'
        dp = [[0] * (max_n + 1) for _ in range(max_n + 1)]
        for b in range(max_n + 1):
            dp[0][b] = 1
        for a in range(1, n + 1):
            dp[a][0] = 1
            for b in range(1, a + 1):
                # 0: a-1, b; 1: a-1, b-1
                dp[a][b] = dp[a - 1][b] + dp[a - 1][b - 1]
            for b in range(a + 1, max_n + 1):
                dp[a][b] = dp[a][b - 1]
        # let i be the number of strings before
        i -= 1
        while n > 0:
            # first 0: dp[n - 1][l]
            if i < dp[n - 1][l]:
                out_print('0', end='')
            else:
                out_print('1', end='')
                i -= dp[n - 1][l]
                l -= 1
            n -= 1
        out_print('')


if __name__ == '__main__':
    main()
