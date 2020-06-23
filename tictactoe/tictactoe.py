cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


def display():
    print('-' * 9)
    print(f"""| {cells[0][2]} {cells[1][2]} {cells[2][2]} |
| {cells[0][1]} {cells[1][1]} {cells[2][1]} |
| {cells[0][0]} {cells[1][0]} {cells[2][0]} |""")
    print('-' * 9)


count = 0


def start():
    while True:
        global count
        wins = [cells[0][0] + cells[0][1] + cells[0][2], cells[1][0] + cells[1][1] + cells[1][2],
                cells[2][0] + cells[2][1] + cells[2][2], cells[0][0] + cells[1][0] + cells[2][0],
                cells[0][1] + cells[1][1] + cells[2][1], cells[0][2] + cells[1][2] + cells[2][2],
                cells[0][2] + cells[1][1] + cells[2][0], cells[2][2] + cells[1][1] + cells[0][0]]
        X = [i.count("X") for i in wins]
        O = [i.count("O") for i in wins]
        if abs(cells.count('X') - cells.count('O')) > 1 or (3 in X and 3 in O):
            print("Impossible")
            break
        elif 3 in X:
            print("X wins")
            break
        elif 3 in O:
            print("O wins")
            break
        elif cells[0].count(' ') == 0 and cells[1].count(' ') == 0 and cells[2].count(' ') == 0:
            print("Draw")
            break
        coordinates = input('Enter the coordinates: ').replace(' ', '')
        if coordinates[0].isdigit() and coordinates[1].isdigit():
            if int(coordinates[0]) > 3 or int(coordinates[1]) > 3:
                print('Coordinates should be from 1 to 3!')
            elif cells[int(coordinates[0]) - 1][int(coordinates[1]) - 1] in ('X', 'O'):
                print('This cell is occupied! Choose another one!')
            else:
                if count % 2 == 0:
                    cells[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = 'X'
                    count += 1
                    display()
                elif count % 2 != 0:
                    cells[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = 'O'
                    count += 1
                    display()
        else:
            print('You should enter numbers!')


display()
start()
