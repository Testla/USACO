"""
ID: hsfncd31
LANG: PYTHON3
TASK: rockers
"""
import os
import typing


def main():
    base_filename = 'test' if os.name == 'nt' else 'rockers'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n, t, m = map(int, get_line().split())
        songs = [int(s) for s in get_line().split()]

        # best[i][j]: i unused disks, at least j minutes left on last used disk
        best = [[0] * (t + 1) for _ in range(m)]
        for song in songs:
            if song > t:
                continue
            for i in range(m):
                for j in range(t - song + 1):
                    best[i][j] = max(best[i][j], best[i][j + song] + 1)
                if i < m - 1:
                    for j in range(t - song + 1, t + 1):
                        best[i][j] = max(best[i][j], best[i + 1][song] + 1)

        out_print(best[0][0])


if __name__ == '__main__':
    main()
