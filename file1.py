<<<<<<< HEAD
import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=',
 '+', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.',
 '?', '/', '\\', '|', '~', '`']
n_letters=int(input("enter how many letters you want insert in the password: "))
n_numbers=int(input("enter how many numbers u want to insert in the password: "))
n_symbols=int(input("enter how many symbols u want to insert in the password: "))
password_list=[]
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password_list+=char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password_list+=char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password_list+=char
random.shuffle(password_list)  
password=""
for item in password_list:
    password+=item
print("your strong and unique password is !")
print(password)
=======

>>>>>>> c707827de8dd8917b57619857caa8bb44b004e33
