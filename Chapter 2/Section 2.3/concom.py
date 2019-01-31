"""
ID: hsfncd31
LANG: PYTHON3
TASK: concom
Time Limit Exceeded at Case#7
"""
import os
import typing
import collections


def main():
    base_filename = 'test' if os.name == 'nt' else 'concom'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        man_num_company = 100
        origin_share = [[0] * (man_num_company + 1) for _ in range(man_num_company + 1)]
        effective_share = [[0] * (man_num_company + 1) for _ in range(man_num_company + 1)]
        owns = [[False] * (man_num_company + 1) for _ in range(man_num_company + 1)]

        for _ in range(n):
            i, j, p = map(int, get_line().split())
            origin_share[i][j] += p
            effective_share[i][j] += p

        # {(father, child)}
        newly_owned = set()
        for i in range(1, man_num_company + 1):
            for j in range(1, man_num_company + 1):
                if effective_share[i][j] >= 50:
                    newly_owned.add((i, j))
                    owns[i][j] = True
        while len(newly_owned):
            i, j = newly_owned.pop()
            for k in range(1, man_num_company + 1):
                # add j's share to i
                effective_share[i][k] += origin_share[j][k]
                if effective_share[i][k] >= 50 and not owns[i][k]:
                    newly_owned.add((i, k))
                    owns[i][k] = True
            for k in range(1, man_num_company + 1):
                # father owns j, too
                if owns[k][i] and not owns[k][j]:
                    newly_owned.add((k, j))
                    owns[k][j] = True

        for i in range(1, man_num_company + 1):
            for j in range(1, man_num_company + 1):
                if owns[i][j] and i != j:
                    out_print(i, j)


if __name__ == '__main__':
    main()
