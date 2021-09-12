from collections import deque


class NoSpaceException(Exception):
    pass


def input_data(n_packages):
    data = deque()
    for i, _ in enumerate(range(n_packages)):
        values = [int(v) for v in input().split()]
        data.append((i, values[0], values[1]))
    return data


def run_processor(buffer_size, n_packages, packages):
    if n_packages == 0:
        return []

    all_jobs = packages
    results = [None] * n_packages
    buffer = deque()
    finish_times = deque()
    current_time = 0

    while all_jobs or buffer:
        while buffer and finish_times[-1][1] == current_time:
            job_done = buffer.pop()
            finish_data = finish_times.pop()
            results[job_done[0]] = finish_data[0]

        if all_jobs and all_jobs[0][1] == current_time:
            received_job = all_jobs.popleft()
            if buffer_size == len(buffer):
                results[received_job[0]] = -1
            else:
                started_at = current_time if not buffer else finish_times[0][1]
                complete_at = started_at + received_job[2]
                buffer.appendleft(received_job)
                finish_times.appendleft((started_at, complete_at))
        else:
            current_time += 1

    return results


if __name__ == '__main__':
    # assert run_processor(1, 0, deque()) == []
    # assert run_processor(1, 1, deque([(0, 0, 0)])) == [0]
    # assert run_processor(1, 2, deque([(0, 0, 1), (1, 1, 1)])) == [0, 1]
    # assert run_processor(1, 2, deque([(0, 0, 1), (1, 0, 1)])) == [0, -1]
    # assert run_processor(1, 2, deque([(0, 0, 0), (1, 0, 0)])) == [0, 0]
    # assert run_processor(1, 2, deque([(0, 0, 1), (1, 0, 0)])) == [0, -1]
    # assert run_processor(2, 2, deque([(0, 0, 1), (1, 0, 1)])) == [0, 1]
    # assert run_processor(1, 3, deque([(0, 0, 2), (1, 1, 4), (2, 5, 3)])) == [0, -1, 5]
    #
    # import time, random
    #
    # ps = 1000
    # test_data = deque()
    # for i, x in enumerate(range(ps)):
    #     test_data.append((i, i, random.randint(0, x)))
    #
    # start_time = time.time()
    # res = run_processor(ps, ps, test_data)
    # print(time.time() - start_time)

    buffer_size, n_packages = [int(v) for v in input().split()]
    for r in run_processor(buffer_size, n_packages, input_data(n_packages)):
        print(r)
