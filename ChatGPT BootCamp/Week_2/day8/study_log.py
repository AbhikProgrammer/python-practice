from datetime import date

num = int(input("How many subjects did you study today?    "))
today = date.today()

with open("study_log.txt", "a") as file:
    file.write("--> DATE: " + str(today) + "\n")
    for i in range(num):
        subject = input("Subject:  ")
        time_studied = input("Time studied:  ")
        file.write(subject + ": " + time_studied + "\n")
