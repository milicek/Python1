def login():
    while True:
        login = input("Zadej login: ")
        password = input("Zadej heslo: ")
        if login and password:
            return login, password
        else:
            print("musíš zadat jméno i heslo")


def exist_user(user_name, database):
    try:
        if not user_name in database.keys():
            print(f"Uživatel {user_name} v databázi neexistuje")
            return False
        else:
            return True
    except:
        print("Špatná databáze")


def strong_password(password):
    lower = False
    uper = False
    digit = False
    for letter in password:
        if letter.islower():
            lower = True
        if letter.isupper():
            uper = True
        if letter.isdigit():
            digit = True
    if lower and uper and digit == True:
        return True
    else:
        print("Slabé heslo , heslo musí obsahovat malé i velké písmena a číslo")
        return False


def main():
    users = {"franta" : "prcat", "michal": "mrdat"}
    name, password = login()
    if not exist_user(name, users):
        if input("Chceš se registrovat? ").lower() == "ano":
            while not strong_password(password):
                password = input("Zadej nové heslo: ")
            users[name] = password
        else:
            print(f"Škoda, Tak nashledanou {name}")
    else:
        pokusy = 2
        while users[name] != password and pokusy > 0:
            password = input("Špatné heslo, zadej heslo správně: ")
            pokusy -= 1
        if pokusy == 0:
            print("Zadal jsi 3x špatné heslo. ")

    #print(f"Gratuluji, jsi přihlášen uživateli {name}")














if __name__ == "__main__":
    main()