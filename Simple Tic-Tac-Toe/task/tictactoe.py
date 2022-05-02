# write your code here

def matrix(ilist):
    matr = []
    for i in range(0, len(ilist), 3):
        matr.append([ilist[i], ilist[i + 1], ilist[i + 2]])
    return matr


def print_ttt(matr):
    print('---------')
    for i in range(len(matr)):
        print(f'| {matr[i][0]} {matr[i][1]} {matr[i][2]} |')
    print('---------')


def check_4_win(matr, symbol):
    wins = False
    for i in range(len(matr)):
        if matr[i][0] == symbol and matr[i][1] == symbol and matr[i][2] == symbol:
            wins = True
        elif matr[0][i] == symbol and matr[1][i] == symbol and matr[2][i] == symbol:
            wins = True
    if matr[0][0] == symbol and matr[1][1] == symbol and matr[2][2] == symbol:
        wins = True
    elif matr[0][2] == symbol and matr[1][1] == symbol and matr[2][0] == symbol:
        wins = True
    return wins


def check_input(item):
    numbers = '0123456789'
    error = True
    while error:
        coord = [str(i) for i in item.split()]
        if coord[0] not in numbers or coord[1] not in numbers:
            print('You should enter numbers!')
            item = input('Please enter coords:')
            continue
        elif int(coord[0]) > 3 or int(coord[1]) > 3 or int(coord[0]) < 1 or int(coord[1]) < 1:
            print('Coordinates should be from 1 to 3!')
            item = input('Please enter coords:')
            continue
        elif matr_comm[int(coord[0]) - 1][int(coord[1]) - 1] != '_':
            print('This cell is occupied! Choose another one!')
            item = input('Please enter coords:')
            continue
        else:
            error = False
    return [int(coord[0]) - 1, int(coord[1]) - 1]

comm = '_________'
matr_comm = matrix(comm)
print_ttt(matr_comm)
x_o_turn = 0
char_space = sum(x.count('_') for x in matr_comm)

while char_space > 0:
    coords = check_input(input('Please enter coords:'))
    if x_o_turn % 2 == 0:
        matr_comm[coords[0]][coords[1]] = 'X'
    else:
        matr_comm[coords[0]][coords[1]] = 'O'
    x_o_turn += 1
    print(x_o_turn)
    char_space = sum(x.count('_') for x in matr_comm)
    char_x = sum(x.count('X') for x in matr_comm)
    char_o = sum(x.count('O') for x in matr_comm)
    wins_x = check_4_win(matr_comm, 'X')
    wins_o = check_4_win(matr_comm, 'O')
    print_ttt(matr_comm)
    # print(wins_x, wins_o, char_space)

    if char_space == 0 and not wins_x and not wins_o:
        print('Draw')
        break
    elif wins_x:
        print('X wins')
        break
    elif wins_o:
        print('O wins')
        break



#
# if wins_x and wins_o or char_x - char_o > 1 or char_o - char_x > 1:
#     print('Impossible')
# elif char_space > 0 and not wins_x and not wins_o:
#     print('Game not finished')









