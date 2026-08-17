from database import get_connection

connection = get_connection()
cursor = connection.cursor()

def insert(id, title, author, available):
    cursor.execute(
        """
        INSERT INTO library(id, title, author, available)
        VALUES (?, ?, ?, ?)
        """,
        (id, title, author, available)
    )

    connection.commit()


def view():
    cursor.execute(
        "SELECT * FROM library"
    )

    books = cursor.fetchall()
    for book in books:
        print(book)

def delete(id):

    cursor.execute(
        """
        DELETE FROM library
        WHERE id = ?
        """,
        (id,)
    )

    connection.commit()
