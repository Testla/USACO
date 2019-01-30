"""
ID: hsfncd31
LANG: PYTHON3
TASK: nocows
Time Limit Exceeded in Case#7
"""
import os
import typing


def main():
    base_filename = 'test' if os.name == 'nt' else 'nocows'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        N, K = map(int, get_line().split())
        max_n, max_k, mod = 200 - 1, 100 - 1, 9901
        # n, k
        dp = [[0] * (max_k + 1) for _ in range(max_n + 1)]
        dp[0][0], dp[1][1] = 1, 1
        for n in range(2, N + 1):
            for k in range(min(len(dp[0]), n + 1, K + 1)):
                for left_n in range(1, n - 1):
                    for smaller_k in range(k - 1):
                        dp[n][k] += dp[left_n][k - 1] * dp[n - 1 - left_n][smaller_k]
                        dp[n][k] += dp[left_n][smaller_k] * dp[n - 1 - left_n][k - 1]
                    # both k - 1
                    dp[n][k] += dp[left_n][k - 1] * dp[n - 1 - left_n][k - 1]
                    dp[n][k] %= mod
                # print(n, k, dp[n][k])
        out_print(dp[N][K])


if __name__ == '__main__':
    main()
