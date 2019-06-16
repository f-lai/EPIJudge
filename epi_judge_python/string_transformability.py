from test_framework import generic_test


from collections import deque
import string

# Uses BFS to find the least steps of transformation.
def transform_string(D, s, t):
    # TODO - you fill in here.
    if not D:
        return -1
    queue = deque([(s,0)])
    explored = set(s)
    while queue:
        cur, distance = queue.popleft()
        if cur == t:
            return distance
        for i in range(len(cur)):
            for c in string.ascii_lowercase:
                cand = cur[:i] + c + cur[i+1:]
                if cand in D and cand not in explored:
                    queue.append((cand, distance+1))
                    explored.add(cand)
    return -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
