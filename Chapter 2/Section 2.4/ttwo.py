"""
ID: hsfncd31
LANG: PYTHON3
TASK: ttwo
Time Limit Exceeded at Case#7
"""
import os
import typing
import collections


def main():
    base_filename = 'test' if os.name == 'nt' else 'ttwo'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        size = 10, 10
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        farmer_pos, cow_pos = None, None
        farmer_dir, cow_dir = 0, 0

        grid = [get_line() for _ in range(size[0])]

        def move(pos: typing.Tuple[int, int], dir: int) -> typing.Tuple[typing.Tuple[int, int], int]:
            forward_pos = pos[0] + directions[dir][0], pos[1] + directions[dir][1]
            if 0 <= forward_pos[0] < size[0] and 0 <= forward_pos[1] < size[1]\
                    and grid[forward_pos[0]][forward_pos[1]] != '*':
                return forward_pos, dir
            else:
                return pos, (dir + 1) % len(directions)

        for row in range(len(grid)):
            if 'F' in grid[row]:
                farmer_pos = (row, grid[row].index('F'))
            if 'C' in grid[row]:
                cow_pos = (row, grid[row].index('C'))
        # { (farmer position, farmer direction, cow position, cow direction) }
        visited = set()
        count = 0
        while farmer_pos != cow_pos:
            print((farmer_pos, farmer_dir, cow_pos, cow_dir), visited)
            if (farmer_pos, farmer_dir, cow_pos, cow_dir) in visited:
                break
            visited.add((farmer_pos, farmer_dir, cow_pos, cow_dir))
            farmer_pos, farmer_dir = move(farmer_pos, farmer_dir)
            cow_pos, cow_dir = move(cow_pos, cow_dir)
            count += 1
        out_print(count if farmer_pos == cow_pos else 0)


if __name__ == '__main__':
    main()
