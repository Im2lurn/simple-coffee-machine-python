resources = {
    "tot_water": 300,
    "tot_milk": 200,
    "tot_coffee": 100,
    "tot_money": 0
}
coffee_money = {
    "espresso": 1.50,
    "latte": 2.50,
    "cappuccino": 3.00
}

coffee_resources = {
    "espresso": [50, 0, 18],
    "latte": [200, 150, 24],
    "cappuccino": [250, 100, 24]
}


def manage_resources(coffee_name):
    if resources["tot_water"] - coffee_resources[coffee_name][0] >= 0:
        if resources["tot_milk"] - coffee_resources[coffee_name][1] >= 0:
            if resources["tot_coffee"] - coffee_resources[coffee_name][2] >= 0:
                resources["tot_water"] -= coffee_resources[coffee_name][0]
                resources["tot_milk"] -= coffee_resources[coffee_name][1]
                resources["tot_coffee"] -= coffee_resources[coffee_name][2]
            else:
                print("Not enough coffee")
                return
        else:
            print("Not enough milk")
            return
    else:
        print("Not enough water")
        return


def manage_money(coffee_name1):
    print(f"Cost : {coffee_money[coffee_name1]}")
    penny = float(input("pennies?:"))
    nickel = float(input("nickels?:"))
    dime = float(input("dimes?:"))
    quarter = float(input("quarters?:"))
    tot_sum = penny / 100 + nickel / 20 + dime / 10 + quarter / 4
    tot_change = round(tot_sum - coffee_money[coffee_name1], 2)
    if tot_change >= 0:
        print(f" Your change is : {tot_change}")
        resources["tot_money"] += coffee_money[coffee_name1]
        return 0
    else:
        print("Not enough money")
        return 1


buy_coffee = "yes"
while buy_coffee == "yes":
    choice = input(f'\n'
                   f'What would you like?  espresso , latte , cappuccino , report :\n')
    if choice == "report":
        print(resources)
    else:
        not_enough = 0
        print("enter coins")
        not_enough = manage_money(choice)
        if not_enough == 0:
            manage_resources(choice)
            print(f"Resources left : {resources}")

    buy_coffee = input("Would you like to buy ? yes or no?").lower()

print("Thank you for shopping with us!!!")
