class CoffeeMachine:

    def __init__(self, water, milk, bean, cups, money):
        self.water = water
        self.milk = milk
        self.bean = bean
        self.cups = cups
        self.money = money

    def remaining(self):  # prompting the user
        print()
        print('The coffee machine has:')
        print(str(self.water) + ' of water')
        print(str(self.milk) + ' of milk')
        print(str(self.bean) + ' of coffee beans')
        print(str(self.cups) + ' of disposable cups')
        print('$' + str(self.money) + ' of money')

    def buy_coffee(self):  # buying coffee
        print()
        type_ = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n> ').strip()
        if type_ == '1':
            if self.water < 250:
                print('Sorry, not enough water!')
            elif self.bean < 16:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough disposable cups!')
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 250
                self.bean -= 16
                self.cups -= 1
                self.money += 4
        elif type_ == '2':
            if self.water < 350:
                print('Sorry, not enough water!')
            elif self.milk < 75:
                print('Sorry, not enough milk!')
            elif self.bean < 20:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough disposable cups!')
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 350
                self.milk -= 75
                self.bean -= 20
                self.cups -= 1
                self.money += 7
        elif type_ == '3':
            if self.water < 200:
                print('Sorry, not enough water!')
            elif self.milk < 100:
                print('Sorry, not enough milk!')
            elif self.bean < 12:
                print('Sorry, not enough coffee beans!')
            elif self.cups < 1:
                print('Sorry, not enough disposable cups!')
            else:
                print('I have enough resources, making you a coffee!')
                self.water -= 200
                self.milk -= 100
                self.bean -= 12
                self.cups -= 1
                self.money += 6
        else:
            print()

    def fill_ingredient(self):
        print()
        add_water = int(input('Write how many ml of water do you want to add:\n> '))
        self.water += add_water
        add_milk = int(input('Write how many ml of milk do you want to add:\n> '))
        self.milk += add_milk
        add_bean = int(input('Write how many grams of coffee beans do you want to add:\n> '))
        self.bean += add_bean
        add_cups = int(input('Write how many disposable cups of coffee do you want to add:\n> '))
        self.cups += add_cups

    def take_money(self):
        print('I gave you $' + str(self.money))
        self.money = 0

    def start(self):
        while True:
            print()
            action = input('Write action (buy, fill, take, remaining, exit):\n> ')
            if action == 'exit':
                break
            elif action == 'buy':
                self.buy_coffee()
            elif action == 'fill':
                self.fill_ingredient()
            elif action == 'take':
                self.take_money()
            elif action == 'remaining':
                self.remaining()


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
coffee_machine.start()
