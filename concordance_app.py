#!/usr/bin/python
# coding: utf-8

import sys

from book import Book
from concordance import Concordance

USAGE = """Usage:

{} [title] <path to book file>

The book file must be a text file separated into pages with "<<<< Page >>>>".

For example, the book file with this content:

Page one text
<<<< Page >>>>
Page two text

would be parsed as a book with two pages.
""".format(__file__)

def main(args):
    if len(args) == 2:
        title = args[0]
        book_file = args[1]
    elif len(args) == 1:
        book_file = args[0]
        title = book_file.split('.')[0]
    else:
        print USAGE
        exit(1)
    with open(book_file) as book_text:
        book = Book(title, book_text.read().split('<<<< Page >>>>'))
        concordance = Concordance(book)

        print concordance

if __name__ == '__main__':
    main(sys.argv[1:])
