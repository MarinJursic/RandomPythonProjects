import random
import os
import tkinter as tk
from PIL import  ImageTk, Image
import time
from tkinter import messagebox
import re
from functools import partial

def Interface():

    HEIGHT = 600
    WIDTH = 500

    root = tk.Tk()

    root.title("Captcha")

    root.resizable(False, False)

    canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH, bg="#AAC8FF")
    canvas.pack()

    xAxis = 0.0235
    yAxis = 0.17
    width = 0.31
    height = 0.265

    path = r"C:\Users\Korisnik\Desktop\Project Files\Captcha\Images"
    WrongType = os.listdir(path)

    CorrectType = WrongType[random.randrange(0, len(WrongType))]

    WrongType.remove(CorrectType)

    CorrectPath = os.path.join(path, CorrectType)

    CorrectImages = os.listdir(CorrectPath)

    count = 0

    count2 = 0

    global num

    num = 0

    global num2

    num2 = 0

    global presses

    presses = 0

    global CorrectAnswers

    CorrectAnswers = random.randrange(3, 6)

    WrongAnswers = 9 - CorrectAnswers

    global WrongImages

    print("Correct Answers = " + str(CorrectAnswers))
    print("Wrong Answers = " + str(WrongAnswers))

    global CorrectPresses

    CorrectPresses = 0

    global blacklist

    blacklist = []

    global blacklist2

    blacklist2 = []

    global incorrect

    incorrect = 0

    Label = tk.Label(canvas, bg="#045DFF", text="Select all pictures with:\n" + CorrectType, foreground="white", font="Courier")
    Label.place(relheight=0.15, relwidth=1)

    image = Image.open(r"C:\\Users\Korisnik\Desktop\Project Files\Captcha\dVHQiE0t_400x400.png")
    image = image.resize((70, 70), Image.ANTIALIAS)

    captcha = ImageTk.PhotoImage(image)

    Button = tk.Button(Label, image=captcha, command=lambda root=root:reset(root))
    Button.place(relx=0.02, rely=0.02, relwidth=0.15, relheight=0.9)

    Button = tk.Button(Label, image=captcha, command=lambda root=root:reset(root))
    Button.place(relx=0.83, rely=0.02, relwidth=0.15, relheight=0.9)

    while xAxis < 0.96:

        while yAxis < 0.99:

            num = random.randrange(0,2)

            if num == 0:

                if count < CorrectAnswers:

                    Img = CorrectImages[random.randrange(0,len(CorrectImages))]

                    for photo in blacklist:

                        while Img == photo:

                            Img = CorrectImages[random.randrange(0, len(CorrectImages))]

                    ImgPath = os.path.join(CorrectPath,Img)

                    blacklist.append(Img)

                    img = tk.PhotoImage(file=ImgPath, master=root)

                    label = tk.Label(root, image=img)
                    label.image = img

                    validatePress = partial(OnClick, CorrectType, ImgPath, root)

                    frame = tk.Frame(canvas, bg="blue")
                    frame.place(relx=xAxis, rely=yAxis, relwidth=width, relheight=height)

                    button = tk.Button(root, bg="white", image=img, command=validatePress)
                    button.place(relx=xAxis, rely=yAxis, relwidth=width, relheight=height)

                    count = count + 1

                else:

                    if count2 < WrongAnswers:

                        randomFolder = WrongType[random.randrange(0,len(WrongType))]

                        randomPath = os.path.join(path, randomFolder)

                        WrongImages = os.listdir(randomPath)

                        Img = WrongImages[random.randrange(0,len(WrongImages))]

                        for photo in blacklist:

                            while Img == photo:

                                Img = WrongImages[random.randrange(0, len(WrongImages))]

                        ImgPath = os.path.join(randomPath,Img)

                        blacklist.append(Img)

                        img = tk.PhotoImage(file=ImgPath, master=root)

                        label = tk.Label(root, image=img)
                        label.image = img

                        validatePress = partial(OnClick, CorrectType, ImgPath, root)

                        frame = tk.Frame(canvas, bg="blue")
                        frame.place(relx=xAxis, rely=yAxis, relwidth=width, relheight=height)

                        button = tk.Button(root, bg="white", image=img, command=validatePress)
                        button.place(relx=xAxis, rely=yAxis, relwidth=width, relheight=height)

                        count2 = count2 + 1



            if num == 1:

                if count2 < WrongAnswers:

                    randomFolder = WrongType[random.randrange(0, len(WrongType))]

                    randomPath = os.path.join(path, randomFolder)

                    WrongImages = os.listdir(randomPath)

                    Img = WrongImages[random.randrange(0, len(WrongImages))]

                    for photo in blacklist:

                        while Img == photo:
                            Img = WrongImages[random.randrange(0, len(WrongImages))]

                    ImgPath = os.path.join(randomPath, Img)

                    blacklist.append(Img)

                    img = tk.PhotoImage(file=ImgPath, master=root)

                    label = tk.Label(root, image=img)
                    label.image = img

                    validatePress = partial(OnClick, CorrectType, ImgPath, root)

                    frame = tk.Frame(canvas, bg="blue")
                    frame.place(relx=xAxis, rely=yAxis, relwidth=width, relheight=height)

                    button = tk.Button(root,bg="white", image=img, command=validatePress)
                    button.place(relx=xAxis, rely=yAxis, relwidth=width, relheight=height)

                    count2 = count2 + 1


                else:

                    if count < CorrectAnswers:

                        Img = CorrectImages[random.randrange(0, len(CorrectImages))]

                        for photo in blacklist:

                            while Img == photo:

                                Img = CorrectImages[random.randrange(0, len(CorrectImages))]


                        ImgPath = os.path.join(CorrectPath, Img)

                        blacklist.append(Img)

                        img = tk.PhotoImage(file=ImgPath, master=root)

                        label = tk.Label(root, image=img)
                        label.image = img

                        validatePress = partial(OnClick, CorrectType, ImgPath, root)

                        frame = tk.Frame(canvas, bg="blue")
                        frame.place(relx=xAxis, rely=yAxis, relwidth=width, relheight=height)

                        button = tk.Button(root, bg="white", image=img, command=validatePress)
                        button.place(relx=xAxis, rely=yAxis, relwidth=width, relheight=height)

                        count = count + 1


            yAxis = yAxis + height + 0.01


        xAxis = xAxis + width + 0.01
        yAxis = 0.17


    root.mainloop()


def reset(root):

    root.destroy()

    root = tk.Tk()

    canvas = tk.Canvas(root)
    canvas.place(width=100,height=50)

    messagebox.showinfo("Resetting Captcha", "Resetting Captcha. Press OK")

    root.destroy()

    time.sleep(1)

    Interface()

def OnClick(CorrectType, image, root):

    global presses

    global CorrectPresses

    global CorrectAnswers

    global blacklist2

    Pt = re.compile(CorrectType)

    Found = Pt.search(image)

    global incorrect

    if Found:

        for photo in blacklist2:

            if photo == image:

                if incorrect == 3:

                    reset(root)

                else:

                    print("Already pressed")

                    incorrect = incorrect + 1

                    return None



        CorrectPresses += 1
        print("Pressed good\nYou are " + str(CorrectPresses) + "/" + str(CorrectAnswers))

        blacklist2.append(image)

    else:

        print("Pressed wrong")


    if CorrectPresses == CorrectAnswers:

        messagebox.showinfo("Bravo", "Bravo")

        exit()



Interface()