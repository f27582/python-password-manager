passwords = []

while True:

    choice_enter = int(input("enter your choice 1=add 2=search 3=delete 4=exit: "))

    if choice_enter == 1:
        person_id_add = int(input("enter your id in add: "))
        password_add = input("enter your password in add:")

        passwords.append([person_id_add, password_add])

        print(passwords)
 

    elif choice_enter == 2:
        search_person_id = int(input("enter your person id for search: "))

        for password in passwords:
            if password[0] == search_person_id:
               print(password)

    elif choice_enter == 3:
        dele_id = int(input("enter your id for delete: "))

        for password in passwords:
            if password[0] == dele_id:
                passwords.remove(password)

        print(passwords)

    else:
        print("invalid choice")
    if choice_enter==4:
        break
    
