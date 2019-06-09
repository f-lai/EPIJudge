from test_framework import generic_test


def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    # TODO - you fill in here.
    if not tree:
        return True
    if not low_range <= tree.data <= high_range:
        return False
    if tree.left:
        is_left_bst = is_binary_tree_bst(tree.left, low_range=low_range, high_range=tree.data)
    else:
        is_left_bst = True
    if tree.right:
        is_right_bst = is_binary_tree_bst(tree.right, low_range=tree.data, high_range=high_range)
    else:
        is_right_bst = True
    return is_left_bst and is_right_bst


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
