import art
import random

print("Welcome to the game of Rock, Paper and Scissors!")
user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice < 0 or user_choice > 2:
    print("You have typed an invalid number, you lose!")
else:
    computer_choice = random.randint(0, 2)
    choices = [art.rock, art.paper, art.scissors]

    print(choices[user_choice])
    print("The Computer chose: ")
    print(choices[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
        print("You lose!")
    else:
        print("You win!")
