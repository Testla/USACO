"""
ID: hsfncd31
LANG: PYTHON3
TASK: pprime
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
    base_filename = 'test' if os.name == 'nt' else 'pprime'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        a, b = map(int, get_line().split())
        upper_bound = 100000000
        primes = euler_sieve(int(math.ceil(upper_bound ** (1 / 2))))
        answer = []
        # single digit number
        for x in range(a, min(b, 10)):
            if is_prime(x, primes):
                answer.append(x)
        # even-number-digits number
        for half in range(1, 10 ** 4):
            x = int(''.join((str(half), *(reversed(str(half))))))
            if a <= x <= b and is_prime(x, primes):
                answer.append(x)
        # odd-number-digits number
        for left in range(1, 10 ** 3):
            for mid in range(10):
                x = int(''.join((str(left), str(mid), *(reversed(str(left))))))
                if a <= x <= b and is_prime(x, primes):
                    answer.append(x)
        out_print(*sorted(answer), sep='\n')


if __name__ == '__main__':
    main()
