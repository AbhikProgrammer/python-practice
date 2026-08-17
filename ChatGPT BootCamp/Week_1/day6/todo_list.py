tasks = []

while True:
    task = str(input("Enter task(or enter 'quit' to end):  "))
    tasks.append(task)

    if task.lower() == "quit":
        break

print("\n Your Tasks:  ")

for task in tasks:
    print("-", task)
