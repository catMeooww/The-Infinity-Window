from tkinter import *
import keyboard
import time
import random
import webbrowser

isPlaying = True
title = "Try Escaping this! Lol!"
titles = [
      "Not this Way",
      "It was a good try",
      "You remember that this is Infinity? Right?",
      "This window is trolling you! LOL!"
]

escapeTexts1 = [
    "Nice Try, Bakka",
    "You Can't",
    "Stop It",
    "If you don't escape, you gay",
    "Why you still trying",
    "Bruh",
    "Give Up",
    "You Annoying",
    "...",
    "Nope",
    "Well,Well,Well...",
    "You failed",
    "Score = F",
    "Just press some other thing",
    "Sussy Button",
    "Game Over",
    "Stuck here forever",
    "Never Gonna Give you Up... But the button let you down",
    "Noob",
    "I Hacked your computer",
    "You're not escaping this",
    "English or Spanish",
    "Ask a friend for Help",
    "Go play Minecraft",
    "No",
    "):",
    "You Fell off",
    "You Dumb?"
]

escapeTexts2 = [
    "You got it Wrong",
    "Did you ever pick a key",
    "I'll let you escape if you have the key",
    "If you don't pick the key, you gay",
    "Just DO it",
    "Bruh",
    "please",
    "You Annoying",
    "...",
    "Nope",
    "Well,Well,Well...",
    "You failed",
    "I won't tell what is the right",
    "Just press some other key",
    "Sussy Key",
    "Game Over",
    "Stuck here forever",
    "Never Gonna Give you Up... But the key let you down",
    "Skill Issue",
    "Limbo",
    "Just pick the KEY",
    "Why you...",
    "Focus",
    "D:",
    "No",
    "):",
    "Its not that hard!",
    "You Dumb?"
]

key = random.randint(1,10)
isKeyCorrect = 0

def giveUp1():
      tip['text'] = "Ok, press SHIFT and click the button"
def giveUp2():
      tip['text'] = f"Key: {key}"

def escape2():
    global isPlaying
    if isKeyCorrect == 1:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        isPlaying = False
   
        time.sleep(1)

        theWindow.destroy()
    else:
        mainLabel['text'] = escapeTexts2[random.randint(0,len(escapeTexts2) - 1)]

def escape1():  
    shiftPressed = 0
    if keyboard.is_pressed('shift'):
        shiftPressed = 1
        mainLabel['text'] = "You Actually did it... To the second Level HAHAHA"
        levelLabel['text'] = "-Level 2-"
        time.sleep(2)
        escapeBtn['command'] = escape2
        keyGrid.grid(column=0,row=3,pady=20)
        giveUpBtn['command'] = giveUp2
    elif shiftPressed == 0:
        mainLabel['text'] = escapeTexts1[random.randint(0,len(escapeTexts1) - 1)]

def selectKey1():
        global isKeyCorrect
        global key
        if key == 1:
             isKeyCorrect = 1
             mainLabel['text'] = "impressive"
        else:
              key = random.randint(1,10)

def selectKey2():
        global isKeyCorrect
        global key
        if key == 2:
             isKeyCorrect = 1
             mainLabel['text'] = "impressive"
        else:
              key = random.randint(1,10)

def selectKey3():
        global isKeyCorrect
        global key
        if key == 3:
             isKeyCorrect = 1
             mainLabel['text'] = "impressive"
        else:
              key = random.randint(1,10)

def selectKey4():
        global isKeyCorrect
        global key
        if key == 4:
             isKeyCorrect = 1
             mainLabel['text'] = "impressive"
        else:
              key = random.randint(1,10)

def selectKey5():
        global isKeyCorrect
        global key
        if key == 5:
             isKeyCorrect = 1
             mainLabel['text'] = "impressive"
        else:
              key = random.randint(1,10)

def selectKey6():
        global isKeyCorrect
        global key
        if key == 6:
             isKeyCorrect = 1
             mainLabel['text'] = "impressive"
        else:
              key = random.randint(1,10)

def selectKey7():
        global isKeyCorrect
        global key
        if key == 7:
             isKeyCorrect = 1
             mainLabel['text'] = "impressive"
        else:
              key = random.randint(1,10)

def selectKey8():
        global isKeyCorrect
        global key
        if key == 8:
             isKeyCorrect = 1
             mainLabel['text'] = "impressive"
        else:
              key = random.randint(1,10)

def selectKey9():
        global isKeyCorrect
        global key
        if key == 9:
             isKeyCorrect = 1
             mainLabel['text'] = "impressive"
        else:
              key = random.randint(1,10)

def selectKey10():
        global isKeyCorrect
        global key
        if key == 10:
             isKeyCorrect = 1
             mainLabel['text'] = "impressive"
        else:
              key = random.randint(1,10)

while isPlaying:
    theWindow = Tk()
    theWindow.title(title)
    theWindow.geometry("1250x600")

    dataGrid = Frame(theWindow,width=100,height=550,bg='cyan', relief = RIDGE, borderwidth = '8')
    dataGrid.grid(column=0,row=0,)
    gameGrid = Frame(theWindow,width=800,height=550, relief = RIDGE, borderwidth = '8')
    gameGrid.grid(column=1,row=0)

    levelLabel = Label(dataGrid,bg='cyan',text="-Level 1-",font=("Arial", 15))
    levelLabel.grid(column=0, row=0)
    division = Label(dataGrid,text="--------------------",bg='cyan',font=("Arial", 15))
    division.grid(column=0, row=1,pady=20,padx=5)
    tip = Label(dataGrid,text="I'm not telling the secret",bg='cyan')
    tip.grid(column=0, row=2)
    giveUpBtn = Button(dataGrid,text="Give Up",command=giveUp1)
    giveUpBtn.grid(column=0, row=3)

    mainLabel = Label(gameGrid,text="Try to Escape!",font=("Arial", 25) )
    mainLabel.grid(column=0, row=1, padx=230, pady=150)
    escapeBtn = Button(gameGrid,text="ESCAPE",command=escape1)
    escapeBtn.grid(column=0,row=2)

    keyGrid = Frame(gameGrid)
    keyLabel = Label(keyGrid,text="---Select The Right Key---")
    keyLabel.grid(column=4,row=0)
    key1 = Button(keyGrid,text="🗝",command=selectKey1)
    key2 = Button(keyGrid,text="🗝",command=selectKey2)
    key3 = Button(keyGrid,text="🗝",command=selectKey3)
    key4 = Button(keyGrid,text="🗝",command=selectKey4)
    key5 = Button(keyGrid,text="🗝",command=selectKey5)
    key6 = Button(keyGrid,text="🗝",command=selectKey6)
    key7 = Button(keyGrid,text="🗝",command=selectKey7)
    key8 = Button(keyGrid,text="🗝",command=selectKey8)
    key9= Button(keyGrid,text="🗝",command=selectKey9)
    key10 = Button(keyGrid,text="🗝",command=selectKey10)
    key1.grid(column=0,row=1)
    key2.grid(column=1,row=1)
    key3.grid(column=2,row=1)
    key4.grid(column=3,row=1)
    key5.grid(column=4,row=1)
    key6.grid(column=5,row=1)
    key7.grid(column=6,row=1)
    key8.grid(column=7,row=1)
    key9.grid(column=8,row=1)
    key10.grid(column=9,row=1)

    theWindow.mainloop()
    title = titles[random.randint(0,len(titles)-1)]
