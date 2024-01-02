from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks = Menu()
coffee_computer = CoffeeMaker()
money = MoneyMachine()

play = True
while play:
    choice = input(f"What would you like? {drinks.get_items()}: ")
    if choice == "off":
        play = False
    elif choice == "report":
        coffee_computer.report()
        money.report()
    elif drinks.find_drink(choice):
        drink_ordered = drinks.find_drink(choice)
        if coffee_computer.is_resource_sufficient(drink_ordered):
            if money.make_payment(drink_ordered.cost):
                coffee_computer.make_coffee(drink_ordered)
