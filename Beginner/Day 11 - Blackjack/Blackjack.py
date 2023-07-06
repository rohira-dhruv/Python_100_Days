# BlackJack Capstone Project.
from random import choice
from art import logo
from os import system

user_cards = []
computer_cards = []


def deal_card():
    """This function randomly draws a card from a deck of cards without removing it."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return choice(cards)


def calculate_score(card_list):
    """This function calculates the score in Blackjack for the hand of cards in card_list."""
    if sum(card_list) > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


def declare_winner(user_score, computer_score):
    """This function compares the two scores and prints who was the winner."""
    if computer_score == 21 and len(computer_cards) == 2:
        print("BLACKJACK! You lose! 😭")
    elif user_score == 21 and len(user_cards) == 2:
        print("BLACKJACK! You Win! 🎉")
    elif user_score <= 21:
        if computer_score > 21:
            print("The Computer went over. You Win 😁")
        elif computer_score < user_score:
            print("You Win 😃")
        elif computer_score == user_score:
            print("It is a Draw!")
        else:
            print("You Lose 😭")
    else:
        print("You went over. You Lose 😤")


def game():
    print(logo)

    decision = "hit"
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    user_score = user_cards[0]
    while decision == "hit" and user_score <= 21:
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        print(f"\tYour cards: {user_cards}, current score is: {user_score}")
        print(f"\tDealer's first card: {computer_cards[0]}")

        if user_score <= 21:
            decision = input("Type 'hit' to get another card, or type 'pass' to pass: ")

    computer_score = computer_cards[0]
    while computer_score <= 16:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\tYour final hand is {user_cards}, and your final score is: {user_score}")
    print(f"\tDealer's final hand is {computer_cards}, and their final score is: {computer_score}")
    print()
    declare_winner(user_score, computer_score)


while input("Do you want to play a game of blackjack? Type 'y' for yes, or type 'n' for no: ").lower() == 'y':
    system('cls')
    game()
    user_cards = []
    computer_cards = []
print("Goodbye! Thanks for playing.")
