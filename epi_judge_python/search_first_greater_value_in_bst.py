from test_framework import generic_test


def find_first_greater_than_k(tree, k):
    ''' O(h) time, O(h) for stack space
    '''
    def helper(tree, k, candidate):
        if not tree:
            return candidate
        if k < tree.data:
            return helper(tree.left, k, tree)
        return helper(tree.right, k, candidate)
    return helper(tree, k, None)


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1

def find_first_inorder_traversal(tree, k):
    # TODO - you fill in here.
    def helper(tree, k, candidate):
        if not tree:
            return candidate
        if k <= tree.data:
            return helper(tree.left, k, tree)
        return helper(tree.right, k, candidate)
    return helper(tree, k, None)


if __name__ == '__main__':

    exit(
        generic_test.generic_test_main("search_first_greater_value_in_bst.py",
                                       'search_first_greater_value_in_bst.tsv',
                                       find_first_greater_than_k_wrapper))
