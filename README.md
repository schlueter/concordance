# Concordance

## Requirements
2 parts:

1. Please design a class (or data structure) to represent a Book


2. Lets write a feature of your system which automatically compiles a concordance:

    (0 - all the words in the book, 1 - in alpha order, 2 - pages on which each word appears)

        --- Lé Concordance ---

        Apple   1,2,3

        Banana  1,5

        ...

        Zebra   3

## Method to build concordance

For each page:

1. Remove all em dash, en dash, period, exclamation point, inverted exclamation point, question mark, inverted question mark, double quote, slash, backslash, parentheses, braces, brackets, colon, semicolon, and newline.

1. Split on spaces into a set.

1. For each group of characters (word) in the set, add the word to the concordance if it is not present, and then add the current page number to the set of page numbers for that word. 

## Notes on this concordance method
- Hyphenated words will be regarded as two words.

- Words that are capitalized because they begin a sentence will look like proper nouns in the concordance.

## Usage

**concordance_app.py** is an executable which can take a filename as a single argument and will then output a concordance for the book contained in that file so long as the file is formatted correctly. An example book in this format is included and the concordance_app may be run on that book with:

    ./concordance_app.py Example\ book\ -\ excerpt\ from\ Hamlet.txt

