class Book(object):
    def __init__(self, author, title):
        self.author = author
        self.title = title
    def display(self):
       self.author = input('Who is the author: ')
       self.title = input('what is the title: ')
       OUTPUT = '{0} written by {0}'.format(self.author, self.title)