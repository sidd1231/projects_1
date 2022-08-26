while True:
    try:
        age = int(input("enter your age"))
        10/age
        raise ValueError("hehe you make bugs")
    # you need to delete expec valueerror....
    except ValueError:
        print("please enter a number")
        continue
    except ZeroDivisionError:
        print("please enter higher  number")
        break
    else:
        print("thank you")

    finally:
        print("ok i am finally done")

    print("all done")
