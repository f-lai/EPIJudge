from test_framework import generic_test


def is_balanced_binary_tree(tree):
    def compare_max_depths(tree, depth=0):
        if not tree:
            return (True, depth)
        is_l_balanced, left_depth = compare_max_depths(tree.left, depth + 1)
        if not is_l_balanced:
            return (False, -1)
        is_r_balanced, right_depth = compare_max_depths(tree.right, depth + 1)
        balanced = is_l_balanced and is_r_balanced and abs(left_depth-right_depth) <= 1
        return (balanced, max(left_depth, right_depth))
    return compare_max_depths(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
