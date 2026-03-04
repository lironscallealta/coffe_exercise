#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

NAME_COMPANY = "Callealta Coffee Store"

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


MALE_NAMES_ENDSWITH_A = [
    "Luca",
    "Andrea",  # male in Italy
    "Mattia",
    "Nicola",  # male in Italy
    "Elia",
    "Enea",
    "Ezra",
    "Joshua",
    "Noa",  # male
    "Sasha",  # male in russia
    "Mika",
    "Ilya",
    "Mustafa",
    "Akira",
    "Kuba",
    "Senna",
]


def checking_machine_resources(
    selected_coffee_ingredients: dict, type_of_coffee: str
) -> bool:

    run_of_resources = False
    for ingredients in selected_coffee_ingredients:

        machine_ingredient = resources[ingredients]

        if machine_ingredient - selected_coffee_ingredients[ingredients] < 0:
            run_of_resources = True
            print(
                f"\n{ingredients.capitalize()} is less than requires for {type_of_coffee} -- {ingredients.capitalize()} is {machine_ingredient} and It needs {selected_coffee_ingredients[ingredients]}\n"
            )
        else:
            resources[ingredients] = (
                machine_ingredient - selected_coffee_ingredients[ingredients]
            )

    return run_of_resources


def delivering_coffee(resources_to_make_coffee: bool, type_of_coffee: str) -> bool:

    if not resources_to_make_coffee:
        resources_to_make_coffee = True
        genre = {"man": "Mr", "woman": "Ms"}
        if resources_to_make_coffee:
            costumer = input("Please write your name: ").capitalize()
            if not costumer.isalpha():
                print("Name can not contain weird characters")
            while not costumer.isalpha():
                costumer = input("Please write a proper name: ").capitalize()

            last_letter = costumer[-1]

            if last_letter == "a" and costumer not in MALE_NAMES_ENDSWITH_A:
                client_genre = genre["woman"]
            elif costumer in MALE_NAMES_ENDSWITH_A:
                not_sure = input(
                    "Are you Mr or Ms?\nYour name in some countries may be for both genres:\n"
                ).lower()
                while not_sure not in ["mr", "ms"]:
                    not_sure = input(
                        "Write only Mr or Ms.\nYour name in some countries may be for both genres:\n"
                    ).lower()
                    if not_sure == "mr":
                        client_genre = genre["man"]
                    else:
                        client_genre = genre["woman"]
                if not_sure.endswith("a"):
                    client_genre = genre["woman"]
                else:
                    client_genre = genre["man"]

            else:
                client_genre = genre["man"]

            print(
                f"{client_genre.capitalize()}. {costumer.capitalize()} your {type_of_coffee.capitalize()} is on the way."
            )
            for i in range(3):
                time.sleep(0.5)
                print(f".", end=" ")
            print(
                f"\nEnjoy your {type_of_coffee.capitalize()} come back any time at {NAME_COMPANY}"
            )
            return True
    return False


def is_number(number) -> int:
    while not number.isdigit():
        number = input("It must be a number")
        if number.isdigit():
            number = int(number)
            return number
    return int(number)


def filling_machine(enough: bool, type_of_coffee: str) -> None:

    if not enough:
        current_recipe = MENU[type_of_coffee]["ingredients"]
        for i in current_recipe:
            amount_current_recipe = current_recipe[i]
            amount_machine = resources[i]

            if amount_machine < amount_current_recipe:
                user_amount = input(f"how much {i} would you fill in?: ")
                user_amount = is_number(user_amount)
                resources[i] = user_amount + amount_machine

                if user_amount < amount_current_recipe:
                    user_amount = input(
                        f"{i.capitalize()} must be higher than {amount_current_recipe} to make the coffee: 1"
                    )
                    user_amount = is_number(user_amount)

                    while user_amount < amount_current_recipe:
                        user_amount = input(
                            f"{i.capitalize()} must be higher than {amount_current_recipe} to make the coffee: 2"
                        )
                        user_amount = is_number(user_amount)
                        resources[i] = user_amount + amount_machine
                        continue

                    amount_machine = user_amount + amount_machine

                else:
                    amount_machine = user_amount + amount_machine

                if amount_machine + user_amount > 300:
                    user_amount = input(
                        f"{i.capitalize()} you must fill resources with at less {(amount_machine + user_amount) - 300} to make the coffee"
                    )
                    user_amount = is_number(user_amount)
                    while amount_machine + user_amount < 300:
                        user_amount = input(
                            f"{i.capitalize()} you must fill resources with at lesss {(amount_machine + user_amount) - 300} to make the coffee-bucle"
                        )
                        user_amount = is_number(user_amount)
                        resources[i] = user_amount + amount_machine

                else:
                    resources[i] = user_amount + amount_machine

                    print("machine okay")
                    break


while True:

    choose = input("What would you like? (espresso/latte/cappuccino): ").lower()
    while choose not in ["espresso", "latte", "cappuccino", "off", "report"]:
        choose = input("write only: espresso/latte/cappuccino): ").lower()
    if choose == "off":
        break
    elif choose == "report":
        for ingredients_ in resources:
            text = f"{ingredients_}: {resources[ingredients_]}"
            if ingredients_ in ["water", "milk"]:
                text = f"{text}ml"
                print(text)
            else:
                text = f"{text}g"
                print(text)
    else:
        dict_user = MENU[choose]["ingredients"]
        enough_resources = checking_machine_resources(dict_user, choose)
        delivering = delivering_coffee(enough_resources, choose)
        filling_machine(delivering, choose)
#bien

