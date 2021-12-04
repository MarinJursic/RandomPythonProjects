import random
import os
import time
import tkinter as tk

text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "


def Register(username, password):

    name = random.randrange(0, 1000, 1)

    name = CheckName(name)

    CheckUsername(username)

    Encode(username, password, name)

    return print("Successfully registered as " + username)


def Login(username, password):

    number = FindNumber(username)

    passwordFile = DecodePassword(number)

    if passwordFile == password:

        print("Welcome " + username)

    else:

        print("Username or password is incorrect\nTry again: ")

        clear = lambda: os.system('cls')
        clear()

        main()


def CheckName(name):

    path = "C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Passwords"
    files = os.listdir(path)

    names = 0

    while names < len(files):

        if files[names] == name:

            name = name + 1

            names = 0

        else:

            names = names + 1

    return name


def FindNumber(username):

    listF = os.listdir(r"C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Usernames")
    KeyList = os.listdir("C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Keys")

    for x in range(len(listF)):

        listPath = os.path.join(r"C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Usernames", listF[x])

        UserFile = open(listPath, 'r')
        UserC = UserFile.read()
        user2 = len(UserC)
        user3 = list(UserC)
        user4 = ""

        KeyPath = os.path.join("C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Keys", KeyList[x])

        KeyFile = open(KeyPath, 'r')
        Key = KeyFile.read()

        for num in range(user2):

            Position2 = text.find(UserC[num])
            Position3 = text.find(Key[num])

            Number = Position2 - Position3

            if Number < 0:
                Number = Number + 61

            user3[num] = text[Number]
            user4 = "".join(user3)

        if user4 == username:

            return x


    print("Username or password is incorrect\nTry again:")

    main()


def CheckUsername(username):

    listF = os.listdir(r"C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Usernames")
    KeyList = os.listdir("C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Keys")

    num = 0

    for x in range(len(listF)):

        listPath = os.path.join(r"C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Usernames", listF[x])

        UserFile = open(listPath, 'r')
        UserC = UserFile.read()
        user2 = len(UserC)
        user3 = list(UserC)
        user4 = ""

        KeyPath = os.path.join("C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Keys", KeyList[x])

        KeyFile = open(KeyPath, 'r')
        Key = KeyFile.read()

        for num in range(user2):

            Position2 = text.find(UserC[num])
            Position3 = text.find(Key[num])

            Number = Position2 - Position3

            if Number < 0:
                Number = Number + 61

            user3[num] = text[Number]
            user4 = "".join(user3)

        if user4 == username:

            print("Username " + "'" + user4 + "'" + " already taken\nTry again")

            time.sleep(2)

            print("\n")

            main()

    return print("No matching username")


def Encode(username, password, name):

    path = "C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Passwords"
    files = os.listdir(path)
    userdata = r"C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Usernames"
    userdata2 = os.listdir(userdata)

    pass2 = len(password)
    string2 = list(password)
    string3 = ""
    user2 = len(username)
    user3 = list(username)
    user4 = ""
    key = " "

    for x in range(user2):

        hash = random.randrange(0, 61, 1)

        key = key + text[hash]

    FileName = str(name) + "=key"
    filepath = os.path.join('C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Keys', FileName)
    file = open(filepath, 'w')
    file.write(key)
    file.close()

    for x in range(pass2):

        position2 = text.find(password[x])

        position3 = text.find(key[x])

        Number = position2 + position3

        if Number > 61:
            Number = Number - 61

        string2[x] = text[Number]
        string3 = "".join(string2)

    PassPath = os.path.join("C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Passwords", str(name))
    PassFile = open(PassPath, 'w')
    PassFile.write(string3)
    PassFile.close()

    for x in range(user2):

        position2 = text.find(username[x])
        position3 = text.find(key[x])

        Number = position2 + position3

        if Number > 61:
            Number = Number - 61

        user3[x] = text[Number]
        user4 = "".join(user3)

    UserPath = os.path.join(r"C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Usernames", str(name))
    UserFile = open(UserPath, 'w')
    UserFile.write(user4)
    UserFile.close()

    return print("Successfully encoded")


def DecodePassword(number):

    PassList = os.listdir("C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Passwords")

    PassPath = os.path.join("C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Passwords", PassList[number])

    PassFile = open(PassPath, 'r')
    password = PassFile.read()

    pass2 = len(password)
    string2 = list(password)
    string3 = ""
    Number = 0

    KeysList = os.listdir("C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Keys")

    KeysPath = os.path.join("C:\\Users\Korisnik\Desktop\Project Files\Passwords and keys\Keys", KeysList[number])

    file = open(KeysPath, 'r')
    Key = file.read()

    for x in range(pass2):

        Position2 = text.find(password[x])
        Position3 = text.find(Key[x])

        Number = Position2 - Position3

        if Number < 0:
            Number = Number + 61

        string2[x] = text[Number]
        string3 = "".join(string2)

    return string3

def main():

    print("Enter what you would like to do:\nFor Registering type 1\nFor logging in type 2")

    choice = int(input("Enter: "))

    if choice == 1:

        username = input("Enter your username: ")

        password = input("Enter your password: ")

        Register(username, password)

    if choice == 2:

        username = input("Enter your username: ")

        password = input("Enter your password: ")

        Login(username, password)


main()