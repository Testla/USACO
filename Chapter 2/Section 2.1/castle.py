"""
ID: hsfncd31
LANG: PYTHON3
TASK: castle
"""
import os
import typing
import collections


def main():
    base_filename = 'test' if os.name == 'nt' else 'castle'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        m, n = map(int, get_line().split())
        castle = [[int(s) for s in get_line().split()] for _ in range(n)]
        directions = ((0, -1), (-1, 0), (0, 1), (1, 0))
        room_of = [[None] * m for _ in range(n)]
        # { room_index: [module] }
        rooms = collections.defaultdict(list)
        num_rooms = 0

        visited = [[False] * m for _ in range(n)]

        def flood_fill(i: int, j: int) -> None:
            visited[i][j] = True
            room_of[i][j] = num_rooms
            rooms[num_rooms].append((i, j))
            for d in range(len(directions)):
                di, dj = i + directions[d][0], j + directions[d][1]
                if not (0 <= di < n and 0 <= dj < m)\
                        or visited[di][dj]\
                        or castle[i][j] & (1 << d):
                    continue
                flood_fill(di, dj)

        for i in range(n):
            for j in range(m):
                if not visited[i][j]:
                    flood_fill(i, j)
                    num_rooms += 1

        # just enumerate all walls
        largest_after_removed = 0
        wall_to_remove = None
        for j in range(m):
            for i in range(n - 1, 0 - 1, -1):
                try_directions = (1, 2)
                for d in try_directions:
                    di, dj = i + directions[d][0], j + directions[d][1]
                    if not (0 <= di < n and 0 <= dj < m) or room_of[i][j] == room_of[di][dj]:
                        continue
                    area = len(rooms[room_of[i][j]]) + len(rooms[room_of[di][dj]])
                    if area > largest_after_removed:
                        largest_after_removed = area
                        wall_to_remove = i + 1, j + 1, 'N' if d == 1 else 'E'

        out_print(num_rooms)
        out_print(max(len(v) for v in rooms.values()))
        out_print(largest_after_removed)
        out_print(*wall_to_remove)

if __name__ == '__main__':
    main()
