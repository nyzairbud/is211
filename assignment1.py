class ListDivideException(Exception):
    pass
def listDivide(numbers = ([]), divide = 2):
    count = 0
    for n in numbers:
        if n % divide == 0:
            count = count + 1
        else:
            raise ListDivideException
        return count

def testlistDivide(self):
    listDivide([1,2,3,4,5])