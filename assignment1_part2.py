class Book(object):
    def __init__(self, author, title):
        self.author = author
        self.title = title
    def display(self):
        book1 = Book("Of Mice and Men", "John Steinbeck")
        book2 = Book("To Kill a Mockingbird", "Harper Lee")
        print("{} written by {}".format(book1))
        print("{} written by {}".format(book2))