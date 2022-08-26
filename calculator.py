import os
import time

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(num1, num2):
    return num1+num2


def subtract(num1, num2):
    return num1-num2


def divide(num1, num2):
    return num1/num2


def multiply(num1, num2):
    return num1*num2


operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply

}


def calculator():

    print(logo)
    calcute = True

    num1 = float(input(" \n \t enter frst number:"))

    for keys in operations:
        print(keys)

    operation = input("please choose any of the  operation: \n")

    num2 = float(input("enter next number:"))
    answer_1 = operations[operation](num1, num2)

    print(f"{num1} {operation} {num2}={answer_1}")
    decide = input(
        f"do u want to continue with {answer_1} or restart (press n for new)").lower()

    if decide == "n":

        calcute: False
        os.system("cls")
        time.sleep(0.5)
        calculator()

    while calcute:
        for keys in operations:
            print(keys)

        operation = input("please choose any of the  operation: \n")
        num3 = float(input("enter next number:"))
        answer_2 = operations[operation](answer_1, num3)

        print(f"{answer_1} {operation} {num3}={answer_2}")

        decide = input(
            f"do u want to continue with {answer_1} or restart (press n for new)(press-y for continue)").lower()

        if decide == "y":
            answer_1 = answer_2
        else:
            calcute: False
            os.system("cls")
            time.sleep(0.5)

            calculator()


calculator()
