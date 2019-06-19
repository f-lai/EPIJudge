from test_framework import generic_test


from collections import defaultdict


def find_nearest_repetition(paragraph):
    # TODO - you fill in here.
    word_to_latest_idx, nearest_distance = {}, float('inf')
    for i, word in enumerate(paragraph):
        if word in word_to_latest_idx:
            nearest_distance = min(i - word_to_latest_idx[word], nearest_distance)
        word_to_latest_idx[word] = i
    return nearest_distance if nearest_distance != float('inf') else -1

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
