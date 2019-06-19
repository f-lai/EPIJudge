from test_framework import generic_test

from collections import Counter


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # TODO - you fill in here.
    magazine_counter = Counter(magazine_text)
    for letter_char, char_occur in Counter(letter_text).items():
        if char_occur > magazine_counter[letter_char]:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
