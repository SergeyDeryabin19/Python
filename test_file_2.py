from random import randint

# Создаем пустое поле 10х10
board = []
for i in range(10):
    board.append(["O"] * 10)

# Функция для печати текущего состояния поле
def print_board(board):
    for row in board:
        print(" ".join(row))

# Генерируем случайную позицию корабля
def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# Заполняем поле одним кораблем
ship_row = random_row(board)
print(ship_row)
ship_col = random_col(board)
print(ship_col)

# Играем до тех пор, пока корабль не будет потоплен
for turn in range(4):
    print("Ход", turn + 1)

    # Просим игрока выбрать строку и столбец
    guess_row = int(input("Выберите строку (от 1 до 10): ")) - 1
    guess_col = int(input("Выберите столбец (от 1 до 10): ")) - 1

    # Проверяем, попал ли игрок в корабль
    if guess_row == ship_row and guess_col == ship_col:
        print("Поздравляем, вы потопили корабль!")
        break
    else:
        # Если игрок промахнулся, отмечаем клетку на поле
        if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
            print("Выстрел за пределами поля.")
        elif board[guess_row][guess_col] == "X":
            print("Вы уже стреляли в эту клетку.")
        else:
            print("Промах.")
            board[guess_row][guess_col] = "X"
        # Печатаем новое состояние поля
        print_board(board)
    # Если это был последний ход, сообщаем игроку, что он проиграл
    if turn == 3:
        print("Игра окончена. Вы проиграли.")