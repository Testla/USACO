"""
ID: hsfncd31
LANG: PYTHON3
TASK: spin
"""
import os
import typing


def main():
    base_filename = 'test' if os.name == 'nt' else 'spin'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        num_wheels = 5
        # The period of any wheel should be less than or equal to 360.
        # So we simple calculate them all.
        # state[i][j]: At time i whether angle j is passable or not
        total_angle = 360
        max_period = 360
        state = [[True] * total_angle for _ in range(max_period)]
        for _ in range(num_wheels):
            input_numbers = list(map(int, get_line().split()))
            speed = input_numbers[0]
            wedges = [(input_numbers[i], input_numbers[i] + input_numbers[i + 1])
                      for i in range(2, len(input_numbers), 2)]
            wedges.sort()
            wedges = [
                (-1, max(-1, wedges[-1][1] - total_angle)),
                *wedges,
                (total_angle, total_angle),
            ]
            print(speed, wedges)
            for t in range(max_period):
                for i in range(len(wedges) - 1):
                    for angle in range(wedges[i][1] + 1, wedges[i + 1][0]):
                        state[t][(angle + t * speed) % total_angle] = False

        found = False
        for t in range(max_period):
            if any(state[t]):
                out_print(t)
                found = True
                break
        if not found:
            out_print('none')


if __name__ == '__main__':
    main()
