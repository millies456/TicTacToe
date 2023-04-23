import random

def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" | ")
        print("\n-------------")

def check_win(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def get_random_move(board):
    valid_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(valid_moves)

def minimax(board, depth, maximizing_player):
    if check_win(board, 'X'):
        return 10 - depth
    elif check_win(board, 'O'):
        return depth - 10
    elif ' ' not in [cell for row in board for cell in row]:
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
        return min_eval

def get_best_move(board):
    max_eval = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                eval = minimax(board, 0, False)
                board[i][j] = ' '
                if eval > max_eval:
                    max_eval = eval
                    best_move = (i, j)
    return best_move

def main():
    board = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
    players = ['X', 'O']
    current_player = 0
    print_board(board)

    while True:
        if current_player == 0:
            # human player's turn
            row = int(input("Enter row number (1-3): ")) - 1
            col = int(input("Enter column number (1-3): ")) - 1
            if board[row][col] == ' ':
                board[row][col] = players[current_player]
                print_board(board)
                if check_win(board, players[current_player]):
                    print(players[current_player], "wins!")
                    break
                current_player = 1
                if ' ' not in [cell for row in board for cell in row]:
                    print("Tie!")
                    break

        else:
            # computer player's turn
            row, col = get_best_move(board)
            board[row][col] = players[current_player]
            print_board(board)
            if check_win(board, players[current_player]):
                print(players[current_player], "wins!")
                break
            current_player = 0
            if ' ' not in [cell for row in board for cell in row]:
                print("Tie!")
                break
if __name__ == '__main__':
    main()


           
