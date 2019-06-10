from test_framework import generic_test


from collections import deque, defaultdict
def is_symmetric(tree):
    # TODO - you fill in here.
    def are_symmetric(t1, t2):
        if not t1 and not t2:
            return True
        elif t1 and t2:
            return (
                t1.data == t2.data and
                are_symmetric(t1.left, t2.right) and
                are_symmetric(t1.right, t2.left)
            )
        else:
            return False
    return not tree or are_symmetric(tree.left, tree.right)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
