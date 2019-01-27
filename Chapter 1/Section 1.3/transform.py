"""
ID: hsfncd31
LANG: PYTHON3
TASK: transform
"""
import os
import collections
import typing


def same(a: typing.List[typing.List[str]], b: typing.List[typing.List[str]]) -> bool:
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] != b[i][j]:
                return False
    return True


def rotate_once(m: typing.List[typing.List[str]]) -> typing.List[typing.List[str]]:
    result = [[''] * len(m) for _ in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m)):
            result[i][j] = m[len(m) - 1 - j][i]
    return result


def rotate(m: typing.List[typing.List[str]], times: int) -> typing.List[typing.List[str]]:
    result = m
    for _ in range(times):
        result = rotate_once(result)
    return result


def reflect(m: typing.List[typing.List[str]]) -> typing.List[typing.List[str]]:
    result = [[''] * len(m) for _ in range(len(m))]
    for i in range(len(m)):
        result[i] = list(reversed(m[i]))
    return result


def main():
    base_filename = 'test' if os.name == 'nt' else 'transform'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n = int(get_line())
        origin = [list(get_line()) for _ in range(n)]
        target = [list(get_line()) for _ in range(n)]
        afters = [
            *((rotate(origin, x),) for x in range(1, 3 + 1)),
            (reflect(origin),),
            tuple(reflect(rotate(origin, x)) for x in range(1, 3 + 1)),
            (origin,),
        ]
        print(afters)
        for i, after in enumerate(afters):
            if any(same(m, target) for m in after):
                out_print(i + 1)
                exit()
        out_print(7)

if __name__ == '__main__':
    main()
