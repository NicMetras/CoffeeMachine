MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 300,
    "coffee": 100,
}

coins = ["quarters", "dimes", "nickels", "pennies"]

def check_resources(drink):
    for ingredient in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def process_payment(payment, drink):
    drink_cost = MENU[drink]["cost"]
    values = [0.25, 0.1, 0.05, 0.01]
    total_paid = 0

    print("Processing your payment...")

    for index, value in enumerate(payment):
        total_paid += (payment[index] * values[index])

    print(f"Amount received: ${total_paid}")

    if total_paid >= drink_cost:
        change = total_paid - drink_cost
        print(f"Dispensing your change: ${change}")
        return True
    else:
        print("Received insufficient funds..Money refunded")
        print(f"${abs(total_paid - drink_cost)} more required for Beverage: {drink}")
        return False





money = 0
machine_on = True
while machine_on:
    user_choice = input("What would you like? [espresso/latte/cappuccino] ")
    if user_choice == "report":
        for r in resources:
            print(f"{r.title()}: {resources[r]}")
        print(f"Money in machine: ${money}")

    elif user_choice == "off":
        machine_on = False

    else:
        if not check_resources(user_choice):
            machine_on = False
        else:
            user_paid = []
            for coin in coins:
                user_paid.append(int(input(f"How many {coin}: ")))

            if process_payment(user_paid, user_choice):
                money += MENU[user_choice]["cost"]
                for r in resources:
                    resources[r] -= MENU[user_choice]["ingredients"][r]
                print(f"Here is your {user_choice}. Enjoy!")
            else:
                continue
