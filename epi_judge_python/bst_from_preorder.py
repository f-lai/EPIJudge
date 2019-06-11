from test_framework import generic_test
from binary_tree_node import BinaryTreeNode as BTN

def rebuild_bst_from_preorder(preorder_sequence):
    # TODO - you fill in here.
    def bst(i, j):
        if i == j:
            return None
        left_subtree_size = len(
            [k
             for k in range(i+1, j)
             if preorder_sequence[k] < preorder_sequence[i]]
        )
        return BTN(
            preorder_sequence[i],
            bst(i+1, i+1+left_subtree_size),
            bst(i+1+left_subtree_size, j)
        )
    return bst(0, len(preorder_sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
