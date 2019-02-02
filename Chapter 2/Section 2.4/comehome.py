"""
ID: hsfncd31
LANG: PYTHON3
TASK: comehome
"""
import os
import typing
import string


def main():
    base_filename = 'test' if os.name == 'nt' else 'comehome'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        p = int(get_line())
        all_labels = string.ascii_uppercase + string.ascii_lowercase
        distance = [[-1] * len(all_labels) for _ in range(len(all_labels))]

        for _ in range(p):
            a, b, d = get_line().split()
            a, b = (all_labels.index(c) for c in (a, b))
            d = int(d)
            if a != b and distance[a][b] == -1 or d < distance[a][b]:
                distance[a][b] = distance[b][a] = d

        # Floyd-Warshall
        for k in range(len(all_labels)):
            for i in range(len(all_labels)):
                for j in range(len(all_labels)):
                    if distance[i][k] != -1 and distance[k][j] != -1\
                            and (distance[i][j] == -1 or distance[i][k] + distance[k][j] < distance[i][j]):
                        distance[i][j] = distance[i][k] + distance[k][j]

        closet_pasture, min_distance = min(
            ((i, d) for i, d in enumerate(distance[all_labels.index('Z')])
             if d != -1 and i < len(string.ascii_uppercase) - 1),
            key=lambda x: x[1])
        out_print(all_labels[closet_pasture], min_distance)

if __name__ == '__main__':
    main()
