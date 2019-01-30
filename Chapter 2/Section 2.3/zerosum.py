"""
ID: hsfncd31
LANG: PYTHON3
TASK: zerosum
Time Limit Exceeded in Case#7
"""
import os
import typing


def main():
    base_filename = 'test' if os.name == 'nt' else 'zerosum'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        operators = ('+', '-', ' ')
        expression = [str((x + 2) // 2) for x in range(n * 2 - 1)]
        answer = []
        for state in range(3 ** (n - 1)):
            for power in range(n - 1):
                operator = operators[state % 3 ** (power + 1) // 3 ** power]
                expression[power * 2 + 1] = operator
            joined_expression = ''.join(expression)
            print(joined_expression)
            if eval(joined_expression.replace(' ', '')) == 0:
                answer.append(joined_expression)
        out_print(*sorted(answer), sep='\n')


if __name__ == '__main__':
    main()
