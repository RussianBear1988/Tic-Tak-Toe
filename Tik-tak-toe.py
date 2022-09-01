board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player = 1

win = 1
draw = -1
running = 0

game = running
mark = 'X'

def DrawBoard():
    print(" %c | %c | %c " % (board[1],board[2],board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4],board[5],board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7],board[8],board[9]))
    print("   |   |   ")

def CheckPosition(x):
    if(board[x] == ' '):
        return True
    elif (board[x] == 'X'):
        print("Выбранная позиция уже занята Первым игроком! Повторите ваш выбор.")
        return False
    else:
        print("Выбранная позиция уже занята Вторым игроком! Повторите ваш выбор.")
        return False

def check_choice(choice):
    try:
        int(choice)
    except ValueError:
        print("Вы ввели букву, а не цифру. Попробуйте снова. Мы принимаем значения от 1 до 9.")
        return False
    if 1 <= int(choice) <= 9:
        return True
    elif int(choice) > 10:
        print("Вы ввели слишком большое число. Попробуйте снова. Мы принимаем значения от 1 до 9.")
        return False
    elif int(choice) < 1:
        print("Вы ввели слишком маленькое число. Попробуйте снова. Мы принимаем значения от 1 до 9.")
        return False


def CheckWin():
    global game
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):
        game = win
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):
        game = win
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):
        game = win
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        game = win
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        game = win
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):
        game=win
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):
        game = win
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):
        game=win
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        game=Draw
    else:
        game=running

print("Первый игрок [X] против Второго игрока [O]\n")
print()
print("Идёт отрисовка игрового поля, пожалуйста, подождите.")

while(game == running):
    DrawBoard()
    if(player % 2 != 0):
        print("Ходит первый игрок")
        mark = 'X'
    else:
        print("Ходит второй игрок")
        mark = 'O'
    choice = input("Введите число от 1 до 9, чтобы поставить свою фишку: ")
    if(check_choice(choice)):
        if(CheckPosition(int(choice))):
            board[int(choice)] = mark
            player+=1
            CheckWin()
DrawBoard()
if(game==draw):
    print("Ничья!")
elif(game==win):
    player-=1
    if(player%2!=0):
        print("Первый игрок победил!")
    else:
        print("Второй игрок победил!")