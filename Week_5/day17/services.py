from database import get_connection

connection = get_connection()
cursor = connection.cursor()

def borrow_book(id):
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

def return_book(id):

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
