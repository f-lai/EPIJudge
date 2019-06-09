from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    # TODO - you fill in here.
    # O(h+k) runtime, O(max(h, k)) space
    # Description: Recurse to the bottom of the tree, when returning back up,
    # record data until k nodes are recorded
    def helper(tree):
        if not tree or len(res) >= k:
            return
        helper(tree.right)
        if len(res) < k:
            res.append(tree.data)
            helper(tree.left)
    res = []
    helper(tree)
    return res

# from collections import deque
# def find_k_largest_in_bst_iter(tree, k):
#     res = []
#     cnt = 0
#     stack = deque([tree])

#     # stack [3] -> [5,3] -> [6,5,3]
#     while cnt < k and stack:
#         cur = stack[0]
#         if cur.right:
#             stack.append(cur.right)
#             continue
#         stack.pop()
#         res.append(cur.data)
#         cnt += 1
#         if cur.left:
#             stack.append(cur.left)
#     return res
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))
