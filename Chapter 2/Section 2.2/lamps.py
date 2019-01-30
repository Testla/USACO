"""
ID: hsfncd31
LANG: PYTHON3
TASK: lamps
"""
import os
import typing
import itertools


def count_1_bits(x: int) -> int:
    result = 0
    while x:
        result += 1
        x &= x - 1
    return result


def button1(lamps: typing.List[bool]) -> None:
    for i in range(len(lamps)):
        lamps[i] = not lamps[i]


def button2(lamps: typing.List[bool]) -> None:
    for i in range(0, len(lamps), 2):
        lamps[i] = not lamps[i]


def button3(lamps: typing.List[bool]) -> None:
    for i in range(1, len(lamps), 2):
        lamps[i] = not lamps[i]


def button4(lamps: typing.List[bool]) -> None:
    for i in range(0, len(lamps), 3):
        lamps[i] = not lamps[i]


def main():
    base_filename = 'test' if os.name == 'nt' else 'lamps'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        c = int(get_line())
        on_lamps = list(map(int, get_line().split()[:-1]))
        off_lamps = list(map(int, get_line().split()[:-1]))
        buttons = (button1, button2, button3, button4)
        possible_configurations = set()
        for state in range(2 ** len(buttons)):
            # enumerate all possible states, 1-bit means that button is pressed odd times
            num_odd = count_1_bits(state)
            if num_odd > c or num_odd % 2 != c % 2:
                continue
            lamps = [True] * n
            for p in range(len(buttons)):
                if state & (1 << p):
                    buttons[p](lamps)
            if all(lamps[on_lamp - 1] for on_lamp in on_lamps) and all(not lamps[off_lamp - 1] for off_lamp in off_lamps):
                possible_configurations.add(''.join('1' if lamp else '0' for lamp in lamps))
        out_print(*(sorted(possible_configurations) if possible_configurations else ('IMPOSSIBLE',)), sep='\n')



if __name__ == '__main__':
    main()
