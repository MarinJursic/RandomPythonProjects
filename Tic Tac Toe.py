import tkinter as tk
from PIL import  ImageTk, Image
import time
from tkinter import messagebox
from functools import partial
from collections import Counter
from copy import deepcopy
from math import inf

AI = 1
NOT_AI = 2

def Interface():

    HEIGHT = 600
    WIDTH = 500

    root = tk.Tk()

    root.title("Tic Tac Toe")

    root.resizable(False, False)

    canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH, bg="#4c4c4c")
    canvas.pack()

    xAxis = 0.0235
    yAxis = 0.17
    width = 0.31
    height = 0.265

    global count

    count = 0

    global Move

    Move = 1

    global Panel

    Panel = [[0 for i in range(3)] for j in range(3)]

    Label = tk.Label(canvas, bg="#a9957b", text="Tic Tac Toe\n" + "Player 1", foreground="white", font="Courier")
    Label.config(font=("Courier", 20, "bold"))
    Label.place(relheight=0.15, relwidth=1)

    image = Image.open(r"C:\\Users\Korisnik\Desktop\Pycharm Files\Tic Tac Toe\Circle.png")
    image = image.resize((70, 70), Image.ANTIALIAS)

    Circle = ImageTk.PhotoImage(image)

    Button = tk.Button(Label, image=Circle, command=lambda root=root:reset(root))
    Button.place(relx=0.02, rely=0.02, relwidth=0.15, relheight=0.9)

    image = Image.open(r"C:\\Users\Korisnik\Desktop\Pycharm Files\Tic Tac Toe\Cross.png")
    image = image.resize((70, 70), Image.ANTIALIAS)

    Cross = ImageTk.PhotoImage(image)

    Button = tk.Button(Label, image=Cross, command=lambda root=root:reset(root))
    Button.place(relx=0.83, rely=0.02, relwidth=0.15, relheight=0.9)

    while xAxis < 0.96:

        while yAxis < 0.99:

            validatePress = partial(OnClick, xAxis, yAxis, width, height,root,Label,Panel)


            frame = tk.Frame(canvas, bg="blue")
            frame.place(relx=xAxis, rely=yAxis, relwidth=width, relheight=height)

            button = tk.Button(root, bg="white",command=validatePress)
            button.place(relx=xAxis, rely=yAxis, relwidth=width, relheight=height)

            count = count + 1

            yAxis = yAxis + height + 0.01

        xAxis = xAxis + width + 0.01
        yAxis = 0.17


    root.mainloop()

def CheckForWinner(Panel):

    global Move

    if Panel[0][0] == 1 and Panel[0][1] == 1 and Panel[0][2] == 1:

        messagebox.showinfo("Tic Tac Toe", "Player 1 Won")
        exit()

    elif Panel[1][0] == 1 and Panel[1][1] == 1 and Panel[1][2] == 1:

        messagebox.showinfo("Tic Tac Toe", "Player 1 Won")
        exit()

    elif Panel[2][0] == 1 and Panel[2][1] == 1 and Panel[2][2] == 1:

        messagebox.showinfo("Tic Tac Toe", "Player 1 Won")
        exit()

    elif Panel[0][0] == 1 and Panel[1][0] == 1 and Panel[2][0] == 1:

        messagebox.showinfo("Tic Tac Toe", "Player 1 Won")
        exit()

    elif Panel[0][1] == 1 and Panel[1][1] == 1 and Panel[2][1] == 1:

        messagebox.showinfo("Tic Tac Toe", "Player 1 Won")
        exit()

    elif Panel[0][2] == 1 and Panel[1][2] == 1 and Panel[2][2] == 1:

        messagebox.showinfo("Tic Tac Toe", "Player 1 Won")
        exit()

    elif Panel[0][0] == 1 and Panel[1][1] == 1 and Panel[2][2] == 1:

        messagebox.showinfo("Tic Tac Toe", "Player 1 Won")
        exit()

    elif Panel[0][2] == 1 and Panel[1][1] == 1 and Panel[2][0] == 1:

        messagebox.showinfo("Tic Tac Toe", "Player 1 Won")
        exit()


   # Player 2


    if Panel[0][0] == 2 and Panel[0][1] == 2 and Panel[0][2] == 2:

        print(1)

        messagebox.showinfo("Tic Tac Toe", "Player 2 Won")
        exit()

    elif Panel[1][0] == 2 and Panel[1][1] == 2 and Panel[1][2] == 2:

        print(2)

        messagebox.showinfo("Tic Tac Toe", "Player 2 Won")
        exit()

    elif Panel[2][0] == 2 and Panel[2][1] == 2 and Panel[2][2] == 2:

        print(3)

        messagebox.showinfo("Tic Tac Toe", "Player 2 Won")
        exit()

    elif Panel[0][0] == 2 and Panel[1][0] == 2 and Panel[2][0] == 2:

        print(4)

        messagebox.showinfo("Tic Tac Toe", "Player 2 Won")
        exit()

    elif Panel[0][1] == 2 and Panel[1][1] == 2 and Panel[2][1] == 2:

        print(5)

        messagebox.showinfo("Tic Tac Toe", "Player 2 Won")
        exit()

    elif Panel[0][2] == 2 and Panel[1][2] == 2 and Panel[2][2] == 2:

        print(6)

        messagebox.showinfo("Tic Tac Toe", "Player 2 Won")
        exit()

    elif Panel[0][0] == 2 and Panel[1][1] == 2 and Panel[2][2] == 2:

        print(7)

        messagebox.showinfo("Tic Tac Toe", "Player 2 Won")
        exit()

    elif Panel[0][2] == 2 and Panel[1][1] == 2 and Panel[2][0] == 2:

        print(8)

        messagebox.showinfo("Tic Tac Toe", "AI Won")
        exit()

    if Move == 9:

        messagebox.showinfo("Tic Tac Toe", "Tie Game")
        exit()

    return False

def SaveInput(xAxis,yAxis,Player):

    global Panel

    if Player == 1:

        if xAxis == 0.0235 and yAxis == 0.17:

            Panel[0][0] = 1
        elif xAxis == 0.3435 and yAxis == 0.17:

            Panel[0][1] = 1
        elif xAxis == 0.6635 and yAxis == 0.17:

            Panel[0][2] = 1
        elif xAxis == 0.0235 and yAxis == 0.44500000000000006:

            Panel[1][0] = 1
        elif xAxis == 0.3435 and yAxis == 0.44500000000000006:

            Panel[1][1] = 1
        elif xAxis == 0.6635 and yAxis == 0.44500000000000006:

            Panel[1][2] = 1
        elif xAxis == 0.0235 and yAxis == 0.7200000000000001:

            Panel[2][0] = 1
        elif xAxis == 0.3435 and yAxis == 0.7200000000000001:

            Panel[2][1] = 1
        elif xAxis == 0.6635 and yAxis == 0.7200000000000001:

            Panel[2][2] = 1

    elif Player == 2:

        if xAxis == 0.0235 and yAxis == 0.17:

            Panel[0][0] = 2
        elif xAxis == 0.3435 and yAxis == 0.17:

            Panel[0][1] = 2
        elif xAxis == 0.6635 and yAxis == 0.17:

            Panel[0][2] = 2
        elif xAxis == 0.0235 and yAxis == 0.44500000000000006:

            Panel[1][0] = 2
        elif xAxis == 0.3435 and yAxis == 0.44500000000000006:

            Panel[1][1] = 2
        elif xAxis == 0.6635 and yAxis == 0.44500000000000006:

            Panel[1][2] = 2
        elif xAxis == 0.0235 and yAxis == 0.7200000000000001:

            Panel[2][0] = 2
        elif xAxis == 0.3435 and yAxis == 0.7200000000000001:

            Panel[2][1] = 2
        elif xAxis == 0.6635 and yAxis == 0.7200000000000001:

            Panel[2][2] = 2

    CheckForWinner(Panel)

    return None

def reset(root):

    root.destroy()

    root = tk.Tk()

    canvas = tk.Canvas(root)
    canvas.place(width=100,height=50)

    messagebox.showinfo("Resetting", "Resetting Tic Tac Toe")

    root.destroy()

    time.sleep(1)

    Interface()

def OnClick(xAxis,yAxis,width,height,root,Label,Panel):

    global Move
    global START_DEPTH

    if Move % 2 == 0:

        Player = 2

        button = tk.Button(root, bg="white",text="✗")
        button.config(font=("Courier", 60, "bold"))
        button.place(relx=xAxis, rely=yAxis, relwidth=width, relheight=height)

        SaveInput(xAxis,yAxis,Player)

        Move += 1

    else:

        Player = 1

        button = tk.Button(root, bg="white", text="〇")
        button.config(font=("Courier", 60, "bold"))
        button.place(relx=xAxis, rely=yAxis, relwidth=width, relheight=height)

        SaveInput(xAxis,yAxis,Player)

        Move += 1


    if Move % 2 == 0:

        Label.config(text="Tic Tac Toe\nPlayer 2")

    else:

        Label.config(text="Tic Tac Toe\nPlayer 1")

    if Move % 2 == 0:

        print("Start")
        print(Panel)

        result = [minimax(Panel,len(findPossibleMoves(Panel)),2)]

        print("Output: ")
        print(result)
        print("ZAKURAC SCORE: " + str(result[0][2]))

        move = [result[0][0],result[0][1]]

        Panel[move[0]][move[1]] = 2

        print(Panel)

        x,y = findPosition(move)

        OnClick(x,y,width,height,root,Label,Panel)

    return None

def findPosition(move):

    if move[0] == 0 and move[1] == 0:

        return 0.0235,0.17

    elif move[0] == 1 and move[1] == 0:

        return 0.0235,0.44500000000000006

    elif move[0] == 2 and move[1] == 0:

        return 0.0235,0.7200000000000001
    elif move[0] == 0 and move[1] == 1:

        return 0.3435,0.17
    elif move[0] == 1 and move[1] == 1:

        return 0.3435,0.44500000000000006
    elif move[0] == 2 and move[1] == 1:

        return 0.3435,0.7200000000000001
    elif move[0] == 0 and move[1] == 2:

        return 0.6635,0.17
    elif move[0] == 1 and move[1] == 2:

        return 0.6635,0.44500000000000006
    elif move[0] == 2 and move[1] == 2:

        return 0.6635,0.7200000000000001

def evaluate(state):

    if wins(state, AI):
        score = +1
    elif wins(state, NOT_AI):
        score = -1
    else:
        score = 0

    return score

def wins(state, player):

    # Check Row
    for row in state:
        if all([value == player for value in row]):
            return True

    # Check Collumn

    for x in range(3):
        if all([row[x] == player for row in state]):
            return True

    # Check Diagonals

    if state[0][0] == player and state[1][1] == player and state[2][2] == player:
        return True

    if state[0][2] == player and state[1][1] == player and state[2][0] == player:
        return True

    return False

def checkIfOver(state):

    return wins(state, NOT_AI) or wins(state, AI)

def findPossibleMoves(state):

    moves = []

    for x in range(3):
        for y in range(3):
            if state[x][y] == 0:
                moves.append([x,y])

    return moves

def minimax(state, depth, player):

    if player == AI:
        bestMove = [-1, -1, -inf]
    else:
        bestMove = [-1, -1, +inf]

    if depth == 0 or checkIfOver(state):
        score = evaluate(state)
        return [-1, -1, score]

    for move in findPossibleMoves(state):

        row, col = move[0], move[1]

        state[row][col] = player
        score = minimax(state, depth - 1, AI if player == 2 else NOT_AI)
        state[row][col] = 0
        score[0], score[1] = row, col

        if player == AI:
            if score[2] > bestMove[2]:
                bestMove = score
        else:
            if score[2] < bestMove[2]:
                bestMove = score

    return bestMove


Interface()