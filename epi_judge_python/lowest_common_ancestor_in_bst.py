import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# Input nodes are nonempty and the key at s is less than or equal to that at b.
def find_LCA_common_with_general_lca(tree, s, b):
    # TODO - you fill in here.
    '''
    This implementation didn't exploit the BST property.
    '''
    def helper(tree):
        if not tree:
            return (False, False, None)
        l_found_s, l_found_b, l_lca = helper(tree.left)
        if l_found_s and l_found_b:
            return (True, True, l_lca)
        r_found_s, r_found_b, r_lca = helper(tree.right)
        if r_found_s and r_found_b:
            return (True, True, r_lca)
        if ((l_found_s and r_found_b) or
            (l_found_b and r_found_s) or
            ((l_found_b or r_found_b) and tree.data == s.data) or
            ((l_found_s or r_found_s) and tree.data == b.data) or
            (tree.data == s.data and tree.data == b.data)):
            return (True, True, tree)
        return (tree.data == s.data or l_found_s or r_found_s, tree.data == b.data or l_found_b or r_found_b, None)
    return helper(tree)[2]

def find_LCA(tree, s, b):
    if s.data <= tree.data <= b.data:
        return tree
    if tree.data < s.data:
        return find_LCA(tree.right, s, b)
    else:
        return find_LCA(tree.left, s, b)

def find_LCA_iter(tree, s, b):
    root = tree
    while not (s.data <= root.data <= b.data):
        if root.data < s.data:
            root = root.right
        else:
            root = root.left
    return root

@enable_executor_hook
def lca_wrapper(executor, tree, s, b):
    result = executor.run(
        functools.partial(find_LCA_iter, tree, must_find_node(tree, s),
                          must_find_node(tree, b)))
    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_in_bst.py",
                                       'lowest_common_ancestor_in_bst.tsv',
                                       lca_wrapper))
