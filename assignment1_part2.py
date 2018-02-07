class Book(object):
    def __init__(self, author, title):
        self.author = author
        self.title = title
    def display(self):
        print(self.title, 'written by', self.author)

book1 = Book("John Steinbeck", "Of Mice and Men")
book2 = Book("Harper Lee", "To Kill a Mockingbird")

print book1.display()
print book2.display()