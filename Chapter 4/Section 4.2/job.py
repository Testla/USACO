"""
ID: hsfncd31
LANG: PYTHON3
TASK: job
Spent two or three days thinking about this problem,
tried some unproved algorithm on the b part and gave up.
Used the algorithm described by
https://yufeizhaome.wordpress.com/2014/08/01/usaco-job-processing-solution/
"""
import os
import typing
import heapq


def main():
    base_filename = 'test' if os.name == 'nt' else 'job'
    with open('{}.in'.format(base_filename), 'r') as infile,\
            open('{}.out'.format(base_filename), 'w') as outfile:  # type: typing.IO[str]
        def get_line() -> str:
            return infile.readline().rstrip('\n')

        def out_print(*args, **kwargs) -> None:
            kwargs['file'] = outfile
            print(*args, **kwargs)

        n, m1, m2 = map(int, get_line().split())
        numbers = [int(s) for s in infile.read().split()]
        a_machines = numbers[:m1]
        b_machines = numbers[m1:]
        b_machines.sort()

        # Just greedy.
        # [(finish_time, machine_id)]
        a_queue = [(a_machines[i], i) for i in range(len(a_machines))]
        heapq.heapify(a_queue)
        a_ready_times = []
        for _ in range(n):
            finish_time, machine_id = heapq.heappop(a_queue)
            a_ready_times.append(finish_time)
            heapq.heappush(a_queue, (finish_time + a_machines[machine_id], machine_id))

        # [(finish_time, machine_id)]
        b_queue = [(b_machines[i], i) for i in range(len(b_machines))]
        heapq.heapify(b_queue)
        b_ready_times = []
        for _ in range(n):
            finish_time, machine_id = heapq.heappop(b_queue)
            b_ready_times.append(finish_time)
            heapq.heappush(b_queue, (finish_time + b_machines[machine_id], machine_id))
        b_latest_finish = max(a + b for a, b in zip(a_ready_times, reversed(b_ready_times)))

        out_print(a_ready_times[-1], b_latest_finish)

if __name__ == '__main__':
    main()
