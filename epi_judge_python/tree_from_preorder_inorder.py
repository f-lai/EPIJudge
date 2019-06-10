from test_framework import generic_test
from binary_tree_node import BinaryTreeNode as TN


def binary_tree_from_preorder_inorder(preorder, inorder):
    # TODO - you fill in here.
    if not preorder:
        if inorder:
            raise ValueError("Wrong inputs")
        return None

    if len(preorder) == 1:
        if len(inorder) != 1:
            raise ValueError("Wrong inputs")
        return TN(preorder[0])

    inorder_idx = {node_data:i for i, node_data in enumerate(inorder)}
    tree = root = TN(preorder[0])
    for p_node_val in preorder[1:]:
        found_insertion = False
        root = tree
        while not found_insertion:
            if inorder_idx[root.data] < inorder_idx[p_node_val]:
                if root.right:
                    root = root.right
                else:
                    root.right = TN(p_node_val)
                    found_insertion = True
            elif inorder_idx[root.data] > inorder_idx[p_node_val]:
                if root.left:
                    root = root.left
                else:
                    root.left = TN(p_node_val)
                    found_insertion = True
            else:
                raise ValueError("Impossible case")
    return tree


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
