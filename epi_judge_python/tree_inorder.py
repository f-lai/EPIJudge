from test_framework import generic_test


from collections import deque


def inorder_traversal_01(tree):
    # TODO - you fill in here.
    # O(h) space for stack space
    if not tree:
        return []
    stack = deque([[tree, False, False]])
    res = []
    while stack:
        top = stack[0]
        cur, done_left, done_right = top
        if cur.left and not done_left:
            stack.appendleft([cur.left, False, False])
            top[1] = True
            continue
        res.append(cur.data)
        stack.popleft()
        if cur.right and not done_right:
            stack.appendleft([cur.right, False, False])
            top[2] = True
    return res


def inorder_traversal(tree):
    if not tree:
        return []

    prev = tree.parent
    result = []

    while tree:
        if tree.parent is prev:
            if tree.left:
                prev, tree = tree, tree.left
            else:
                result.append(tree.data)
                prev, tree = tree, (tree.right or tree.parent)
        else:
            if prev is tree.left:
                result.append(tree.data)
                prev, tree = tree, tree.right or tree.parent
            else:
                prev, tree = tree, tree.parent
    return result


def preorder_traversal(tree):
    if not tree:
        return []

    prev = tree.parent
    result = []

    import pdb; pdb.set_trace()
    while tree:
        if tree.parent is prev:
            result.append(tree.data)
            if tree.left:
                prev, tree = tree, tree.left
            else:
                prev, tree = tree, tree.right or tree.parent
        else:
            if prev is tree.left:
                prev, tree = tree, tree.right or tree.parent
            else:
                prev, tree = tree, tree.parent
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       preorder_traversal))
