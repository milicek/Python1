





def get_name():
    return input("Zadej jméno: ")


def get_age():
    return int(input("Zadej věk: "))


def add_user(database, user=None):
    database.append(user)
    return len(database)

def tests():
    assert type(get_name()) == str
    assert len(get_name()) > 0
    assert type(get_age()) == int
    assert type(get_age()) == int and get_age() > 0
    users = []
    assert type (add_user(users,"michal")) == int
    assert add_user(users)- add_user(users, "Franta") == -1

def main():
    tests()
    users = ["jana", "franta"]
    print(add_user(users,"michal"))




if __name__ == "__main__":
    main()