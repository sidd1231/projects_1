import time
import os
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


logo = """
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
"""
code = True


def ecncode(text, shift_number):
    message = text
    ans_word = ""

    for item in message:
        ans_position = 0
        if item == " ":
            ans_word += "/"
        elif (item != " ") and (item not in alphabet):
            ans_word += item
        else:
            if (shift_number+alphabet.index(item)) > 25:

                ans_position = (shift_number+alphabet.index(item))-26
                ans_word += alphabet[ans_position]
            else:

                position = alphabet.index(item)
                ans_position = position+shift_number
                ans_word += alphabet[ans_position]

    return(ans_word)


def decode(word, num):
    ans_word = ""

    for item in word:
        ans_position = 0
        if item == "/":
            ans_word += " "
        else:
            if (alphabet.index(item)-shift_number) < 0:

                ans_position = (alphabet.index(item)-shift_number)+26
                ans_word += alphabet[ans_position]

            else:
                position = alphabet.index(item)

                ans_position = position-shift_number

                ans_word += alphabet[ans_position]

    return(ans_word)


while code:
    os.system("cls")
    time.sleep(.5)

    print("\t \t ")
    print(logo)
    print("\n \n \n \t >>>>>>>>>>>>>>>>>>>>>>>>>Wleccome!!!!!<<<<<<<<<<<<<<<<")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
    if direction == "encode":
        text = input("Type your message:\n").lower()

        shift_number = int(input("Type the shift number:\n"))
        if shift_number >= 26:
            print("invalid shift number :")
            x = input("hit enter to enter again")
            continue
        print(ecncode(text, shift_number))

    if direction == "decode":
        text = input("Type your message:\n").lower()
        shift_number = int(input("Type the shift number:\n"))
        if shift_number >= 26:
            print("invalid shift number :")
            x = input("hit enter to enter again")
            continue
        print(decode(text, shift_number))

    decide = input("do You wan to exit(y) or continue(n):(y/n)").lower()
    if decide == "y":
        code = False
    os.system("cls")
    time.sleep(.5)
