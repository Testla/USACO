"""
ID: hsfncd31
LANG: PYTHON3
TASK: contact
Time Limit Exceeded in Case#7
"""
import os
import typing
import collections
import itertools


class Trie(object):
    # Ad-hoc implementation

    def __init__(self):
        dictionary_size = len('01')
        max_pattern_length = 12
        self.nodes = [[0] * dictionary_size for _ in range(
            (dictionary_size ** (max_pattern_length + 1) - 1) // (dictionary_size - 1) + 1)]
        self.num_used_nodes = 1
        self.string_of_node = [''] * len(self.nodes)
        self.num_occurrence = [0] * len(self.nodes)

    @staticmethod
    def char_index(c: str) -> int:
        return ord(c) - ord('0')

    def next(self, x: int, c: str) -> int:
        # actually always returns int, just to suppress PyCharm's warning
        i = ord(c) - ord('0')
        if self.nodes[x][i] == 0:
            self.nodes[x][i] = self.num_used_nodes
            self.string_of_node[self.num_used_nodes] = self.string_of_node[x] + c
            self.num_used_nodes += 1
        self.num_occurrence[self.nodes[x][i]] += 1
        return self.nodes[x][i]


def main():
    base_filename = 'test' if os.name == 'nt' else 'contact'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        a, b, n = map(int, get_line().split())
        trie = Trie()
        q = collections.deque((), b)
        import time
        start_time = time.time()
        for line in infile:
            for c in line.rstrip('\n'):
                q.append(0)
                for i in range(len(q)):
                    q[i] = trie.next(q[i], c)
        print(time.time() - start_time)
        # { num_occurrence: [string] }
        string_of_num_occurrence = collections.defaultdict(list)
        for s, num_occurrence in zip(trie.string_of_node, trie.num_occurrence):
            if len(s) < a:
                continue
            string_of_num_occurrence[num_occurrence].append(s)
        print(time.time() - start_time)
        for num_occurrence, strings in itertools.islice(reversed(sorted(string_of_num_occurrence.items())), n):
            out_print(num_occurrence)
            strings.sort(key=lambda s: (len(s), s))
            for i in range(0, len(strings), 6):
                out_print(*strings[i: i + 6])

if __name__ == '__main__':
    main()
