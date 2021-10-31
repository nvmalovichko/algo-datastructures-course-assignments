from collections import deque, defaultdict
from functools import lru_cache

THREAD_INDEX = defaultdict(list)


@lru_cache(maxsize=128)
def get_parent_index(i):
    return (i - 1) // 2


@lru_cache(maxsize=128)
def get_left_child_index(i):
    return i * 2 + 1


@lru_cache(maxsize=128)
def get_right_child_index(i):
    return i * 2 + 2


@lru_cache(maxsize=128)
def last_not_leave_index(n):
    return (n // 2) - 1


def _min_heapify(n, ar, i):
    left_index = get_left_child_index(i)
    right_index = get_right_child_index(i)
    nodes = list()

    current = (ar[i], i)
    nodes.append(current)

    child_left = (ar[left_index], left_index)
    nodes.append(child_left)

    if right_index <= n - 1:
        child_right = (ar[right_index], right_index)
        nodes.append(child_right)

    min_item = min(nodes, key=lambda x: x[0])
    if min_item != current:
        ar[i], ar[min_item[1]] = ar[min_item[1]], ar[i]
        return min_item[1]


def _sift_down(n, ar, i):
    if n <= 1:
        return

    affected_index = _min_heapify(n, ar, i)

    last_node_index = last_not_leave_index(n)
    if affected_index is not None:
        if affected_index <= last_node_index:
            _sift_down(n, ar, affected_index)


def _sift_up(n, ar, i):
    if n <= 1:
        return

    _min_heapify(n, ar, i)

    parent_index = get_parent_index(i)
    if parent_index >= 0:
        _sift_up(n, ar, parent_index)


def extract_min(ar):
    if len(ar) == 1:
        return ar.pop()

    min_val = ar[0]
    ar[0] = ar.pop()
    _sift_down(len(ar), ar, 0)
    return min_val


def add_node(ar, value):
    ar.append(value)
    n = len(ar)
    _sift_up(n, ar, get_parent_index(n - 1))


def process_job(jobs, threads, processing_pool, iteration):
    while jobs and threads:
        job = jobs.popleft()
        free_thread = threads.popleft()
        finish_at = job + iteration
        if not finish_at in THREAD_INDEX:
            add_node(processing_pool, finish_at)
        THREAD_INDEX[finish_at].append(free_thread)
        print(f'{free_thread} {iteration}')


def run(threads, jobs):
    processing_pool = []

    process_job(jobs, threads, processing_pool, 0)
    while jobs:
        finished_at = extract_min(processing_pool)
        free_threads = deque(sorted(THREAD_INDEX[finished_at]))
        process_job(jobs, free_threads, processing_pool, finished_at)
        del THREAD_INDEX[finished_at]


if __name__ == '__main__':
    n_threads, n_jobs = [int(x) for x in input().split()]
    threads = deque(range(n_threads))
    jobs = deque([int(x) for x in input().split()])

    # n_threads = 2
    # threads = deque([0, 1])
    # jobs = deque([1, 2, 3, 4, 5])

    # n_threads = 4
    # threads = deque([0, 1, 2, 3])
    # jobs = deque([1] * 20)

    # n_threads = 10
    # threads = deque(sorted(range(n_threads)))
    # jobs = deque([x for x in range(n_threads * 10000)])

    # time_start = time.time()
    run(threads, jobs)
    # print(time.time() - time_start)
