from game_data import MENU, resources as stock


def get_report(profit):
    """displays the report of the Coffee Machine."""
    for ingredient in stock:
        unit = "ml"
        if ingredient == "coffee":
            unit = "g"
        print(f"{ingredient.capitalize()}: {stock[ingredient]} {unit}")
    print(f"Money: ${profit}")


def check_resources(drink):
    """Checks if there are enough resources to make the drink."""
    required_resources = MENU[drink]["ingredients"]
    for ingredient in required_resources:
        if required_resources[ingredient] > stock[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def process_coins():
    """Returns the total from the coins inserted into the machine."""
    print("Please insert coins.")
    total = 0
    total += int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction_successful(money_received, drink):
    """Return True when the payment is accepted, or False if money is insufficient."""
    cost = MENU[drink]["cost"]
    if cost <= money_received:
        change = round(money_received - cost, 2)
        print(f"Here is the change: ${change}")
        global money
        money += cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False


def make_coffee(drink):
    """Deduct the required ingredients from the resources."""
    order = MENU[drink]
    for item in order["ingredients"]:
        stock[item] -= order["ingredients"][item]
    print(f"Here is your {drink} ☕. Enjoy!")


should_continue = True
money = 0
while should_continue:
    action = input("What would you like to have? (espresso/latte/cappuccino): ").lower()
    if action == "off":
        break
    elif action == "report":
        get_report(money)
    elif action in MENU:
        if check_resources(action):
            payment = process_coins()
            if transaction_successful(payment, action):
                make_coffee(action)
print("Thanks for using the machine!")
