"""
ID: hsfncd31
LANG: PYTHON3
TASK: sprime
"""
import os
import typing
import math


def euler_sieve(upper_bound: int) -> typing.List[int]:
    """
    find prime numbers no bigger than upper_bound
    uses O(n) time and O(n) space
    """
    primes = []
    is_prime = [True] * (upper_bound + 1)
    for i in range(2, upper_bound):
        if is_prime[i]:
            primes.append(i)
        for prime in primes:
            if i * prime > upper_bound:
                break
            is_prime[i * prime] = False
            if i % prime == 0:
                break
    return primes


def is_prime(x: int, primes: typing.List[int]) -> bool:
    for prime in primes:
        if x % prime == 0:
            return False
        if prime ** 2 > x:
            break
    return True


def main():
    base_filename = 'test' if os.name == 'nt' else 'sprime'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        primes = euler_sieve(int(math.ceil((10 ** 8 - 1) ** (1 / 2))))
        candidates = [2, 3, 5, 7]
        for _ in range(n - 1):
            new_candidates = []
            for candidate in candidates:
                for trail in range(1, 10, 2):
                    new_candidate = candidate * 10 + trail
                    if is_prime(new_candidate, primes):
                        new_candidates.append(new_candidate)
            candidates = new_candidates
        out_print(*candidates, sep='\n')


if __name__ == '__main__':
    main()
