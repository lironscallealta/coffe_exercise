# data program

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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# messagges

order_done_msj = "The drink is dispensed, Thanks"
order_options = "What would you like? (espresso/latte/cappuccino)"
turn_off = "shutting down For maintainers"
h_short = "how many"
string_quarters = "quarters"
string_dimes = "dimes"
string_nickels = "nickels"
string_pennies = "pennies"
list_money_amounts_strings = [
    string_quarters,
    string_dimes,
    string_nickels,
    string_pennies,
]

messages = [
    order_done_msj,
    order_options,
    turn_off,
    h_short,
    string_quarters,
    string_dimes,
    string_pennies,
    list_money_amounts_strings,
]
# Variables
cash = 0


# Defs
def prompting_well(prompting):
    """
    prompting for actions you can do
    :param prompting: words allows
    :return: Strings with correct word
    """
    while prompting not in ["espresso", "latte", "cappuccino", "off", "report"]:
        prompting = input(f"choose one\n{order_options[21:]}: ").lower()
    return prompting


def off(secret_word):
    """
    Actions requires to turn off program, the function turn off program
    :param secret_word: exact word: "off"
    :return: none
    """
    if secret_word == "off":
        print(turn_off)
        exit()


def report(money):
    """Full report:
    program give measures regard the Menu"""

    count = 0
    for key in resources:
        measure = ["ml", "ml", "g"]
        print(f"{key}: {resources[key]} {measure[count]}")
        count += 1
    print(f"Money: ${money}")


def checking_integrates(number_or_not, amount_in_string):
    """
    checking if users puts integers instead of strings
    :param number_or_not: Integer
    :param amount_in_string: text with information previous set up by who made program
    :return: dict with money
    """

    while not number_or_not.isdigit():
        number_or_not = input(
            f"Please write it well.\n{h_short} {amount_in_string}: ?: "
        )
    amounts = {amount_in_string: number_or_not}
    return amounts


def money_user_dict() -> list:  # with dict
    """
    checking how much money user put into machine
    :return: dictionary with info
    """
    print("Please insert coins.")
    counting = 0
    user_cash = []
    while True:
        money_user = input(
            f"{h_short} {list_money_amounts_strings[counting]}?: "
        )  # h = how many?
        dict_info_money = checking_integrates(
            money_user, list_money_amounts_strings[counting]
        )
        user_cash.append(dict_info_money)
        print(user_cash)
        counting += 1

        if counting == len(list_money_amounts_strings):
            return user_cash


def how_much_money_user_put(how_much) -> float:

    calculating = 0
    calculating += float(how_much[0]["quarters"]) * 0.25
    calculating += float(how_much[1]["dimes"]) * 0.10
    calculating += float(how_much[2]["nickels"]) * 0.05
    calculating += float(how_much[3]["pennies"]) * 0.01

    return calculating


def cost_product_resources_updates(product, users_cash):
    """This calculates how much change you receive
    as well resources get updated by the user's order who just asked it"""

    bring_milk = True
    if product == "espresso":
        bring_milk = False

    water = MENU[product]["ingredients"]["water"]
    coffee = MENU[product]["ingredients"]["coffee"]
    if bring_milk:
        milk = MENU[product]["ingredients"]["milk"]

    if product == "cappuccino" or product == "latte":
        change = users_cash - MENU["espresso"]["cost"]
        resources["water"] = resources["water"] - water
        resources["milk"] = resources["milk"] - milk
        resources["coffee"] = resources["coffee"] - coffee
        return change

    else:
        change = users_cash - MENU["cappuccino"]["cost"]
        resources["water"] = resources["water"] - water
        resources["coffee"] = resources["coffee"] - coffee
        return change


def enough_resources(resources_to_check: dict, prompt_product: str):
    measure = ["ml", "ml", "g"]
    counting = 0
    for items in resources_to_check:

        if resources_to_check[items] > resources[items]:

            print(
                f"not enough {items}: {resources[items]} {measure[counting]}.\nIt needs to be refilled"
            )
        counting += 1


# def to run program


def running():
    going = True
    while going:
        prompt = prompting_well(input(f"{order_options}: ").lower())
        if prompt == "off":
            off(prompt)  # checking out if they want to turn off
        elif prompt == "report":
            report(cash)
            running()

        user_amount = money_user_dict()

        print(f"You insert ${round(how_much_money_user_put(user_amount),2)}")
        money_float_user_total = how_much_money_user_put(user_amount)
        your_change = cost_product_resources_updates(prompt, money_float_user_total)
        if your_change < 0:
            print(
                f"you dont have enough money, money being refund it ${round(how_much_money_user_put(user_amount),2)}"
            )
            running()
        print(
            f"your change of {prompt} which cost ${MENU[prompt]["cost"]} is ${round(your_change,2)}"
        )
        enough_resources(MENU[prompt]["ingredients"], prompt)

        should_continue = input("Do you want to continue? [y/n]").lower()
        while should_continue not in ["y", "n"]:
            should_continue = input("Do you want to continue? [y/n]").lower()
        if should_continue == "n":
            going = False
        else:
            going = True


# trying program ;D
running()

# All code made by Rodrigo Callealta except data giving by teacher Angela from Udemy
# Download the PDF
# for the  program requirements here: https://drive.google.com/uc?export=download&id=1eIZt2TeFGVrk4nXkx8E_5Slw2coEcOUo
