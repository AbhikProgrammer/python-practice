from services import borrow_book, return_book
from models import view, delete, insert

func = input("Please enter (view/insert/delete/borrow/return):   ")

if func.lower() == "view":
    view()

if func.lower() == "insert":
    id = input("Give id:  ")
    title = input("Give title:  ")
    author = input("Give author:  ")
    available = input("Give no. of books available:  ")

    insert(id, title, author, available)
    print("\nSuccessfully inserted!")

if func.lower() == "delete":
    id = input("Give id of book u wanna delete:  ")
    delete(id)


if func.lower() == "borrow":
    id = input("Give id of book u wanna borrow:  ")
    borrow_book(id)

if func.lower() == "return":
    id = input("Give id of book u wanna return:  ")
    return_book(id)
