note = input("Enter a note:   ")

with open("notes.txt", "a") as file:
    file.write(note + "\n")

print("Note Saved")

with open("notes.txt", "r") as file:
    print(file.read())
