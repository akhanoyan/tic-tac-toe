board = [1,2,3,4,5,6,7,8,9]
def draw_board():
    print(board[0:3], board[3:6], board[6:9], sep='\n')
draw_board()
def win_check():
    win = False
    winning_combo = ((0,1,2),(3,4,5),(6,7,8),
                    (0,3,6),(1,4,7),(2,5,8),
                    (0,4,8),(2,4,6))
    for pos in winning_combo:
        if board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]]:
            win = board[pos[0]]
    return win
def step_check(index, char):
    if (int(index) < 1 or int(index) > 9 or board[int(index) - 1] in ('X', 'O')):
        return False
    else:
        board[int(index)-1] = char
        return True
step = 1
turn = 'X'
while step < 10 and win_check() == False:
    index = input('Ход ' + turn + '. Введите координату клетки, в которую хотите поставить ' + turn + ' ')
    if index.isnumeric():
        if (step_check(int(index), turn)):
            if turn == 'X':
                turn = 'O'
            else:
                turn='X'
            draw_board()
            win_check()
            step += 1
        else:
            print("Координата не верна. Повторите ход")
    else:
        print("Координата не верна. Повторите ход")

if win_check == False and step == 10:
    print('Ничья')
else:
    print('Выиграл ' + win_check())
    draw_board()