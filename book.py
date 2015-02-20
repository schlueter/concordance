class Book:
    """An object to represent a book and it's concordance, which this class will
    create from the text
    """

    def __init__(self, title, pages):
        """Initialize a bok with given pages and title.

        Arguments:
        title ::= A string containing the title of the book.

        pages ::= An array of strings where each string contains the text of a
                  page of the book in order.
        """
        self.pages = pages
        self.title = title
