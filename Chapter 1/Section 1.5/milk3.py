"""
ID: hsfncd31
LANG: PYTHON3
TASK: milk3
"""
import os
import typing


def main():
    base_filename = 'test' if os.name == 'nt' else 'milk3'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        full = tuple(map(int, get_line().split()))
        answer = {full[2]}
        visited = set()

        def dfs(state: typing.List[int]):
            if state[0] == 0:
                answer.add(state[2])
            for fr0m in range(0, 3):
                for to in range(0, 3):
                    if fr0m != to:
                        move = min(state[fr0m], full[to] - state[to])
                        if move == 0:
                            continue
                        state[fr0m] -= move
                        state[to] += move
                        t = tuple(state)
                        if t not in visited:
                            visited.add(t)
                            dfs(state)
                        state[fr0m] += move
                        state[to] -= move

        dfs([0, 0, full[2]])
        out_print(*sorted(answer))


if __name__ == '__main__':
    main()
