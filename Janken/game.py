from random import choice


def add_score(user_name, score=0):
    a_file = open("rating.txt", "r")
    list_of_lines = a_file.readlines()
    for i in range(len(list_of_lines)):
        if user_name in list_of_lines[i]:
            my_list = list_of_lines[i].split(" ")
            if my_list[1].strip('\n').isdigit():  # strip('\n') to avoid value error
                my_list[0] = user_name
                temp = my_list[1].strip('\n')
                temp = int(temp) + score
                list_of_lines[i] = f'{my_list[0]} {str(temp)} \n'
                break
    a_file = open("rating.txt", "w")
    a_file.writelines(list_of_lines)
    a_file.close()


def check_winner(user, ai, rule, name_):
    if user in rule[ai]:
        add_score(name_, 100)
        print(f'Well done. Computer chose {ai} and failed')
    elif user == ai:
        add_score(name_, 50)
        print(f'There is a draw ({user})')
    elif ai in rule[user]:
        print(f'Sorry, but computer chose {ai}')


def start():
    winner = {}
    name = input('Enter your name: ')
    print(f'Hello, {name}')
    file_b = open('rating.txt', 'r+', encoding='utf-8')
    list_lines = file_b.readlines()
    if len(list_lines) > 0:
        file_b = open('rating.txt', 'a', encoding='utf-8')
        # bug fixed
        my_name = ''
        for line in list_lines:
            if name in line:
                my_name = line
                break
        if my_name not in list_lines:
            list_lines = f'\n{name} 0'
            print(list_lines, file=file_b, flush=True)
    else:
        file_b = open('rating.txt', 'w', encoding='utf-8')  # if file is empty write new
        list_lines = f'{name} 0'
        print(list_lines, file=file_b, flush=True)

    file_b.close()
    list_of_options = input()
    if list_of_options == '':
        options = ['rock', 'paper', 'scissors']  # default options
    else:
        options = list_of_options.split(',')  # take custom options
    temp = options + options
    number = (len(options) // 2) + 1
    for i in options:
        others = [x for x in temp[temp.index(i)+1:number+temp.index(i)] if x != i]
        winner[i] = others
    print("Okay, let's start")
    while True:
        user_input = input().strip(' ')
        if user_input in options:
            computer = choice(options)
            check_winner(user_input, computer, winner, name)
        elif user_input == '!rating':
            with open('rating.txt', 'r') as filer:
                list_name = filer.readlines()
                for line in list_name:
                    if name in line:
                        new_list = line.split(" ")
                        print('Your rating:', new_list[1].strip('\n'))
        elif user_input == '!exit':
            print('Bye!')
            break
        else:
            print('Invalid input')


start()
