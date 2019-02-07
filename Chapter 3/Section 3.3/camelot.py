"""
ID: hsfncd31
LANG: PYTHON3
TASK: camelot
TLE at Case#4
"""
import os
import typing
import collections
import itertools


def main():
    base_filename = 'test' if os.name == 'nt' else 'camelot'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        r, c = map(int, get_line().split())
        chess = []
        strings = infile.read().split()
        for i in range(0, len(strings), 2):
            column = ord(strings[i]) - ord('A')
            row = r - int(strings[i + 1])
            chess.append((row, column))
        king = chess[0]
        knights = chess[1:]
        directions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))

        # distance between any two points for a knight, four dimensional array
        knight_distance = [[None] * c for _ in range(r)]
        for row in range(r):
            for column in range(c):
                distance = [[None] * c for _ in range(r)]
                distance[row][column] = 0
                q = collections.deque(((row, column),))
                while len(q):
                    current = q.popleft()
                    for d in directions:
                        to = current[0] + d[0], current[1] + d[1]
                        if not (0 <= to[0] < r and 0 <= to[1] < c):
                            continue
                        if distance[to[0]][to[1]] is None:
                            distance[to[0]][to[1]] = distance[current[0]][current[1]] + 1
                            q.append(to)
                knight_distance[row][column] = distance

        answer = None
        for gathering_point in itertools.product(range(r), range(c)):
            sum_knights_move = sum(
                knight_distance[gathering_point[0]][gathering_point[1]][knight[0]][knight[1]] for knight in knights)
            for meeting_point, meet_knight in itertools.product(itertools.product(range(r), range(c)), knights):
                old_knight_move =\
                    knight_distance[gathering_point[0]][gathering_point[1]][meet_knight[0]][meet_knight[1]]
                king_move = max(abs(king[0] - meeting_point[0]), abs(king[1] - meeting_point[1]))
                knight_meeting_move =\
                    knight_distance[meeting_point[0]][meeting_point[1]][meet_knight[0]][meet_knight[1]]
                post_meeting_move =\
                    knight_distance[gathering_point[0]][gathering_point[1]][meeting_point[0]][meeting_point[1]]
                total_move = sum_knights_move - old_knight_move + knight_meeting_move + king_move + post_meeting_move
                if answer is None or total_move < answer:
                    answer = total_move
            # in case of there's no knight, the king moves on his own
            if len(knights) == 0:
                king_alone_move = max(abs(king[0] - gathering_point[0]), abs(king[1] - gathering_point[1]))
                if answer is None or king_alone_move < answer:
                    answer = king_alone_move

        out_print(answer)


if __name__ == '__main__':
    main()
