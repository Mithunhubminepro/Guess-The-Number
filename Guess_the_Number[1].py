#This is the game's code
#Update 1.1.1 Main Purpose of this update: Spelling Mistkes were Correct, another time.sleep and when thanking the user for playing we added the name varible there.
import random
import time

Name = input ("Enter your name: ")





#perparing!!!
random_var = random.randint(1, 100)
sleep = random.randint(1,3)

#Welcoming the user
print ("Welcome to random guesser! You'll enter a number try to guess the number! If the number is wrong the system will say its worng and if you're correct then it'll say correct")

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

print (f"Thanks for playing{Name}!!!")

time.sleep (5)
