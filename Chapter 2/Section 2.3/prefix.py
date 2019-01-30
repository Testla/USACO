"""
ID: hsfncd31
LANG: PYTHON3
TASK: prefix
"""
import os
import typing
import string
import collections


class Trie(object):
    # Using set to check if primitive matches exceeds time limit in Case#6,
    # so try Trie.
    # 0.986 secs, that's close!

    def __init__(self):
        max_num_primitives = 200
        max_primitive_length = 10
        dictionary_size = len(string.ascii_uppercase)
        self.nodes = [[None] * dictionary_size for _ in range(max_num_primitives * max_primitive_length + 1)]
        self.is_word_end = [False] * len(self.nodes)
        self.num_used_nodes = 1

    @staticmethod
    def char_index(c: str) -> int:
        return ord(c) - ord('A')

    def add(self, s: str) -> None:
        current = 0
        for c in s:
            if self.nodes[current][Trie.char_index(c)] is None:
                self.nodes[current][Trie.char_index(c)] = self.num_used_nodes
                self.num_used_nodes += 1
            current = self.nodes[current][Trie.char_index(c)]
        self.is_word_end[current] = True

    def next(self, x: typing.Union[int, None], c: str) -> typing.Union[int, None]:
        return None if x is None else self.nodes[x][Trie.char_index(c)]

    def check(self, x: typing.Union[int, None]) -> bool:
        return False if x is None else self.is_word_end[x]


def main():
    base_filename = 'test' if os.name == 'nt' else 'prefix'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        primitives = Trie()
        while True:
            new_primitives = get_line().split()
            if new_primitives == ['.']:
                break
            for new_primitive in new_primitives:
                primitives.add(new_primitive)
        max_primitive_length = 10
        max_prefix_length = 0
        current_position = 0
        # [bool], whether the position is possible prefix, the prefix up to this place is consumed
        prefix_states = collections.deque((0,), max_primitive_length + 1)
        for line in infile:
            for c in line.rstrip('\n'):
                ok = False
                for i in range(len(prefix_states)):
                    prefix_states[i] = primitives.next(prefix_states[i], c)
                    if primitives.check(prefix_states[i]):
                        ok = True
                if ok:
                    max_prefix_length = current_position + 1
                prefix_states.append(0 if ok else None)
                current_position += 1
            if all(prefix_state is None for prefix_state in prefix_states):
                break
        out_print(max_prefix_length)


if __name__ == '__main__':
    main()
