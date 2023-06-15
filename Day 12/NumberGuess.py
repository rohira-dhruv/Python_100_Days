from art import logo
from random import randint
from os import system

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def compare(guess, target):
    if guess < target:
        print("Too low.")
    elif guess > target:
        print("Too high.")
    else:
        print(f"You got it!")
    return guess - target


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    attempts = 0
    if difficulty == 'easy':
        attempts = EASY_LEVEL_TURNS
    elif difficulty == 'hard':
        attempts = HARD_LEVEL_TURNS
    else:
        print("Psst, You have chosen an invalid difficulty level.")

    target = randint(1, 101)
    while attempts != 0:
        print(f"You have {attempts} attempts to guess the number.")
        guess = int(input("Make a guess: "))
        if compare(guess, target) == 0:
            break
        attempts -= 1

        if attempts == 0:
            print("You've run out of guesses! You lose.")
            print(f"The number was {target}.")


should_continue = 'yes'
while should_continue == 'yes':
    system('cls')
    game()
    should_continue = input("Do you want to play the game again? Type 'yes' or 'no': ")
print("Goodbye! Thanks for playing!")
