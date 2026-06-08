expense = str(input("Give name of expense:    "))
amount = input("Give the amount you are spending:    ")

with open("expense.txt", "a") as file:              #We cannot interchange "w" and "a" as "w" removes previous text writes newly
    file.write("--> "+expense+" : "+amount+"\n")

print("Expense saved")

with open("expense.txt", "r") as file:
    print(file.read())
