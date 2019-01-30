"""
ID: hsfncd31
LANG: PYTHON3
TASK: prefix
"""
import os
import typing
import string
import collections


def main():
    base_filename = 'test' if os.name == 'nt' else 'prefix'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        primitives = set()
        while True:
            new_primitives = get_line().split()
            if new_primitives == ['.']:
                break
            primitives.update(new_primitives)
        max_primitive_length = 10
        max_prefix_length = 0
        current_position = 0
        # [bool], whether the position is possible prefix, the prefix up to this place is already consumed
        ok_positions = collections.deque((True,), max_primitive_length)
        prefix_buffer = collections.deque(('',), max_primitive_length + 1)
        for line in infile:
            for c in line.rstrip('\n'):
                prefix_buffer.append(c)
                # print(ok_positions, prefix_buffer)
                ok = False
                for i in range(len(ok_positions)):
                    if ok_positions[i]\
                            and ''.join(prefix_buffer[j] for j in range(i + 1, len(prefix_buffer))) in primitives:
                        ok = True
                        break
                if ok:
                    max_prefix_length = current_position + 1
                current_position += 1
                ok_positions.append(ok)
            if all(not ok for ok in ok_positions):
                break
        out_print(max_prefix_length)


if __name__ == '__main__':
    main()
