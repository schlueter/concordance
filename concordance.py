#!/usr/bin/python
# coding: utf-8

import re

NON_WORD_CHARACTER_REGEX = r'[--.,!?¿¡"/\\\(\)\[\]\{\}:;\n]'

class Concordance:
    """An object to represent a book and it's concordance, which this class will
    create from the text
    """

    def __init__(self, book):
        """Initialize pages to the pages supplied in the first argument and
        run the concordancer to create a concordance of the book.

        Arguments:

        book ::= A Book object.
        """
        self.concordance = self.__run_concordancer(book)

    def __run_concordancer(self, book):
        """Runs the concordancer on the pages of the book to create
        a concordance.

        Arguments:

        book ::= A Book object.
        """
        concordance = {}
        for number, page in enumerate(book.get_pages()):
            words = set(re.sub(NON_WORD_CHARACTER_REGEX, '', page).split(' '))
            for word in words:
                if word:
                    if not word in concordance:
                        concordance[word] = set()
                    concordance[word].add(number + 1)
        return concordance

    def __unicode__(self):
        output_list = []
        concordance = self.concordance
        words = concordance.keys()

        word_width = reduce(lambda x, y: x if x > y else y,
                            map(lambda x: len(x), words))

        word_output = r'{:<%s} {}' % word_width

        words.sort()

        for word in words:
            if word:
                page_numbers = list(concordance[word])
                page_numbers.sort()
                output_list.append(word_output.format(
                    word,
                    r','.join(map(lambda x: str(x), page_numbers))
                ))

        return '\n'.join(output_list)

    def __str__(self):
        return unicode(self).encode('utf-8')
