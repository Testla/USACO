"""
ID: hsfncd31
LANG: PYTHON3
TASK: money
"""
import os
import typing
import itertools


def main():
    base_filename = 'test' if os.name == 'nt' else 'money'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        v, n = map(int, get_line().split())
        coins = list(itertools.chain(*((int(s) for s in line.split()) for line in infile)))

        dp = [0] * (n + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, n + 1):
                dp[i] += dp[i - coin]
        out_print(dp[n])


if __name__ == '__main__':
    main()
