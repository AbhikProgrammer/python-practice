import sqlite3

connection = sqlite3.connect("library.db")

cursor = connection.cursor()

# Create Database table

cursor.execute("""
CREATE TABLE IF NOT EXISTS library (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    available INTEGER
)
""")

connection.commit()

# Add books

def insert(id, title, author, available):


    cursor.execute(
        """
        INSERT INTO library(id, title, author, available)
        VALUES (?, ?, ?, ?)
        """,
        (id, title, author, available)
    )

    connection.commit()

# View books

def view():
    cursor.execute(
        "SELECT * FROM library"
    )

    books = cursor.fetchall()

    for book in books:
        print(book)

# Borrow books

def borrow(id):
    cursor.execute("SELECT available FROM library WHERE id = ?",
    (id,)
    )

    available = cursor.fetchone()[0] - 1

    # Sees the number of books present

    if available == -1:
        print("\nSorry, book not available")

    else:
            cursor.execute(
                """
                UPDATE library
                SET available = ?
                WHERE id = ?
                """,
                (available, id)
            )
            print("\nBook issued!")


    connection.commit()

def return(id):

    cursor.execute("SELECT available FROM library WHERE id = ?",
    (id,)
    )

    available = cursor.fetchone()[0] + 1

    # Sees the number of books present
    cursor.execute(
        """
        UPDATE library
        SET available = ?
        WHERE id = ?
        """,
        (available, id)
    )
    print("\nBook returned!!")


    connection.commit()

def delete(id):

    cursor.execute(
        """
        DELETE FROM library
        WHERE id = ?
        """,
        (id,)
    )

    connection.commit()
