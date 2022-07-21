from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
coin_machine = MoneyMachine()

customer = True
while customer:
    drink_order = input(f"What would you like? ({menu.get_items()}): ")

    if drink_order == "off":
        customer = False
    elif drink_order == "report":
        coffee_machine.report()
        coin_machine.report()
    elif coffee_machine.is_resource_sufficient(menu.find_drink(drink_order)):
        cost = menu.find_drink(drink_order).cost
        coin_machine.make_payment(cost)
        coffee_machine.make_coffee(menu.find_drink(drink_order))
