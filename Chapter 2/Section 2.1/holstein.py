"""
ID: hsfncd31
LANG: PYTHON3
TASK: holstein
"""
import os
import typing
import itertools


def main():
    base_filename = 'test' if os.name == 'nt' else 'holstein'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        v = int(get_line())
        require = [int(s) for s in get_line().split()]
        g = int(get_line())
        feeds = [list(map(int, get_line().split())) for _ in range(g)]

        # weird that typing.List[int] can't suppress warning of return tuple(include_feeds)
        include_feeds: typing.List = []
        vitamin_fed = [0] * v
        answer = None
        print(feeds)

        def dfid(remain: int, position: int) -> typing.Union[typing.Tuple[int], None]:
            """ depth first iterative deepening """
            if g - position < remain:
                # not enough feed
                return None
            for i in range(position, g):
                include_feeds.append(i)
                if remain == 1:
                    ok = True
                    for j in range(v):
                        if vitamin_fed[j] + feeds[i][j] < require[j]:
                            ok = False
                            break
                    if ok:
                        return tuple(include_feeds)
                else:
                    for j in range(v):
                        vitamin_fed[j] += feeds[i][j]
                    result = dfid(remain - 1, i + 1)
                    if result:
                        return result
                    for j in range(v):
                        vitamin_fed[j] -= feeds[i][j]
                include_feeds.pop()
            return None

        for depth in itertools.count(1):
            answer = dfid(depth, 0)
            if answer:
                break
        out_print(len(answer), *(x + 1 for x in answer))


if __name__ == '__main__':
    main()
