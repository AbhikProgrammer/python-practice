import sqlite3

connection = sqlite3.connect("students.db")

cursor = connection.cursor()

# Create Database table

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    branch TEXT,
    cgpa REAL
)
""")

connection.commit()

# Insert data

def insert(name, branch, cgpa):


    cursor.execute(
        """
        INSERT INTO students(name, branch, cgpa)
        VALUES (?, ?, ?)
        """,
        (name, branch, cgpa)
    )

    connection.commit()

# View data

def view():
    cursor.execute(
        "SELECT * FROM students"
    )

    students = cursor.fetchall()

    for student in students:
        print(student)

# Update database

def update_cgpa(name, cgpa):


    cursor.execute(
        """
        UPDATE students
        SET cgpa = ?
        WHERE name = ?
        """,
        (cgpa, name)
    )

    connection.commit()

# Delete entries

def delete(name):

    cursor.execute(
        """
        DELETE FROM students
        WHERE name = ?
        """,
        (name,)
    )

    connection.commit()

print("Welcome to the student database")
str = input("\nEnter either of the following (insert/view/update/delete):   ")

if str.lower() == "insert":
    name = input("\nGive name of student:  ")
    branch = input("Give branch of student:  ")
    cgpa = input("Give CGPA of student:  ")
    insert(name, branch, cgpa)

if str.lower() == "view":
    view()

if str.lower() == "update":
    name = input("\nGive name of student (Case sensitive):   ")
    cgpa = input("Enter CGPA")
    update_cgpa(name, cgpa)

if str.lower() == "delete":
    name = input("\nGive name of student:  ")
    delete(name)


connection.close()
