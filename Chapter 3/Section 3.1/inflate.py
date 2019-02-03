"""
ID: hsfncd31
LANG: PYTHON3
TASK: inflate
"""
import os
import typing


def main():
    base_filename = 'test' if os.name == 'nt' else 'inflate'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        m, n = map(int, get_line().split())
        categories = [tuple(map(int, get_line().split())) for _ in range(n)]

        max_score_of_time = [0] * (m + 1)
        # more points first, less time first
        categories.sort(key=lambda x: (x[0], -x[1]), reverse=True)
        shortest_time = categories[0][1] + 1
        for points, time in categories:
            if time >= shortest_time:
                # already processed a category that is not worse
                continue
            shortest_time = time
            for t in range(time, m + 1):
                max_score_of_time[t] = max(max_score_of_time[t], max_score_of_time[t - time] + points)

        out_print(max_score_of_time[m])


if __name__ == '__main__':
    main()
