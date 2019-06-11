import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from binary_tree_node import BinaryTreeNode as BTN


def build_min_height_bst_from_sorted_array(arr):
    # TODO - you fill in here.
    def bst(i, j, arr):
        if i >= j:
            return None
        m = (i+j)//2
        return BTN(arr[m], bst(i, m, arr), bst(m+1, j, arr))
    return bst(0, len(arr), arr)

@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure("Result binary tree mismatches input array")
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "bst_from_sorted_array.py", 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))



