from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
print("welocome this dumb coffee machine")
order=Menu.get_items()
choice=input("wat do u want"+order)
drink=Menu.find_drink(order)
print("what do u want to order")



ingredients=MenuItem.ingredients
print("resorces available in the machine:")
CoffeeMaker.report(drink)
des=CoffeeMaker.is_resource_sufficient(drink)
if(des==True):
    CoffeeMaker.make_coffee(order)
else:
    print("not suffecient ingredients")
s=input("do u wanna know the report")
if(s=="y"):
    MoneyMachine.report()
