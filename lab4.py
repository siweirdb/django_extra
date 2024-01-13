users = []
is_authorized = -1


def password_validation(password: str) -> str:
    while len(password) < 8:
        print("Password should be longer")
        password = input("Password: ")
    return password


def email_validation(email: str) -> str:
    while True:
        if email_available_check(email) != -1:
            print("Such mail already exists. Please enter another email")
            email = input()
        elif "@" not in email:
            print('Email should contain "@". Enter email with this symbol (@)')
            email = input()
        else:
            break
    return email


def authorization():
    email = input("Enter email: ")
    while email_available_check(email) == -1:
        print("there is no such email! try typing again")
        email = input()
    correct_password = users[email_available_check(email)]["password"]
    password = input("Enter password: ")

    while correct_password != password:
        print("Wrong password!")
        password = input()

    print("You are successfully logged in!")
    global is_authorized
    is_authorized = email_available_check(email)


def create_user():
    name = input("Name: ")
    surname = input("Surname: ")
    age = input("Age: ")
    while not age.isnumeric():
        if not age.isnumeric():
            print("You have entered a string")
            age = input()
    age = int(age)
    address = input("Address: ")
    email = input("Email: ")
    email = email_validation(email)
    password = input("Password: ")
    password = password_validation(password)
    user = {
        "name": name,
        "surname": surname,
        "age": age,
        "address": address,
        "email": email,
        "password": password,
    }
    users.append(user)


def show_users():
    for i in range(0, len(users)):
        print(
            f'{i + 1}. Name: {users[i]["name"]}, Surname: {users[i]["surname"]}, Age: {users[i]["age"]}, '
            f'Address: {users[i]["address"]}, Email: {users[i]["email"]}'
        )


def email_available_check(email: str) -> int:
    for index, user in enumerate(users):
        if user["email"] == email:
            return index
    return -1


def delete_user():
    email = input("Enter the email address of the user you want to delete: ")

    user = email_available_check(email)

    while user == -1:
        print("Sorry, there is no such mail. Please enter another email.")
        print("OR If you want to exit, enter 0")

        email = input()

        if email == "0":
            return

        user = email_available_check(email)

    global is_authorized
    if user == is_authorized:
        is_authorized = -1
    del users[user]
    print("the user has been successfully deleted.")


def logout():
    global is_authorized
    is_authorized = -1
    print("You are logout!")


while True:
    print("Choose one option:")
    print("1. Create User")
    print("2. Show list of Users")
    print("3. Delete User from List")
    print("4. Logout" if is_authorized != -1 else "4. Authorization")
    print("5. Exit")

    option = input()

    if not option.isnumeric() or int(option) > 5:
        print("You are insert not number. Please insert number 1-5")

    match option:
        case "1":
            create_user()
        case "2":
            show_users()
        case "3":
            delete_user()
        case "4":
            if is_authorized != -1:
                logout()
            else:
                authorization()
        case "5":
            break

    print()
