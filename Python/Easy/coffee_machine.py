water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550


class ResourceError(Exception):
    pass


def remaining():
    print()
    print(f'''The coffee machine has :
{water} of water
{milk} of milk
{coffee_beans} of coffee beans
{cups} of disposable cups
${money} of money
        ''')


def select_action() -> str:
    print("Write action (buy, fill, take, remaining):")
    return input()


def coffee_name():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    response = input()
    if response == "back":
        return 0
    return int(response)


def buy():
    global water, milk, coffee_beans, cups, money
    coffee_flavour = coffee_name()
    try:
        if coffee_flavour == 1:
            check_resources(need_water=250, need_beans=16)
            water -= 250
            coffee_beans -= 16
            cups -= 1
            money += 4

        elif coffee_flavour == 2:
            check_resources(need_water=350, need_milk=75, need_beans=20)
            water -= 350
            milk -= 75
            coffee_beans -= 20
            cups -= 1
            money += 7

        elif coffee_flavour == 3:
            check_resources(need_water=200, need_milk=100, need_beans=12)
            water -= 200
            milk -= 100
            coffee_beans -= 12
            cups -= 1
            money += 6
    except ResourceError:
        pass


def check_resources(need_water=0, need_milk=0, need_beans=0):
    if water < need_water:
        print('Sorry, not enough water!\n')
        raise ResourceError
    if milk < need_milk:
        print('Sorry, not enough milk!\n')
        raise ResourceError
    if coffee_beans < need_beans:
        print('Sorry, not enough beans!\n')
        raise ResourceError
    if cups < 1:
        print('Sorry, not enough cups\n')
        raise ResourceError
    print('I have enough resources, making you a coffee!\n')


def fill():
    global water, milk, coffee_beans, cups, money
    print("Write how many ml of water do you want to add: ")
    water_to_add = int(input())
    print("\nWrite how many ml of milk do you want to add: ")
    milk_to_add = int(input())
    print("\nWrite how many grams of coffee beans do you want to add:")
    coffee_to_add = int(input())
    print("\nWrite how many disposable cups of coffee do you want to add:")
    cups_to_add = int(input())
    print()
    water += water_to_add
    milk += milk_to_add
    coffee_beans += coffee_to_add
    cups += cups_to_add


def take():
    global money
    print(f"I gave you ${money}")
    print()
    money = 0


def main():
    while True:
        action = select_action()
        print()

        if action == "remaining":
            remaining()

        elif action == "buy":
            buy()

        elif action == "fill":
            fill()

        elif action == "take":
            take()

        elif action == "exit":
            break


if __name__ == '__main__':
    main()