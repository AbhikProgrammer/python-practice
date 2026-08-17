class Book:
    def __init__(self, title, author, price):
        self.title  = title
        self.author = author
        self.prine = price

    def display(self):
        print("\nBook Details")
        print("title :  ", self.title )
        print("author:  ", self.author)
        print("price:  ", self.price)

book = Book(
    "Harry Potter",
    "JK Rowling",
    8.5
)

book.display()
