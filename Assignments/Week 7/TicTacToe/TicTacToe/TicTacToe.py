import numpy as np
def check_all_spaces(board):
    if ' ' not in board:
        return True
    else:
        return False
def check_o_player(board):
        win = False
        # check horizontally
        if board[0, 0] == 'O' and board[0, 1] == 'O' and board[0, 2] == 'O':
            win = True
        elif board[1, 0] == 'O' and board[1, 1] == 'O' and board[1, 2] == 'O':
            win = True
        elif board[2, 0] == 'O' and board[2, 1] == 'O' and board[2, 2] == 'O':
             win = True
        # check vertically
        elif board[0, 0] == 'O' and board[1, 0] == 'O' and board[2, 0] == 'O':
            win = True
        elif board[0, 1] == 'O' and board[1, 1] == 'O' and board[2, 1] == 'O':
            win = True
        elif board[0, 2] == 'O' and board[1, 2] == 'O' and board[2, 2] == 'O':
            win = True
        # check diagonally
        elif board[0, 0] == 'O' and board[1, 1] == 'O' and board[2, 2] == 'O':
            win = True
        elif board[0, 2] == 'O' and board[1, 1] == 'O' and board[2, 0] == 'O':
            win = True
        return win
def check_x_player(board):
        win = False
        # check horizontally
        if board[0, 0] == 'X' and board[0, 1] == 'X' and board[0, 2] == 'X':
            win = True
        elif board[1, 0] == 'X' and board[1, 1] == 'X' and board[1, 2] == 'X':
            win = True
        elif board[2, 0] == 'X' and board[2, 1] == 'X' and board[2, 2] == 'X':
             win = True
        # check vertically
        elif board[0, 0] == 'X' and board[1, 0] == 'X' and board[2, 0] == 'X':
            win = True
        elif board[0, 1] == 'X' and board[1, 1] == 'X' and board[2, 1] == 'X':
            win = True
        elif board[0, 2] == 'X' and board[1, 2] == 'X' and board[2, 2] == 'X':
            win = True
        # check diagonally
        elif board[0, 0] == 'X' and board[1, 1] == 'X' and board[2, 2] == 'X':
            win = True
        elif board[0, 2] == 'X' and board[1, 1] == 'X' and board[2, 0] == 'X':
            win = True
        return win
    
def main():
    try:
        board = np.array([[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']])
        print(board)
        condition = False
        global player1entered
        global player2entered
        while condition == False:
            player1entered = False
            player2entered = False
            while player1entered == False:
                player1row = int(input('Enter a row (0, 1, or 2) for player X: '))
                player1col = int(input('Enter a column (0, 1, or 2) for player X: '))
                if board[player1row, player1col] == ' ':
                    board[player1row, player1col] = 'X'
                    player1entered = True
                else:
                    print('That space is already taken.')
            board[player1row, player1col] = 'X'
            print(board)
            x_status = check_x_player(board)
            check_board = check_all_spaces(board)
            if check_board == True:
                print('Tie game')
                break
            if x_status == True:
                print('X player won')
                break
            while player2entered == False:
                player2row = int(input('Enter a row (0, 1, or 2) for player O: '))
                player2col = int(input('Enter a column (0, 1, or 2) for player O: '))
                if board[player2row, player2col] == ' ':
                    board[player2row, player2col] = 'O'
                    player2entered = True
                else:
                    print('That space is already taken.')
            board[player2row, player2col] = 'O'
            print(board)
            o_status = check_o_player(board)
            check_board_again = check_all_spaces(board)
            if check_board_again == True:
                print('Tie game')
                break
            if o_status == True:
                print('O player won')
                break
    except ValueError:
        print('Invalid input')
        exit()
    except IndexError:
        print('Invalid input')
        exit()
if __name__ == "__main__":
    main()
