from collections import Counter
from copy import deepcopy
import time

START_DEPTH = 9

def minimax(boardValues, depth, alpha, beta, aiTurn):
    if depth == START_DEPTH - 1 and winCheck(boardValues):
        return 100, boardValues

    if depth == 0 or winCheck(boardValues):
        return getScore(boardValues), boardValues

    if aiTurn:
        maxEval = float("-inf")
        best_move = None
        for position in getAllMovesMinimax(boardValues, aiTurn):
            score = minimax(position, depth - 1, alpha, beta, False)[0]
            maxEval = max(maxEval, score)

            alpha = max(alpha, score)

            if maxEval == score:
                best_move = position

            if beta < alpha:
                break

        return maxEval, best_move

    else:
        minEval = float("inf")
        best_move = None
        for position in getAllMovesMinimax(boardValues, False):
            score = minimax(position, depth - 1, alpha, beta, True)[0]
            minEval = min(minEval, score)

            beta = min(beta, score)

            if minEval == score:
                best_move = position

            if beta < alpha:
                break

        return minEval, best_move

def getAllMovesMinimax(boardValues, aiTurn):
    boardValues_temp = deepcopy(boardValues)
    possible_moves = getAllPossibleMoves(boardValues_temp)
    positions = []

    for move in possible_moves:
        boardValues_temp = deepcopy(boardValues)
        positions.append(simulateMoves(boardValues_temp, move, aiTurn))

    return positions


def simulateMoves(boardValues, move, aiTurn):
    boardValues_temp = deepcopy(boardValues)
    if aiTurn:
        boardValues_temp = updateBoard(boardValues, move+1, "O")[0]
    else:
        boardValues_temp = updateBoard(boardValues, move+1, "X")[0]

    return boardValues_temp


def getPossibleWins(boardValues):
    board = []
    possible_wins = 0

    for i in range(0, 9, 3):
        board.append(boardValues[i:i + 3])

    # Lines check
    for row_num, row in enumerate(board):
        row_line = [j for j in row]

        numOfValues = Counter(row_line).most_common(1)[0][1]
        mostCommonValue = Counter(row_line).most_common(1)[0][0]

        if numOfValues == 2 and mostCommonValue != " ":
            possible_wins += 1

    for col_num, col in enumerate(board[0]):
        column_line = [board[col_val][col_num] for col_val, _ in enumerate(board)]

        numOfValues = Counter(column_line).most_common(1)[0][1]
        mostCommonValue = Counter(column_line).most_common(1)[0][0]

        if numOfValues == 2 and mostCommonValue != " ":
            possible_wins += 1

    # Diagonal check
    diagonal_line = [board[i][i] for i, _ in enumerate(board)]

    numOfValues = Counter(diagonal_line).most_common(1)[0][1]
    mostCommonValue = Counter(diagonal_line).most_common(1)[0][0]

    if numOfValues == 2 and mostCommonValue != " ":
        possible_wins += 1

    opposite_diagonal_line = [board[i][len(board[0]) - 1 - i] for i, _ in enumerate(board)]

    numOfValues = Counter(opposite_diagonal_line).most_common(1)[0][1]
    mostCommonValue = Counter(opposite_diagonal_line).most_common(1)[0][0]

    if numOfValues == 2 and mostCommonValue != " ":
        possible_wins += 1

    return possible_wins


def getScoreForPlayer(boardValues, player):
    board = []

    seenRowMove = {
        0: [],
        1: [],
        2: []
    }
    seenColMove = {
        0: [],
        1: [],
        2: []
    }
    seenDiagonalMove = {
        0: [],
        1: []
    }  # 0 is normal and 1 is opposite diagonal line

    score = 0
    score_add = 2
    score_take = 5
    possible_wins = getPossibleWins(boardValues)

    players = ["O", "X"]

    if player == players[0]:
        opposite_player = players[1]
    else:
        opposite_player = players[0]

    for i in range(0, 9, 3):
        board.append(boardValues[i:i + 3])

    print(board)

    # Lines check
    for row_num, row in enumerate(board):
        row_line = [j for j in row]

        numOfValues = Counter(row_line).most_common(1)[0][1]
        mostCommonValue = Counter(row_line).most_common(1)[0][0]

        if numOfValues == 2 and mostCommonValue == player and row_line not in seenRowMove[row_num]:
            seenRowMove[row_num].append(row_line)
            if opposite_player in row_line:
                score -= score_take
            score += score_add

    for col_num, col in enumerate(board[0]):
        column_line = [board[col_val][col_num] for col_val, _ in enumerate(board)]

        numOfValues = Counter(column_line).most_common(1)[0][1]
        mostCommonValue = Counter(column_line).most_common(1)[0][0]

        if numOfValues == 2 and mostCommonValue == player and column_line not in seenColMove[col_num]:
            seenColMove[col_num].append(column_line)
            if opposite_player in column_line:
                score -= score_take
            score += score_add

    # Diagonal check
    diagonal_line = [board[i][i] for i, _ in enumerate(board)]

    numOfValues = Counter(diagonal_line).most_common(1)[0][1]
    mostCommonValue = Counter(diagonal_line).most_common(1)[0][0]

    if numOfValues == 2 and mostCommonValue == player and diagonal_line not in seenDiagonalMove[0]:
        seenDiagonalMove[0].append(diagonal_line)
        if opposite_player in diagonal_line:
            score -= score_take
        score += score_add

    opposite_diagonal_line = [board[i][len(board[0]) - 1 - i] for i, _ in enumerate(board)]

    numOfValues = Counter(opposite_diagonal_line).most_common(1)[0][1]
    mostCommonValue = Counter(opposite_diagonal_line).most_common(1)[0][0]

    if numOfValues == 2 and mostCommonValue == player and opposite_diagonal_line not in seenDiagonalMove[1]:
        seenDiagonalMove[1].append(opposite_diagonal_line)
        if opposite_player in opposite_diagonal_line:
            score -= score_take
        score += score_add

    if possible_wins > 1:
        score -= possible_wins * 5

    #print(f"Possible wins: {possible_wins}, score: {score}")

    return score


def getScore(boardValues):

    score = getScoreForPlayer(boardValues, "O") - getScoreForPlayer(boardValues, "X")
    return score


def winCheck(boardValues):
    board = []

    for i in range(0, 9, 3):
        board.append(boardValues[i:i+3])

    # Lines check
    for row in board:
        row_line = [j for j in row]

        numOfValues = Counter(row_line).most_common(1)[0][1] / len(row_line)

        if numOfValues == 1 and row_line[0] != " ":
            return True

    for j, col in enumerate(board[0]):
        column_line = [board[col_val][j] for col_val, _ in enumerate(board)]

        numOfValues = Counter(column_line).most_common(1)[0][1] / len(column_line)

        if numOfValues == 1 and column_line[0] != " ":
            return True

    # Diagonal check
    diagonal_line = [board[i][i] for i, _ in enumerate(board)]
    opposite_diagonal_line = [board[i][len(board[0])-1-i] for i, _ in enumerate(board)]

    numOfValues = Counter(diagonal_line).most_common(1)[0][1] / len(diagonal_line)

    if numOfValues == 1 and diagonal_line[0] != " ":
        return True

    numOfValues = Counter(opposite_diagonal_line).most_common(1)[0][1] / len(diagonal_line)

    if numOfValues == 1 and opposite_diagonal_line[0] != " ":
        return True

    return False

def winPrint(player):
    print("")
    print("")
    print("")
    if player:
        print("PLAYER WON")
    else:
        print("PLAYER 2 WON")


def resetBoardValues():
    board = []
    for i in range(9):
        board.append(" ")

    return board


def printBoard(board):
    for line in board:
        print(line)


def makeBoard(boardValues):
    board = []

    for i in range(0, 9, 3):
        board.append("_______")
        board.append(f"|{boardValues[i]}|{boardValues[i+1]}|{boardValues[i+2]}|")
    board.append("_______")

    printBoard(board)

    return board


def updateBoard(boardValues, num, update):

    if boardValues[num-1] == " ":
        boardValues[num-1] = update
        return boardValues, None
    else:
        #print("ERROR ERROR ERROR")
        return boardValues, "Error"


def playerVSplayer():
    boardValues = resetBoardValues()
    running = True
    playerTurn = True

    while running:

        getScore(boardValues)

        print("")
        print("")
        print("")

        num = int(input("Upisi broj od 1 do 9: "))

        if 0 < num < 10:
            if playerTurn:
                if updateBoard(boardValues, num, "X")[1]:
                    print("Error")
                else:
                    boardValues = updateBoard(boardValues, num, "X")[0]
                    board = makeBoard(boardValues)

                    if winCheck(boardValues):
                        winPrint(playerTurn)
                        running = False

                    playerTurn = not playerTurn
            else:
                if updateBoard(boardValues, num, "O")[1]:
                    print("Error")
                else:
                    boardValues = updateBoard(boardValues, num, "O")[0]
                    board = makeBoard(boardValues)

                    if winCheck(boardValues):
                        winPrint(playerTurn)
                        running = False

                    playerTurn = not playerTurn
        else:
            print("Wrong num")


def getAllPossibleMoves(boardValues):
    moves = []

    for i, move in enumerate(boardValues):
        if move == " ":
            moves.append(i)

    #print(moves)
    return moves


def playerVSai():
    boardValues = resetBoardValues()
    running = True
    playerTurn = True
    time_of_calc = 0
    prev_time = 0.5

    while running:

        if playerTurn:
            print("")
            print("")
            print("")

            num = int(input("Upisi broj od 1 do 9: "))

            if 0 < num < 10:
                if updateBoard(boardValues, num, "X")[1]:
                        print("Error")
                else:
                    boardValues = updateBoard(boardValues, num, "X")[0]
                    board = makeBoard(boardValues)

                    if winCheck(boardValues):
                        winPrint(playerTurn)
                        running = False

                    playerTurn = not playerTurn
            else:
                print("Wrong num")
        else:
            start_time = time.time()
            print("Calculating...")

            print(f"Expect at least {round(prev_time, 2)} seconds")

            score, boardValues = minimax(boardValues, START_DEPTH, float("-inf"), float("inf"), True)

            print(f"Score of the move: {score}")
            time_of_calc = time.time() - start_time
            print(f"Time to calculate: {round(time_of_calc, 2)} seconds")
            prev_time = time_of_calc

            board = makeBoard(boardValues)

            if winCheck(boardValues):
                winPrint(playerTurn)
                running = False

            playerTurn = not playerTurn


choice = 0
while choice > 2 or choice < 1:
    choice = int(input("Press 1 if you want to play player VS player, \nand click 2 if you want to play against AI: "))

if choice == 1:
    playerVSplayer()
else:
    playerVSai()