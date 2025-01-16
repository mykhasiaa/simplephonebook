#Мені ліньки змінювати клавіатуру щоразу,
#тому телефонна книга англійською

#creating phonebook
contacts = {}

#допоміжний словник для неуважних користувачів (допоміг ChatGPT), я не додумалась
lowercase = {name.lower(): name for name in contacts}

while True:
    # options
    print("Phonebook".center(50, "✦"))
    print("1. Add contact".center(62))
    print("2. Find contact".center(64))
    print("3. Delete contact".center(65))

    # make a choice
    while True:
        choice = input("Choose an option: ")
        if choice == "1" or choice == "2" or choice == "3":
            print("Okay! Let's continue")
            break
        else:
            continue

    #add
    if choice == "1":
        name = input("Who do you want to add?\nType in their name: ")
        number = input("Type in their number: ")
        contacts[name] = [number]
        lowercase[name.lower()] = name
        print("Contact added!\n")

    #find
    elif choice == "2":
        find = input("Who do you want to find?\nType in their name: ").lower()
        if find in lowercase:
            originalname = lowercase[find]
            print(f"{originalname}'s phone number is {contacts[originalname][0]}\n")
        else:
            print("Contact not found.\n")

    #delete
    else:
        delete = input("Who do you want to delete from your phonebook?\nType in their name: ").lower()
        if delete in lowercase:
            originalname = lowercase[delete]
            contacts.pop(originalname)
            lowercase.pop(delete)
            print("Contact deleted!\n")
        else:
            print("Contact not found.\n")

    # return to the main menu?
    while True:
        print("Do you want to return to the main menu?")
        print("1. Yes")
        print("2. No")
        mainmenu = input("Choose an option: ")
        if mainmenu == "1":
            print("")
            break
        elif mainmenu == "2":
            print("Goodbye!")
            exit() #<- з exit() допоміг ChatGPT
        else:
            continue