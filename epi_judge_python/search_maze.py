import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze, s, e):
    def adjacent(x, y):
        return [Coordinate(i, j)
                for i,j in [(x+1, y), (x,y+1), (x-1, y), (x,y -1)]
                if 0 <= i < len(maze) and 0 <= j < len(maze[0]) and maze[i][j] == 0
        ]
    '''
    [((0,0), [(0,0)]), ((0,0), [(0,0),(1,0),])]
    cur = (0,0)
    '''
    if not maze:
        return []
    exploring = set()
    exploring.add(s)
    queue = collections.deque([(s, [s])])
    while queue:
        cur, cur_path = queue.popleft()
        if cur == e:
            return cur_path
        neighbours = adjacent(cur.x, cur.y)
        for n in neighbours:
            if n not in exploring:
                queue.append((n, cur_path + [n]))
                exploring.add(n)
    return []

def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))
