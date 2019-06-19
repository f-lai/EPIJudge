import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph, s):

    # TODO - you fill in here.
    if paragraph == []:
        raise ValueError("Empty string cannot cover")
    if len(s) > len(paragraph):
        raise ValueError("Cannot possibly cover")
    if len(s) == 1 and list(s)[0] in paragraph:
        first_idx = paragraph.index(list(s)[0])
        return Subarray(first_idx, first_idx)

    all_chars_needed = set(s)
    chars_needed = set(s)
    window_needs = {c: 1 for c in s}
    best_candidate = Subarray(float("-inf"), float("inf"))

    i = 0
    for j in range(1, len(paragraph) + 1):
        if paragraph[j-1] not in all_chars_needed:
            continue
        window_needs[paragraph[j-1]] -= 1
        if window_needs[paragraph[j-1]] == 0:
            chars_needed.remove(paragraph[j-1])

        while chars_needed == set():
            if paragraph[i] not in all_chars_needed:
                i += 1
                continue
            if j-i == len(s): # short circuit since it's the smallest possible
                return Subarray(i, j-1)
            if j - i < best_candidate.end - best_candidate.start:
                best_candidate = Subarray(i, j-1)
            if window_needs[paragraph[i]] == 0:
                chars_needed.add(paragraph[i])
            window_needs[paragraph[i]] += 1
            i += 1

    return best_candidate


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure("Index out of range")

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure("Not all keywords are in the range")

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "smallest_subarray_covering_set.py",
            "smallest_subarray_covering_set.tsv",
            find_smallest_subarray_covering_set_wrapper))
