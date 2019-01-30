"""
ID: hsfncd31
LANG: PYTHON3
TASK: subset
"""
import os
import typing


def roman_numeral(x: int) -> str:
    letters = ('IV', 'XL', 'CD', 'M')
    """ I II III IV V VI VII VIII IX X """
    components = []
    for power in range(3, 0 - 1, -1):
        digit = x % 10 ** (power + 1) // 10 ** power
        component = ''
        if digit <= 3:
            component = letters[power][0] * digit
        elif digit == 4:
            component = letters[power][0] + letters[power][1]
        elif digit <= 8:
            component = letters[power][1] + letters[power][0] * (digit - 5)
        else:
            # digit == 9
            component = letters[power][0] + letters[power + 1][0]
        components.append(component)
    return ''.join(components)


def main():
    base_filename = 'test' if os.name == 'nt' else 'subset'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        max_n = 39
        max_diff = sum(range(max_n + 1))
        # bigger minus smaller
        state = [0] * (max_diff + 1)
        state[1] = 1
        for i in range(2, n + 1):
            new_state = [0] * len(state)
            for j in range(len(state)):
                new_state[abs(j - i)] += state[j]
                if j + i < len(state):
                    new_state[j + i] += state[j]
            state = new_state
        out_print(state[0])

if __name__ == '__main__':
    main()
