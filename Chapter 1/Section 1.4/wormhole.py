"""
ID: hsfncd31
LANG: PYTHON3
TASK: wormhole
"""
import os
import typing
import collections
import bisect


def find_pairing(done: int, buffer: typing.List[typing.Union[int, None]]) -> typing.Generator[typing.List[typing.Union[int, None]], None, None]:
    first_unpaired = None
    for i in range(len(buffer)):
        if buffer[i] is None:
            if first_unpaired is None:
                first_unpaired = i
            else:
                buffer[first_unpaired] = i
                buffer[i] = first_unpaired

                if done + 2 == len(buffer):
                    yield buffer
                else:
                    yield from find_pairing(done + 2, buffer)

                buffer[first_unpaired] = None
                buffer[i] = None


def all_pairings(n: int) -> typing.Generator[typing.List[int], None, None]:
    """ pairings share a common buffer, use immediately or keep a copy """
    buffer = [None] * n
    yield from find_pairing(0, buffer)


def main():
    base_filename = 'test' if os.name == 'nt' else 'wormhole'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        wormholes = [list(map(int, get_line().split())) for _ in range(n)]
        # { y: (x, wormhole_index) }
        wormholes_on_horizontal_lines = collections.defaultdict(list)
        for i, wormhole in enumerate(wormholes):
            wormholes_on_horizontal_lines[wormhole[1]].append((wormhole[0], i))
        for v in wormholes_on_horizontal_lines.values():
            v.sort()

        def find_next(w: typing.List[int]) -> typing.Union[int, None]:
            line = wormholes_on_horizontal_lines[w[1]]
            position = bisect.bisect_right(line, (w[0], i))
            return None if position == len(line) else line[position][1]
        # wormhole number or None, the place if Bessie exits and starts from a certain wormhole
        next_position = [find_next(wormhole) for wormhole in wormholes]

        def test_pairing(pairing: typing.List[int]) -> bool:
            entered = [False] * n  # save some processing
            for i in range(len(pairing)):
                # i is the first wormhole entered
                if not entered[i]:
                    current = i
                    enterable = set()
                    while current is not None:
                        # print(pairing, current, entered, enterable)
                        entered[current] = True
                        if current in enterable:
                            return True
                        enterable.add(current)
                        current = pairing[current]
                        current = next_position[current]
                        # import time
                        # time.sleep(0.5)
            return False
        # for pairing in all_pairings(4):
        #     print(pairing)
        out_print(sum(1 if test_pairing(pairing) else 0 for pairing in all_pairings(n)))


if __name__ == '__main__':
    main()
