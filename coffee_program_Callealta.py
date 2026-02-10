#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: This should be modeled by using domain entities instead a dict spec
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
# TODO: This should be an Enum, TypeDict or similar
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

# TODO: If a messages collection is defined, then why the code is using the
# messages directly instead trough the colection?
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
# TODO: This variable doesn't seems to be used (value not updated)
cash = 0


# Defs
def prompting_well() -> str:
    """
    prompting for actions you can do
    :param prompting: words allows
    :return: Strings with correct word
    """

    prompt: str = input(f"{order_options}: ").lower()
    # TODO: The valid/allowed drinks should not be defined here.
    while prompt not in ["espresso", "latte", "cappuccino", "off", "report"]:
        prompt = input(f"choose one\n{order_options[21:]}: ").lower()

    return prompt


def off(secret_word: str) -> None:
    # NOTE: why this secret_word logic? Alos, it's checking the prompt twice.
    # Once here, and once before this function call
    """
    Actions requires to turn off program, the function turn off program
    :param secret_word: exact word: "off"
    :return: none
    """
    if secret_word == "off":
        print(turn_off)
        exit()


def report(money: int) -> None:
    """Full report:
    program give measures regard the Menu"""

    count = 0
    for key in resources:
        measure = ["ml", "ml", "g"]
        print(f"{key}: {resources[key]} {measure[count]}")
        count += 1
    print(f"Money: ${money}")


# TODO: Check this signature, number_or_not sounds like a boolean, but you are
# passing a str just to changing it into a number. If works, is misleading.
# Also the return type is strange.
def checking_integrates(number_or_not: str, amount_in_string: str) -> dict[str, str]:
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
            # TODO: Really hard to read the message
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


# TODO: how_much seems to be a collection, but why is a list? Shouldn't be a
# dict?
# def how_much_money_user_put(how_much: dict[str, int]) -> float
def how_much_money_user_put(how_much) -> float:

    calculating = 0
    calculating += float(how_much[0]["quarters"]) * 0.25
    calculating += float(how_much[1]["dimes"]) * 0.10
    calculating += float(how_much[2]["nickels"]) * 0.05
    calculating += float(how_much[3]["pennies"]) * 0.01

    return calculating


def cost_product_resources_updates(product: str, users_cash: float):
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
        prompt = prompting_well()
        if prompt == "off":
            off(prompt)  # checking out if they want to turn off
        elif prompt == "report":
            report(cash)
            # FIX: Don't do this recursive call!! use `continue`
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


def main() -> None:
    running()


if __name__ == "__main__":
    main()

# All code made by Rodrigo Callealta except data giving by teacher Angela from Udemy
# Download the PDF
# for the  program requirements here: https://drive.google.com/uc?export=download&id=1eIZt2TeFGVrk4nXkx8E_5Slw2coEcOUo
