"""
ID: hsfncd31
LANG: PYTHON3
TASK: humble
"""
import os
import typing
import heapq
import itertools


def main():
    base_filename = 'test' if os.name == 'nt' else 'humble'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        _, n = map(int, get_line().split())
        primes = [int(s) for s in get_line().split()]
        heap = primes.copy()
        heapq.heapify(heap)
        # maintains n smallest humble numbers
        # used to prevent the heap from growing too big
        # stores negatives of the numbers to get a max heap
        smallest_humble_numbers = list(-prime for prime in itertools.islice(primes, min(len(primes), n)))
        heapq.heapify(smallest_humble_numbers)
        for _ in range(n - 1):
            humble_number = heapq.heappop(heap)
            # start multiplying from the biggest prime factor to avoid duplicate
            for i in range(len(primes) - 1, 0 - 1, -1):
                if humble_number % primes[i] == 0:
                    for j in range(i, len(primes)):
                        new_humble_number = humble_number * primes[j]
                        if len(smallest_humble_numbers) < n:
                            heapq.heappush(smallest_humble_numbers, -new_humble_number)
                        elif new_humble_number >= -smallest_humble_numbers[0]:
                                break
                        else:
                            heapq.heapreplace(smallest_humble_numbers, -new_humble_number)
                        heapq.heappush(heap, new_humble_number)
                    break
        out_print(heapq.heappop(heap))

if __name__ == '__main__':
    main()
