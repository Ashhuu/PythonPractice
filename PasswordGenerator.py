import string
import random
listF = []

while 1:
    length = input("How long of a password do you want?")
    char = input("How many characters do you want in your password")
    num = input("How many numbers do you want in your password")
    if (int(char) + int(num)) > int(length):
        print("\nError: Sum of character and integers exceed total length of password. Please re-enter")
    else:
        break


while len(listF) < int(length):
    for i in range(0, int(char)):
        temp = random.choice(string.ascii_letters)
        listF.append(temp)
    for i in range(0, int(num)):
        temp = random.choice(string.digits)
        listF.append(temp)

for i in listF:
    if i is listF[0]:
        a = i
    else:
        a = a+i

print(a)




