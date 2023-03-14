from art import logo, line
from random import randint, choice
import os
from colorama import Fore, Style

game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
winner = ''
symbol = ''
first_player = 0


def print_positions():
    print(f"{Fore.BLUE}[", end='')

    for i in range(len(positions)):
        print(f"{positions[i]+1}", end='')
        if i != len(positions) - 1:
            print(", ", end='')

    print("]", end='')
    print(Style.RESET_ALL)


def print_game_board():
    for i in range(3):
        for j in range(3):
            print(f" {game_board[(i * 3) + j]} ", end='')
            if j == 2 and i < 2:
                print(line)
            elif i != 2 or j != 2:
                print('|', end='')
            else:
                print("\n")


def check_board():
    global winner
    for i in range(3):
        j = i * 3
        if game_board[j] != ' ' and game_board[j] == game_board[j + 1] and game_board[j] == game_board[j + 2]:
            winner = game_board[j]
            return True
        elif game_board[i] != ' ' and game_board[i] == game_board[i + 3] and game_board[i] == game_board[i + 6]:
            winner = game_board[i]
            return True

    if game_board[0] != ' ' and game_board[0] == game_board[4] and game_board[0] == game_board[8]:
        winner = game_board[0]
        return True
    if game_board[2] != ' ' and game_board[2] == game_board[4] and game_board[2] == game_board[6]:
        winner = game_board[2]
        return True

    return False


def player_input(i):
    taken = True

    while taken:
        print("Available positions: ", end='')
        print_positions()
        input_symbol = int(input(f"Player {i + 1}: Insert position for {symbol} symbol: ")) - 1
        if input_symbol not in positions:
            print("That position is already taken.")
            taken = True
        else:
            taken = False

    return input_symbol


def find_two_equals(sign):
    # vertical
    for i in range(3):
        if game_board[i] == sign:
            if game_board[i] == game_board[i + 3] and game_board[i + 6] == ' ':
                return i + 6
            elif game_board[i] == game_board[i + 6] and game_board[i + 3] == ' ':
                return i + 3
        elif game_board[i + 3] == sign and game_board[i + 6] == sign and game_board[i] == ' ':
            return i

    # horizontal
    for i in range(0, 7, 3):
        if game_board[i] == sign:
            if game_board[i] == game_board[i + 1] and game_board[i + 2] == ' ':
                return i + 2
            elif game_board[i] == game_board[i + 2] and game_board[i + 1] == ' ':
                return i + 1
        elif game_board[i + 1] == sign and game_board[i + 2] == sign and game_board[i] == ' ':
            return i

    # first diagonal
    if game_board[0] == sign:
        if game_board[0] == game_board[4] and game_board[8] == ' ':
            return 8
        elif game_board[0] == game_board[8] and game_board[4] == ' ':
            return 4
    elif game_board[4] == sign and game_board[8] == sign and game_board[0] == ' ':
        return 0

    # second diagonal
    if game_board[2] == sign:
        if game_board[2] == game_board[4] and game_board[6] == ' ':
            return 6
        elif game_board[2] == game_board[6] and game_board[4] == ' ':
            return 4
    elif game_board[4] == sign and game_board[6] == sign and game_board[2] == ' ':
        return 2

    return -1


def ai_input():
    # check if AI has two equals
    sign = 'X' if first_player == 1 else 'O'
    next_sign = find_two_equals(sign)
    if next_sign != -1:
        return next_sign

    # check if player has two equals
    sign = 'X' if first_player == 0 else 'O'
    next_sign = find_two_equals(sign)

    if next_sign != -1:
        return next_sign

    # if there both checks above are false, then choose a random position
    return choice(positions)


# os.system('cls' if os.name == 'nt' else 'clear')
print(logo)
print_game_board()

mode = int(input("Press 1 to play against the AI, 2 for two players: "))
if mode == 1:
    first_player = randint(0,1)

while not winner:
    for i in range(2):
        if len(positions) == 0:
            print("The match is even")
            exit()

        symbol = 'X' if i == 0 else 'O'

        if mode == 2:
            input_symbol = player_input(i)
        else:
            if (first_player + i) == 1:
                input_symbol = ai_input()
            else:
                input_symbol = player_input(0)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        game_board[input_symbol] = symbol
        positions.remove(input_symbol)
        print_game_board()

        if check_board():
            if mode == 1:
                if first_player == 0:
                    print(f"{'You won!' if winner == 'X' else 'AI won!'}")
                else:
                    print(f"{'You won!' if winner == 'O' else 'AI won!'}")
            else:
                print(f"The winner is {'player 1' if winner == 'X' else 'player 2'}")

            exit()


