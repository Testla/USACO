"""
ID: hsfncd31
LANG: PYTHON3
TASK: fence6
"""
import os
import typing
import collections


def main():
    base_filename = 'test' if os.name == 'nt' else 'fence6'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        # { frozenset(fences): vertex_number }
        vertices = collections.defaultdict(lambda: len(vertices))
        # { v: { v2: l } }
        graph = collections.defaultdict(dict)
        fence_lengths = []
        for _ in range(n):
            s, l, n1, n2 = map(int, get_line().split())
            end1_fences = frozenset((s, *(int(x) for x in get_line().split())))
            vertex1 = vertices[end1_fences]
            end2_fences = frozenset((s, *(int(x) for x in get_line().split())))
            vertex2 = vertices[end2_fences]
            if len(end1_fences & end2_fences) > 1:
                # two fences share same endpoints
                print(s, l, end1_fences & end2_fences)
            graph[vertex1][vertex2] = min(graph[vertex1].get(vertex2, l), l)
            graph[vertex2][vertex1] = min(graph[vertex2].get(vertex1, l), l)
            fence_lengths.append(l)

        stack_position = [-1] * len(vertices)
        stack = []
        length_up_to = [0]
        global answer
        answer = None

        def dfs(current: int, previous: typing.Union[None, int]) -> None:
            global answer
            stack_position[current] = len(stack)
            stack.append(current)
            for neighbour, length in graph[current].items():
                if neighbour != previous:
                    if stack_position[neighbour] != -1:
                        perimeter = length_up_to[-1] - length_up_to[stack_position[neighbour]] + length
                        if answer is None or perimeter < answer:
                            answer = perimeter
                    else:
                        length_up_to.append(length_up_to[-1] + length)
                        dfs(neighbour, current)
                        length_up_to.pop()
            stack.pop()
            stack_position[current] = -1

        dfs(0, None)
        # assume that there is only one connected component
        out_print(answer)

if __name__ == '__main__':
    main()
