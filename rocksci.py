import random
choosed = True
print(" \t \t \t  welcome to rock scisor paper game")

print("\n user please choose: \n rock-0 \n scissors-1 \n paper-2")
choice = int(input("choice:"))

if choice == 0:
    print("you choose_rock")
    # Rock
    print("""
     _______
   ---'   ____)
         (_____)
         (_____)
         (____)
   ---.__(___)
   """)
elif choice == 1:
    print("you choose_scissors")
    # Scissors
    print("""
    _______
   ---'   ____)____
             ______)
          __________)
         (____)
   ---.__(___)
   """)

elif choice == 2:
    print("you choose_paper")
    # Paper
    print("""
        _______
   ---'    ____)____
              ______)
             _______)
            _______)
   ---.__________)
   """)

else:
    print("invalid choice. \t please choose again")
    choosed = False

if choosed:
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print("computer choose-rock")

        # Rock
        print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)

    elif computer_choice == 1:
        print("computer choose-scissors")
        # Scissors
        print("""
        _______
    ---'   ____)____
              ______)
              _______
           __________)
          (____)
    ---.__(___)
    """)

    elif computer_choice == 2:
        print("computer choose-paper")
        # Paper
        print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)

    else:
        print("print computer crash")

    print(computer_choice)

    if choice == computer_choice:
        print(" \t \t \t draw !")
    elif (choice == 0 and computer_choice == 1) or (choice == 1 and computer_choice == 0):
        if choice > computer_choice:
            print(" \t \t \t you lose")
        else:
            print(" \t \t \t you win")
    elif (choice == 0 and computer_choice == 2) or (choice == 2 and computer_choice == 0):
        if choice > computer_choice:
            print("\t \t \t you win ")
        else:
            print("\t \t \t you loose")

    elif (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 1):
        if choice > computer_choice:
            print(" \t \t \t you loose ")
        else:
            print("\t \t \t you win")
