"""
ID: hsfncd31
LANG: PYTHON3
TASK: ariprog
"""
import os
import typing
import itertools
import time


def main():
    base_filename = 'test' if os.name == 'nt' else 'ariprog'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        m = int(get_line())
        start_time = time.time()

        bisquare = {p ** 2 + q ** 2 for p in range(0, m + 1) for q in range(0, m + 1)}
        # print(time.time() - start_time)
        bisquare_sorted = list(sorted(bisquare))
        # print(time.time() - start_time)
        print(len(bisquare_sorted), bisquare_sorted)
        solutions = []
        for i in range(len(bisquare_sorted)):
            for j in range(i + 1, len(bisquare_sorted)):
                # i is the first and j is the second
                b = bisquare_sorted[j] - bisquare_sorted[i]
                if bisquare_sorted[i] - b in bisquare:
                    # has been searched by (bisquare_sorted[i] - b, bisquare_sorted[i]) or further former pair
                    continue
                if bisquare_sorted[i] + (n - 1) * b > bisquare_sorted[-1]:
                    break
                current = bisquare_sorted[j]
                for k in itertools.count(2):
                    current += b
                    if current > bisquare_sorted[-1]:
                        break
                    if current not in bisquare:
                        break
                    if k >= n - 1:
                        solutions.append((current - (n - 1) * b, b))
        # print(time.time() - start_time)
        if len(solutions) == 0:
            out_print('NONE')
        else:
            print(len(solutions))
            solutions.sort(key=lambda x: (x[1], x[0]))
            print(time.time() - start_time)
            for solution in solutions:
                out_print(*solution)


if __name__ == '__main__':
    main()
