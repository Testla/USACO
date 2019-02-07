"""
ID: hsfncd31
LANG: PYTHON3
TASK: shopping
TLE at Case#10
"""
import os
import typing
import operator
import functools
import itertools
# import array
import time
# import ctypes


class NDArray(object):
    """ Really simple multi-dimensional array. """
    def __init__(self, size: typing.Iterable[int]):
        size = list(size)
        self._data = [0] * functools.reduce(operator.mul, size)
        # both array.array and ctypes doesn't help
        # self._data = array.array('i', [0] * functools.reduce(operator.mul, size))
        # Array_type = ctypes.c_int * functools.reduce(operator.mul, size)
        # self._data = Array_type()
        self.element_size = [
            functools.reduce(operator.mul, itertools.islice(size, i + 1, None), 1) for i in range(len(size))]

    def _location(self, key: typing.Iterable[int]):
        return sum(index * size for index, size in zip(key, self.element_size))

    def __getitem__(self, key: typing.Iterable[int]) -> int:
        return self._data.__getitem__(self._location(key))

    def __setitem__(self, key: typing.Iterable[int], value: int) -> None:
        self._data.__setitem__(self._location(key), value)


def main():
    base_filename = 'test' if os.name == 'nt' else 'shopping'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        start_time = time.time()
        s = int(get_line())
        # [({code: number}, price)]
        special_offers = []
        for _ in range(s):
            numbers = [int(s) for s in get_line().split()]
            products = dict((numbers[i], numbers[i + 1]) for i in range(1, len(numbers) - 1, 2))
            special_offers.append((products, numbers[-1]))
        b = int(get_line())
        if b == 0:
            # WTF, Case#3 is '0\n0\n'...
            out_print('0')
            exit()
        products_to_buy = [[int(s) for s in get_line().split()] for _ in range(b)]
        product_codes, product_counts, product_prices = zip(*products_to_buy)

        # ndarray[k_1]...[k_b]: minimum price to get k_i of product i respectively
        ndarray = NDArray((k + 1 for k in product_counts))
        for key in itertools.product(*(range(k + 1) for k in product_counts)):
            ndarray[key] = sum(price * count for price, count in zip(product_prices, key))

        for special_offer in special_offers:
            if any(code not in product_codes for code in special_offer[0]):
                # contains unwanted product
                continue
            for key in itertools.product(*(
                    range(special_offer[0].get(code, 0), count + 1)
                    for code, count in zip(product_codes, product_counts))):
                precedent = (count - special_offer[0].get(code, 0)
                             for code, count in zip(product_codes, key))
                ndarray[key] = min(ndarray[key], ndarray[precedent] + special_offer[1])

        out_print(ndarray[product_counts])
        print(time.time() - start_time)

if __name__ == '__main__':
    main()
