# My first python project
# Creat a random password
# password contains at least 6 charachters
# 30% of the password is upper case letters
# 30% of the password is lower case letters
# 20% of the password is numbers
# 20% of the password is punctuations


#Wrote by Mohammed Al-Bunde
#Date: 30-07-2022

import string
import random  # import random library to shuffle the password charachters
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

charchter_number = input("How many charachters for the password?")
#print(charchter_number)

while True:
    
    try:
        charchter_number =  int(charchter_number)
        if charchter_number < 6    :
            print("you have to enter at least 6 charachters")
            charchter_number = input("please enter the number again")
        else:
            break
    except:
        print("please enter numbers only")
        charchter_number = input("how many charachters for the password? ")
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
# print(s1)
# print(s2)
# print(s3)
# print(s4)

part1 = round(charchter_number* (30/100))
part2 = round(charchter_number* (20/100))

password = []

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])
for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])
    
random.shuffle(password)
password = "".join(password[0:])
    


print (password)
