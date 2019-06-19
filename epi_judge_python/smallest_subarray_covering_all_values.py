import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


'''
             0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
                       i
paragraph = “a a a a a d d d d b d d c a b”
                                       j
chars_needed = ("a")
window_needs = {'a': 1, 'b': 0, 'c':0}
best_candidate = ('-inf', 'inf'), (0, 13)
'''


from collections import namedtuple

from ipdb import launch_ipdb_on_exception

Subarray = namedtuple('Subarray', ('start', 'end'))


def find_smallest_sequentially_covering_subset(p, s):
    # TODO - you fill in here.
    if p == []:
        raise ValueError("Empty string cannot cover")
    if len(s) > len(p):
        raise ValueError("Cannot possibly cover")
    if len(s) == 1 and list(s)[0] in p:
        first_idx = p.index(list(s)[0])
        return Subarray(first_idx, first_idx + 1)

    all_chars_needed = set(s)
    chars_needed = set(s)
    window_needs = {c: 1 for c in s}
    best_candidate = Subarray(float("-inf"), float("inf"))

    i = 0
    for j in range(1, len(p) + 1):
        if p[j-1] not in all_chars_needed:
            continue
        window_needs[p[j-1]] -= 1
        if window_needs[p[j-1]] == 0:
            chars_needed.remove(p[j-1])

        while chars_needed == set():
            if p[i] not in all_chars_needed:
                i += 1
                continue
            if j-i == len(s): # short circuit since it's the smallest possible
                return Subarray(i, j)
            if j - i < best_candidate.end - best_candidate.start:
                best_candidate = Subarray(i, j)
            if window_needs[p[i]] == 0:
                chars_needed.add(p[i])
            window_needs[p[i]] += 1
            i += 1
    return best_candidate


@enable_executor_hook
def find_smallest_sequentially_covering_subset_wrapper(executor, paragraph,
                                                       keywords):
    with launch_ipdb_on_exception():
        result = executor.run(
            functools.partial(find_smallest_sequentially_covering_subset,
                            paragraph, keywords))

        # kw_idx = 0
        # para_idx = result.start
        # if para_idx < 0:
        #     raise RuntimeError('Subarray start index is negative')

        # while kw_idx < len(keywords):
        #     if para_idx >= len(paragraph):
        #         raise TestFailure("Not all keywords are in the generated subarray")
        #     if para_idx >= len(paragraph):
        #         raise TestFailure("Subarray end index exceeds array size")
        #     if paragraph[para_idx] == keywords[kw_idx]:
        #         kw_idx += 1
        #     para_idx += 1

        import ipdb; ipdb.set_trace()
        return result[1] - result[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_all_values.py",
            'smallest_subarray_covering_all_values.tsv',
            find_smallest_sequentially_covering_subset_wrapper))
