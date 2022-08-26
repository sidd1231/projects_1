import random
import passwordgen
alpha = passwordgen.wordlist()
password = ""

sym = ["!", "@", "#", "$", "%", "^", "&",
       "*", "(", ")", ",", "/", ":", "+"]
num = ["1", '2', '3', '4', '5', '6', '7', '8', '9', '0']


print("\t \t >>>>>>>>>>>>welcome to the password generator<<<<<<<<<<<<<")

n_letters = int(input("enter the nummber of letter you want :"))
n_numbers = int(input("enter the number of number u want in password:"))
n_symbol = int(input("enter the number of symbols u want in password:"))

total_used = n_symbol+n_letters+n_numbers

for n in range(total_used):
    # print(n)
    x = int(random.randint(1, 3))

    if x == 1:
        password += random.choice(sym)
    elif x == 2:
        password += random.choice(alpha)
    elif x == 3:
        password += random.choice(num)
    else:
        print("Techinal error!,please try again")

print(password)
# this is different approach we can also do it easy way the suffel the password
