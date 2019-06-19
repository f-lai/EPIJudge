from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import OrderedDict


class LruCache:
    def __init__(self, capacity):
        # TODO - you fill in here.
        self.capacity = capacity
        self.cache = OrderedDict()

    def lookup(self, isbn):
        # TODO - you fill in here.
        if isbn not in self.cache:
            return -1
        self.cache.move_to_end(isbn)
        return self.cache[isbn]

    def insert(self, isbn, price):
        # TODO - you fill in here.
        if isbn not in self.cache:
            if self.capacity == len(self.cache):
                self.cache.popitem(last=False)
            self.cache[isbn] = price
        self.cache.move_to_end(isbn)

    def erase(self, isbn):
        # TODO - you fill in here.
        return int(self.cache.pop(isbn, None) is not None)


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
