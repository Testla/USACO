"""
ID: hsfncd31
LANG: PYTHON3
TASK: stamps
Time Limit Exceeded in Case#10
"""
import os
import typing
import itertools


def main():
    base_filename = 'test' if os.name == 'nt' else 'stamps'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        k, n = map(int, get_line().split())
        stamps = []
        while len(stamps) < n:
            stamps.extend(map(int, get_line().split()))
        stamps.sort()

        # Looks like humble number in 3.1,
        # but different combination can produce the same result.
        # We want to know the smallest possible number of stamps for each value.
        min_num_stamp_for_value = [-1] * (stamps[-1] * k + 1 + 1)
        min_num_stamp_for_value[0] = 0
        for i in itertools.count(1):
            for stamp in stamps:
                if stamp > i:
                    break
                if min_num_stamp_for_value[i - stamp] != -1\
                        and min_num_stamp_for_value[i - stamp] < k\
                        and (min_num_stamp_for_value[i] == -1
                             or min_num_stamp_for_value[i - stamp] + 1 < min_num_stamp_for_value[i]):
                    min_num_stamp_for_value[i] = min_num_stamp_for_value[i - stamp] + 1
            if min_num_stamp_for_value[i] == -1:
                out_print(i - 1)
                break

if __name__ == '__main__':
    main()
