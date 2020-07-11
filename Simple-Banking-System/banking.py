from random import randrange
import sqlite3


class Banking:
    def __init__(self):
        self.con = sqlite3.connect('card.s3db')
        self.cur = self.con.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS card('
                         'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,'
                         'number TEXT,'
                         'pin TEXT,'
                         'balance INTEGER DEFAULT 0);')
        self.accounts = {}
        self.rows = self.con.execute('SELECT * FROM card;')
        for row in self.rows:
            self.accounts[row[1]] = row[2]
        self.exit = False
        self.con.commit()

    def add_card(self, number, pin):
        self.con.execute('INSERT INTO card(number, pin) VALUES (?,?)', (number, pin))
        self.con.commit()

    def create_account(self):
        print()
        card_no = f'4000000{str(randrange(10000000, 99999999))}'
        last_digit = 0
        if check_sum(card_no) % 10 != 0:
            last_digit = (10 - check_sum(card_no) % 10)
        card_no = f'{card_no}{str(last_digit)}'
        card_pin = str(randrange(1000, 9999))
        print('Your card has been created')
        print(f'Your card number:\n{card_no}')
        print(f'Your card PIN:\n{card_pin}')
        self.add_card(card_no, card_pin)
        self.con.commit()
        self.accounts[card_no] = card_pin

    def authenticate(self):
        print()
        number = input('Enter your card number:\n')
        pin = input('Enter your PIN:\n')
        if check_sum(number) % 10 == 0 and number in self.accounts.keys() and self.accounts[number] == pin:
            print()
            print('You have successfully logged in!')
            print()
            while True:
                print('''1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit''')
                act = input().strip()
                if act == '1':
                    self.cur.execute(f"SELECT balance FROM card WHERE number={number}")
                    row = self.cur.fetchone()
                    my_pin = row[0]
                    print(f"Balance: {str(my_pin)}")
                    print()
                elif act == '2':
                    print()
                    deposit = int(input('Enter income: \n'))
                    self.cur.execute(f"UPDATE card SET balance = balance +{deposit} WHERE number='{number}'")
                    self.con.commit()
                    print('Income was added!')
                    print()
                elif act == '3':
                    print()
                    print('Transfer')
                    card_no = input('Enter card number: \n')
                    if check_sum(card_no) % 10 != 0:
                        print('Probably you made mistake in the card number. Please try again!')
                        print()
                    elif card_no not in self.accounts.keys():
                        print('Such a card does not exist.')
                        print()
                    elif card_no == number:
                        print("You can't transfer money to the same account!")
                        print()
                    else:
                        money = int(input('Enter how much money you want to transfer: \n'))
                        self.cur.execute(f"SELECT balance FROM card WHERE number='{number}'")
                        new_row = self.cur.fetchone()
                        my_balance = new_row[0]
                        if my_balance >= money:
                            self.cur.execute(f"UPDATE card SET balance = balance -{money} WHERE number='{number}'")
                            self.cur.execute(f"UPDATE card SET balance = balance +{money} WHERE number='{card_no}'")
                            self.con.commit()
                            print('Success!')
                            print()
                        else:
                            print('Not enough money!')
                            print()
                elif act == '4':
                    self.cur.execute(f"DELETE FROM card WHERE number='{number}';")
                    self.con.commit()
                    print()
                    self.accounts = {}
                    self.rows = self.con.execute('SELECT * FROM card;')
                    for row in self.rows:
                        self.accounts[row[1]] = row[2]
                    self.exit = False
                    self.con.commit()
                    print('The account has been closed!')
                    break
                elif act == '5':
                    print('You have successfully logged out!')
                    break
                else:
                    self.exit = True
                    break
        else:
            print()
            print('Wrong card number or PIN!')

    def start(self):
        while True:
            if self.exit:
                self.con.close()
                print()
                print('Bye!')
                break
            print()
            print("""1. Create an account
2. Log into account
0. Exit""")
            action = input().strip()
            if action == '0':
                self.exit = True
                continue
            if action == '1':
                self.create_account()
            elif action == '2':
                self.authenticate()


def check_sum(card):
    new_no = []
    for i in range(len(card)):
        if i % 2 == 0:
            x = int(card[i]) * 2
            if x > 9:
                x -= 9
            new_no.append(x)
        else:
            new_no.append(int(card[i]))
    return sum(new_no)


banking = Banking()
banking.start()
