from isOdd import isOdd

def print_field(arr):
    for i in arr:
        for j in i:
            print(j,end='  ')
        print()

def over_game (arr):
    flag = False
    for i in range (0,3):
        if (arr[i][0] == arr[i][1]) & (arr[i][0] == arr[i][2]) & (arr[i][0] != '_'):
            flag = True
            return flag
        if (arr[0][i] == arr[1][i]) & (arr[0][i] == arr[2][i]) & (arr[0][i] != '_'):
            flag=True
            return flag
    if (arr[0][0] == arr[1][1]) & (arr[0][0] == arr[2][2]) & (arr[0][0] != '_'):
        flag=True
        return flag
    if (arr[0][2] == arr[1][1]) & (arr[0][2] == arr[2][0]) & (arr[0][2] != '_'):
        flag=True
        return flag
    return flag

def step_players(xo, array):
    flag = False
    while not flag:
        step_p = input(f'Ходит: {xo}, Введите через пробел значение хода по вертикали и горизонтали от 1 до 3: ')
        step = step_p.split()
        if (array[int(step[0])-1][int(step[1])-1] == '_'):
            flag = True
            array[int(step[0])-1][int(step[1])-1] = xo
        else:
            print('Так сходить нельзя')

def x_o(input_index):
    if not isOdd(input_index):
        result='x'
    else:
        result='o'
    return result
def game(input_list):
    for i in range (0, 9):
        print_field(input_list)
        step_players(x_o(i), input_list)
        if over_game(input_list):
            print(f'Игрок со знаком {x_o(i)} победил')
            print_field(input_list)
            break
        if i == 8:
            print('Ничья')