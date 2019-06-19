from test_framework import generic_test

from collections import Counter

def can_form_palindrome(s):
    # TODO - you fill in here.
    return sum(1 for _, n_occurence in Counter(s).items()
               if n_occurence % 2 == 1) <= 1



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
