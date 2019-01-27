"""
ID: hsfncd31
LANG: PYTHON3
TASK: milk
"""
import os
import typing


def main():
    base_filename = 'test' if os.name == 'nt' else 'milk'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n, m = map(int, get_line().split())
        total_price = 0
        farmers = [tuple(map(int, get_line().split())) for _ in range(m)]
        for farmer in sorted(farmers):
            amount = min(n, farmer[1])
            total_price += amount * farmer[0]
            n -= amount
            if n == 0:
                break
        out_print(total_price)

if __name__ == '__main__':
    main()
