contacts = {}

while True:
    name = str(input("Give name of recipient:    "))

    if name.lower() == "quit":   #name.lower() is used in case user doesnt take care of lowercase or uppercase
        break
    contacts[name] = str(input("Give the phone number:    "))

print("\n Contacts")

for name, phone in contacts.items():
    print(name, "-", phone)
