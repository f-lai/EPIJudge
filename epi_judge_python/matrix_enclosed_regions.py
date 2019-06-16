from test_framework import generic_test
from itertools import product
from collections import deque


def fill_surrounded_regions(board):
    if not board or not board[0]:
        return

    def reachable(x, y):
        queue = deque([(x, y)])
        seen = {(x, y)}
        while queue:
            x, y = queue.popleft()
            for d in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nxt_x, nxt_y = x+d[0], y+d[1]
                nxt = (nxt_x, nxt_y)
                if nxt not in seen and 0 <= nxt_x < m and 0 <= nxt_y < n and\
                   board[nxt_x][nxt_y] == 'W':
                    queue.append(nxt)
                    seen.add(nxt)
        return list(seen)

    m, n = len(board), len(board[0])
    reachable_from_boundry = set()

    for x, y in product(range(m), range(n)):
        if (x, y) not in reachable_from_boundry and\
           (x == 0 or x == m-1 or y == 0 or y == n-1) and\
           board[x][y] == 'W':
            reachable_xy = reachable(x, y)
            reachable_from_boundry = {*reachable_from_boundry, *reachable_xy}


    for x, y in product(range(m), range(n)):
        if (x, y) not in reachable_from_boundry:
            board[x][y] = 'B'


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
