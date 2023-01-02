from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from os import system

my_money = MoneyMachine()
coffee = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    option = menu.get_items()
    choice = input(f"what drink would you like?{option}:  ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_money.report()
        coffee.report()
    elif choice =="latte" or choice == "cappuccino" or choice == "espresso":
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if my_money.make_payment(drink.cost):
                coffee.make_coffee(drink)
    elif choice == "clear":
        system("cls")
    else:
        menu.find_drink(choice)