"""
ID: hsfncd31
LANG: PYTHON3
TASK: race3
"""
import os
import typing
import itertools
import collections


def main():
    base_filename = 'test' if os.name == 'nt' else 'race3'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        # { vertex: [neighbor] }
        n = 0
        graph = collections.defaultdict(set)
        reverse_graph = collections.defaultdict(set)
        while True:
            numbers = [int(s) for s in get_line().split()]
            if numbers[0] == -1:
                break
            for neighbor in itertools.islice(numbers, len(numbers) - 1):
                graph[n].add(neighbor)
                reverse_graph[neighbor].add(n)
            n += 1
        n -= 1

        def search(start: int, stop_at: typing.Union[int, None], graph: typing.Mapping[int, typing.Set[int]])\
                -> typing.Set[int]:
            """ start and stop_at(if provided) included """
            result = { start }
            q = collections.deque((start,))
            while len(q):
                current = q.popleft()
                for neighbor in graph[current]:
                    if neighbor != stop_at and neighbor not in result:
                        result.add(neighbor)
                        q.append(neighbor)
            if stop_at:
                result.add(stop_at)
            return result

        unavoidable_points = []
        splitting_points = []
        source = 0
        sink = n
        for vertex in range(1, n):
            first_points = search(source, vertex, graph)
            unavoidable = bool(sink not in first_points)
            if unavoidable:
                unavoidable_points.append(vertex)

            # like the do-while false
            while True:
                # ensure that the first part is well-formed
                # Every point in the course can be reached from the start.
                # Already satisfied in origin course.
                # The finish can be reached from each point in the course.
                # Point 4 of Case#5 can be reached from 46 but is splitting point, so >= is used.
                if not (search(vertex, None, reverse_graph) >= first_points):
                    break
                # The finish has no outgoing arrows.
                if not ((graph[vertex] & first_points) <= { vertex }):
                    break

                # ensure that the second part is well-formed
                second_points = (set(range(n + 1)) - first_points) | { vertex }
                # Every point in the course can be reached from the start.
                if not (search(vertex, None, graph) >= second_points):
                    break
                # The finish can be reached from each point in the course.
                if not (search(sink, vertex, reverse_graph) >= second_points):
                    break
                # The finish has no outgoing arrows.
                # Already satisfied in origin course.

                # additional requirements
                # (1) have no common arrows
                have_common_arrow = False
                for first_point in (first_points - { vertex }):
                    if graph[first_point] & (second_points - { vertex })\
                            or reverse_graph[first_point] & (second_points - { vertex }):
                        have_common_arrow = True
                        break
                if have_common_arrow:
                    break
                # (2) have S as their only common point
                # Don't quite understand, already satisfied by definition of second_points?
                splitting_points.append(vertex)
                break

        out_print(len(unavoidable_points), *unavoidable_points)
        out_print(len(splitting_points), *splitting_points)


if __name__ == '__main__':
    main()
