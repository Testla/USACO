"""
ID: hsfncd31
LANG: PYTHON3
TASK: heritage
"""
import os
import typing


def main():
    base_filename = 'test' if os.name == 'nt' else 'heritage'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        in_order = list(get_line())
        pre_order = list(get_line())

        answer = []

        def work(in_order_range: typing.Tuple[int, int], pre_order_range: typing.Tuple[int, int]):
            if in_order_range[0] == in_order_range[1]:
                return
            print(in_order_range, pre_order_range)
            root = pre_order[pre_order_range[0]]
            in_middle = in_order.index(root)
            left_size = in_middle - in_order_range[0]
            work((in_order_range[0], in_middle), (pre_order_range[0] + 1, pre_order_range[0] + 1 + left_size))
            work((in_middle + 1, in_order_range[1]), (pre_order_range[0] + 1 + left_size, pre_order_range[1]))
            answer.append(root)

        work((0, len(in_order)), (0, len(pre_order)))

        out_print(''.join(answer))


if __name__ == '__main__':
    main()
