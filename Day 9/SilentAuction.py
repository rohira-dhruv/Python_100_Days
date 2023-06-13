from art import logo
from os import system

print(logo)
print("Welcome to the silent auction program.")
auction = {}

should_continue = "yes"
while should_continue == "yes":
    name = input("What is your name?\n")
    bid = int(input("What's your bid? $"))
    auction[name] = bid
    should_continue = input("Are there other bidders? Type 'yes' or 'no'\n")
    system('cls')

highest_bidder = ""
highest_bid = 0
for bidder in auction:
    if highest_bid < auction[bidder]:
        highest_bidder = bidder
        highest_bid = auction[bidder]

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
