import random
import time





#perparing!!!
random_var = random.randint(1, 100)
sleep = random.randint(1,3)

#Welcoming the user
print ("Welcome! to random gusser! you'll enter a number try to to guess the number! If the number is wrong the system will says worng and If you're correct then it'll says correct")

#letting the user to guess!
guess = int(input("Enter a number: "))

#adding this "time.sleep" to trick the user that its loading! but its not!
time.sleep (sleep)

#if / if not
if guess == random_var:
    print("Correct! You Won!")

if not guess == random_var:
    print ("Wrong! You Lost!")
    print(f"Answer is: {random_var}")

#I guess nobody will win! Mabye one in one trillion?

print ("Thanks for playing!!!")
