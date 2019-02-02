"""
ID: hsfncd31
LANG: PYTHON3
TASK: maze1
Time Limit Exceeded in Case#7
"""
import os
import typing
import collections


def main():
    base_filename = 'test' if os.name == 'nt' else 'maze1'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        w, h = map(int, get_line().split())
        maze = [get_line() for _ in range(h * 2 + 1)]
        # The square next to an exit, actually.
        # May be the same square(on the corner), so set is used.
        exits = set()

        # find exits
        for i in range(w):
            if maze[0][i * 2 + 1] == ' ':
                exits.add((0, i))
            if maze[h * 2][i * 2 + 1] == ' ':
                exits.add((h - 1, i))
        for i in range(h):
            if maze[i * 2 + 1][0] == ' ':
                exits.add((i, 0))
            if maze[i * 2 + 1][w * 2] == ' ':
                exits.add((i, w - 1))

        # minimum distance from each exit
        min_distances = []
        directions = ((-1, 0), (0, -1), (0, 1), (1, 0))
        for ex1t in exits:
            # also used as visited
            distance = [[None] * w for _ in range(h)]
            distance[ex1t[0]][ex1t[1]] = 1
            q = collections.deque((ex1t,))
            while len(q):
                current = q.popleft()
                for dir in directions:
                    neighbour = current[0] + dir[0], current[1] + dir[1]
                    if 0 <= neighbour[0] < h and 0 <= neighbour[1] < w\
                            and distance[neighbour[0]][neighbour[1]] is None\
                            and maze[current[0] * 2 + 1 + dir[0]][current[1] * 2 + 1 + dir[1]] == ' ':
                        distance[neighbour[0]][neighbour[1]] = distance[current[0]][current[1]] + 1
                        q.append(neighbour)
            min_distances.append(distance)

        out_print(max(
            min(min_distance[i][j] for min_distance in min_distances)
            for i in range(h) for j in range(w)))


if __name__ == '__main__':
    main()
