"""
ID: hsfncd31
LANG: PYTHON3
TASK: msquare
TLE in Case#8
"""
import os
import typing
import itertools
import math

Factorials = [math.factorial(i) for i in range(10)]


def cantor_expansion(permutation: typing.List[int]) -> int:
    result = 0
    for i in range(len(permutation)):
        result += Factorials[len(permutation) - 1 - i]\
                  * sum(1 if permutation[j] < permutation[i] else 0 for j in range(i + 1, len(permutation)))
    return result


def apply_transformation(board: typing.List[int], transformation: typing.List[int]) -> typing.List[int]:
    return [board[p - 1] for p in transformation]


def main():
    base_filename = 'test' if os.name == 'nt' else 'msquare'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        target = [int(s) - 1 for s in get_line().split()]
        transformations = [
            [8, 7, 6, 5, 4, 3, 2, 1],
            [4, 1, 2, 3, 6, 7, 8, 5],
            [1, 7, 2, 4, 5, 3, 6, 8],
        ]
        # [(board, precedent_index, transformation)]
        states = [(list(range(8)), -1, -1)]
        visited = [False] * math.factorial(len(transformations[0]))
        if target == states[0][0]:
            out_print('0\n')
            return
        visited[cantor_expansion(states[0][0])] = True
        for p in itertools.count(0):
            for t in range(len(transformations)):
                board_after = apply_transformation(states[p][0], transformations[t])
                cantor_board_after = cantor_expansion(board_after)
                if visited[cantor_board_after]:
                    continue
                visited[cantor_board_after] = True
                if board_after == target:
                    sequence = [t]
                    while p != 0:
                        sequence.append(states[p][2])
                        p = states[p][1]
                    out_print(len(sequence))
                    out_print(''.join('ABC'[i] for i in reversed(sequence)))
                    return
                states.append((board_after, p, t))


if __name__ == '__main__':
    main()
