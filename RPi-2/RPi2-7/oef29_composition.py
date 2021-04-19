# composition is used to build out classes that use other classes, it is used more often then inheritance
# composition allows your classes to be simpler and reduces the complexity of your code overall

class BookShelf:

    def __init__(self, *books):
        self.books = list(books)
        print("1", type(self.books))

    def add_book(self, extra_book):
        self.books.append(extra_book)

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book1 = Book("Harry Potter")
book2 = Book("Python 3.7")

shelf_living_room = BookShelf(book1, book2)
print("2", shelf_living_room)

book3 = Book("Arduino for beginners")
shelf_living_room.add_book(book3)
print("3", shelf_living_room)

print("4 check all books on the shelf in the living room")
for book in shelf_living_room.books:
    print(book)