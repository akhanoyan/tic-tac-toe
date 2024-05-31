board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def draw_board():
    print("  0 1 2")
    for i in range(3):
        row = []
        for j in range(3):
            element = board[i*3+j]
            if isinstance(element, int):  # Check if the element is still a number
                row.append('-')  # Replace numbers with dash
            else:
                row.append(element)  # 'X' or 'O' stays
        print(f"{i} {' '.join(row)}")
draw_board()

def win_check():
    winning_combo = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6))
    for pos in winning_combo:
        if board[pos[0]] == board[pos[1]] == board[pos[2]]:
            return board[pos[0]]
    return False

def step_check(index, char):
    if int(index) < 1 or int(index) > 9 or board[int(index) - 1] in ('X', 'O'):
        return False
    else:
        board[int(index) - 1] = char
        return True

step = 1
turn = 'X'
game_over = False

while step < 10 and not game_over:
    index = input(f'Ход {turn}. Введите координату клетки, в которую хотите поставить {turn}: ')
    if index.isdigit():
        index = int(index)
        if 1 <= index <= 9 and step_check(index, turn):
            draw_board()
            winner = win_check()
            if winner:
                print(f'Выиграл {winner}')
                game_over = True
            else:
                turn = 'O' if turn == 'X' else 'X'
                step += 1
        else:
            print("Координата не верна. Повторите ход")
    else:
        print("Введите корректную координату от 1 до 9.")

if not game_over and step == 10:
    print('Ничья')
