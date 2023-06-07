# This is a Tip Calculator.
print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
num_people = int(input("How many people to split the bill? "))
total_amount = bill * (1 + (tip_percentage/100))
final_amount = round(total_amount/num_people, 2)
final_amount = "{:.2f}".format(total_amount/num_people)
print(f"Each person should pay: ${final_amount}")
