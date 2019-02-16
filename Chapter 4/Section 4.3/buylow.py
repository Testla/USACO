"""
ID: hsfncd31
LANG: PYTHON3
TASK: buylow
Referred to the official solution.
"""
import os
import typing
import bisect


def main():
    base_filename = 'test' if os.name == 'nt' else 'buylow'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        _ = int(get_line())
        prices = [int(s) for s in infile.read().split()]

        # use negative of the trailing number so we can keep a "descending" sequence
        max_trailing_of_length = []
        max_length = []
        for price in prices:
            i = bisect.bisect_left(max_trailing_of_length, -price)
            if i == len(max_trailing_of_length):
                max_trailing_of_length.append(-price)
            else:
                max_trailing_of_length[i] = min(max_trailing_of_length[i], -price)
            max_length.append(i + 1)

        num_distinct = []
        for i in range(len(prices)):
            if max_length[i] == 1:
                num_distinct.append(1)
                continue
            last = None
            sum_num_distinct = 0
            for j in range(i - 1, 0 - 1, -1):
                if max_length[j] == max_length[i] - 1 and prices[j] > prices[i] and prices[j] != last:
                    sum_num_distinct += num_distinct[j]
                    # Too avoid duplicate.
                    # We know that if two same price has same max_length(max_length[i] - 1 here)
                    # then no different price between them can has the same max_length,
                    # (if a higher price has same max_length, the latter same price's max_length will be that plus one;
                    #  and a lower price must has bigger max_length than the former same price),
                    # so if we consider only a specific max_length, same price must appear consecutively.
                    last = prices[j]
            num_distinct.append(sum_num_distinct)

        max_max_length = max(max_length)
        answer = 0
        last = None
        # count reversely and ignore same trailing price
        for i in reversed(range(len(num_distinct))):
            if max_length[i] == max_max_length and prices[i] != last:
                answer += num_distinct[i]
                last = prices[i]

        out_print(max_max_length, answer)


if __name__ == '__main__':
    main()
