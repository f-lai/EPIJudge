import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree, s, b):
    # TODO - you fill in here.
    def helper(tree):
        if not tree:
            return (False, False, None)
        l_found_s, l_found_b, l_lca = helper(tree.left)
        if l_found_s and l_found_b:
            return (True, True, l_lca)
        r_found_s, r_found_b, r_lca = helper(tree.right)
        if r_found_s and r_found_b:
            return (True, True, r_lca)
        if (
            (l_found_s and r_found_b) or
            (l_found_b and r_found_s) or
            ((l_found_b or r_found_b) and tree.data == s.data) or
            ((l_found_s or r_found_s) and tree.data == b.data) or
            (tree.data == s.data and tree.data == b.data)
        ):
            return (True, True, tree)
        return (tree.data == s.data or l_found_s or r_found_s, tree.data == b.data or l_found_b or r_found_b, None)
    return helper(tree)[2]


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
