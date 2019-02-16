"""
ID: hsfncd31
LANG: PYTHON3
TASK: buylow
TLE at Case#10
"""
import os
import typing


class BinaryIndexedTree(object):
    """ zero-based version """
    def __init__(self, size: int):
        self.elements = [0] * size
        self.data = [0] * size

    def __str__(self):
        return self.elements.__str__()

    def __repr__(self):
        return self.elements.__repr__()

    def update(self, index: int, new_value: int) -> None:
        if self.elements[index] == new_value:
            return
        delta = new_value - self.elements[index]
        self.elements[index] = new_value
        while index < len(self.data):
            self.data[index] += delta
            index |= index + 1

    def prefix_sum(self, end: int) -> int:
        end -= 1
        result = 0
        while end >= 0:
            result += self.data[end]
            end = (end & (end + 1)) - 1
        return result


def main():
    base_filename = 'test' if os.name == 'nt' else 'buylow'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        origin_prices = [int(s) for s in infile.read().split()]
        price_to_id = dict((origin_price, i) for i, origin_price in enumerate(reversed(sorted(set(origin_prices)))))
        prices = [price_to_id[origin_price] for origin_price in origin_prices]

        # dp[length - 1][last_price]: number of possible sequences
        dp = [BinaryIndexedTree(len(prices))]
        for price in prices:
            if dp[-1].prefix_sum(price):
                dp.append(BinaryIndexedTree(len(prices)))
            for length in range(len(dp) - 1, 1 - 1, -1):
                dp[length].update(price, dp[length - 1].prefix_sum(price))
            dp[0].update(price, 1)
            # print(price)
            # print(*enumerate(dp), sep='\n', end='\n\n')

        out_print(len(dp), dp[-1].prefix_sum(n))


if __name__ == '__main__':
    main()
