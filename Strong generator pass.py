# 1- import string module
# 2- store all characters in lists (upper/lower case, digits, punctuations)
# 3- Take number of characters from user
# 4- make sure the number of characters is 6 or more
# 5- shuffle al lists
# 6- calculate 30% and 20% of number of characters
# 7- create password 60% letters and 40% digits and punctuations

import string
import random

s1 = list(string.ascii_lowercase) # 30%
s2 = list(string.ascii_uppercase) # 30%
s3 = list(string.digits) # 20%
s4 = list(string.punctuation) # 20%

characters = input("How manu characters for the password?: ")

while True:
          try:
                    characters = int(characters)
                    if characters < 10 :
                              print("You at least 6 characters")
                              characters = input("Please Enter the Number again!!:  ")
                    else:
                              break
          except:
                    print("Please Enter numbers only")
                    characters = input("Please Enter the Number again!!:  ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s1)
random.shuffle(s4)

part1 = round(characters * (30/100))
part2 = round(characters * (20/100))

password = []

for i in range(part1):
          password.append(s1[i]) #aFbHcM
          password.append(s2[i]) #aFbHcM

for i in range(part2):
          password.append(s3[i])
          password.append(s4[i])

random.shuffle(password)

password = "".join(password[0:])

print(password)