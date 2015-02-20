#!/usr/bin/python
# coding: utf-8

import re


class Concordance:
    """An object to represent a book and it's concordance, which this class will
    create from the text
    """


    NON_WORD_CHARACTER_REGEX = r'[--.,!?¿¡"/\\\(\)\[\]\{\}:;\n]'

    def __init__(self, book):
        """Initialize pages to the pages supplied in the first argument and
        run the concordancer to create a concordance of the book.

        Arguments:

        book ::= A Book object.
        """
        self.concordance = self.run_concordancer(book)

    def run_concordancer(self, book):
        """Runs the concordancer on the pages of the book to create
        a concordance.

        Arguments:

        book ::= A Book object.
        """
        concordance = {}
        for number, page in enumerate(book):
            words = set(re.sub(NON_WORD_CHARACTER_REGEX, '', page).split(' '))
            for word in words:
                if not word in concordance:
                    concordance[word] = set()
                concordance[word].add(number)
        return concordance

