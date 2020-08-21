import random


class tiktaktoe:  # tiktaktoe with AI

    def __init__(self):
        self.cell = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.coordinates = [1, 2, 3]
        self.moves = []
        self.flag = True
        self.fc = 0
        self.hu_player = 'O'
        self.ai_player = 'X'

    def display(self):
        print('-' * 9)
        print(f'| {self.cell[0][2]} {self.cell[1][2]} {self.cell[2][2]} |')
        print(f'| {self.cell[0][1]} {self.cell[1][1]} {self.cell[2][1]} |')
        print(f'| {self.cell[0][0]} {self.cell[1][0]} {self.cell[2][0]} |')
        print('-' * 9)

    def mini_max(self, mark="O"):
        self.fc += 1
        avail_spots = self.moves
        my_list = []
        if check_wins(my_list):

    def check_wins(self, new_list):
        wins = [[self.cell[0][2], self.cell[1][2], self.cell[2][2]], [self.cell[0][1], self.cell[1][1], self.cell[2][1]],
                [self.cell[0][0], self.cell[1][0], self.cell[2][0]], [self.cell[0][2], self.cell[0][1], self.cell[0][0]],
                [self.cell[1][2], self.cell[1][1], self.cell[1][0]], [self.cell[2][2], self.cell[2][1], self.cell[2][0]],
                [self.cell[0][2], self.cell[1][1], self.cell[2][0]], [self.cell[2][2], self.cell[1][1], self.cell[0][0]]]
        _x_ = ['X', 'X', 'X']
        _o_ = ['O', 'O', 'O']
        for i in range(len(self.cell)):
            for j in range(len(self.cell)):
                new_list.append(self.cell[i][j])
        if _x_ in wins:
            print('X wins')
            print()
            self.flag = False
            return self.flag
        elif _o_ in wins:
            print('O wins')
            print()
            self.flag = False
            return self.flag
        elif (new_list.count('X') + new_list.count('O')) == 9:
            print('Draw')
            print()
            self.flag = False
        return self.flag
    def start(self, func1, func2):
        self.display()
        while self.flag:
            print(self.moves)
            my_list = []
            self.check_wins(my_list)
            if self.flag is True:
                func1('X')
            else:
                break
            my_new_list = []
            self.check_wins(my_new_list)
            if self.flag is True and ' ' in my_new_list:
                func2('O')

    def user(self, mark="X"):
        while True:
            input_location = input('Enter the coordinates: ')
            location = input_location.split(' ')
            location_ = ''.join(location)
            if not location_.isdigit():
                print('You should enter numbers!')
            else:
                x, y = location
                if int(x) not in self.coordinates or int(y) not in self.coordinates:
                    print('Coordinates should be from 1 to 3!')
                else:
                    x = int(x) - 1
                    y = int(y) - 1
                    if self.cell[x][y] != ' ':
                        print('This cell is occupied! Choose another one!')
                    else:
                        self.cell[x][y] = mark
                        self.display()
                        self.moves.remove(input_location)
                        break

    def easy_ai(self, mark="O"):
        ai_move = random.choice(self.moves)
        self.moves.remove(ai_move)
        print('Making move level "easy"')
        a, b = ai_move.split(' ')
        a = int(a) - 1
        b = int(b) - 1
        self.cell[a][b] = mark
        self.display()

    def medium_ai(self, mark="O"):
        mark_2 = 'X' if mark == 'O' else 'O'
        winning = [[mark, mark, ' '], [' ', mark, mark], [mark, ' ', mark]]
        losing = [[mark_2, mark_2, ' '], [' ', mark_2, mark_2], [mark_2, ' ', mark_2]]
        foo = [['1 1', '1 2', '1 3'], ['2 1', '2 2', '2 3'], ['3 1', '3 2', '3 3'],
               ['1 1', '2 2', '3 3'], ['1 3', '2 2', '3 1'], ['1 1', '2 1', '3 1'],
               ['1 2', '2 2', '3 2'], ['1 3', '2 3', '3 3']]
        ha = []
        for i in range(len(foo)):
            ha.append([])
            for j in range(len(foo[i])):
                x, y = foo[i][j].split(' ')
                x = int(x) - 1
                y = int(y) - 1
                ha[i].append(self.cell[x][y])
        my_index = 100
        new_index = 100
        for yay in ha:
            if yay in winning:
                my_index = ha.index(yay)
        for nay in ha:
            if nay in losing:
                new_index = ha.index(nay)
        if 0 <= my_index <= 7:  # place a third to get three in a row to win
            for e in foo[my_index]:
                x, y = e.split(' ')
                x = int(x) - 1
                y = int(y) - 1
                if self.cell[x][y] == ' ':
                    self.cell[x][y] = mark
                    print('Making move level "medium"')
                    self.moves.remove(e)
            self.display()
        elif my_index == 100 and 0 <= new_index <= 7:  # place a third to block the opponent
            for e in foo[new_index]:
                x, y = e.split(' ')
                x = int(x) - 1
                y = int(y) - 1
                if self.cell[x][y] == ' ':
                    self.cell[x][y] = mark
                    print('Making move level "medium"')
                    self.moves.remove(e)
            self.display()
        elif my_index == 100 and new_index == 100:  # random move
            com = random.choice(self.moves)
            self.moves.remove(com)
            print('Making move level "medium"')
            a, b = com.split(' ')
            a = int(a) - 1
            b = int(b) - 1
            self.cell[a][b] = mark
            self.display()




    def init_start(self):
        while True:
            self.cell = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
            self.moves = ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3']
            self.flag = True
            command = input('Input command: ')
            if command == 'exit':
                exit()
            else:
                command = command.split(' ')
                if len(command) != 3:
                    print('Bad parameters!')
                elif len(command) == 3 and command[0] == 'start':
                    if command[1] == 'easy' and command[2] == 'easy':
                        self.start(self.easy_ai, self.easy_ai)
                    elif command[1] == 'user' and command[2] == 'easy':
                        self.start(self.user, self.easy_ai)
                    elif command[1] == 'user' and command[2] == 'user':
                        self.start(self.user, self.user)
                    elif command[1] == 'easy' and command[2] == 'user':
                        self.start(self.easy_ai, self.user)
                    elif command[1] == 'user' and command[2] == 'medium':
                        self.start(self.user, self.medium_ai)
                    elif command[1] == 'easy' and command[2] == 'medium':
                        self.start(self.easy_ai, self.medium_ai)
                    elif command[1] == 'medium' and command[2] == 'medium':
                        self.start(self.medium_ai, self.medium_ai)
                    elif command[1] == 'medium' and command[2] == 'user':
                        self.start(self.medium_ai, self.user)
                    elif command[1] == 'medium' and command[2] == 'easy':
                        self.start(self.medium_ai, self.easy_ai)




# ===============================================================================================
play = tiktaktoe()
play.init_start()
