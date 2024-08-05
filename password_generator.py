import random
import string

L=int(input("Enter length of the password: "))

characters = string.ascii_letters + string.digits + string.punctuation

password=""

for i in range(L):
    password += random.choice(characters)

print("Your Password is:\n",password)