# This project is inspired from the famous "POMODORO" technique
# in this technique, the one is supposed to
# - focus on one thing for 25 mins, then take a 5 mins break 
# - after repeating this 4 times, take a longer break of 15 to 20 mins

workMin = 25
shortBreak = 5
longBreak = 20
reps = 0
mainTimer = None


from tkinter import *
import math

# Countdown

def countDown(count):
    
    # converting seconds to minutes
    mins = math.floor( count / 60 )
    secs = count % 60
    if secs < 10:   # TO show 5:00 instead of just 5:0
        secs = f"0{secs}"
    # Python is a dynamic langauge means a variable can convert to str or int automatically and implicitily

    # Changing the timer text 
    canvas.itemconfig(timer, text= f"{mins}:{secs}")
    
    if(count > 0):
        
        global mainTimer
        
        mainTimer = win.after(1000,countDown, count-1)
        # 1000 means 1 second
        # countDown - Recursion
        # count -1 => if count is starting at 3, then count-1 = 2, then count-1 = 1 and then 0
    else:
        Start()
        
            

def Start():
    
    global reps
    
    reps += 1
    
    workSec = workMin * 60
    shortSec = shortBreak * 60
    longSec = longBreak * 60
    
    if reps % 8 == 0:
        info.config(text="Break")
        countDown(longSec)
        
    elif reps % 2 == 0:
        info.config(text="Break")
        countDown(shortSec)
        
    else:
        countDown(workSec)
        info.config(text="Focus")
        
         

def Reset():
    # Changing the timer text 
    win.after_cancel(mainTimer)
    canvas.itemconfig(timer, text="00:00")
    info.config(text="Welcome")
    
    global reps
    reps = 0
    


win = Tk()
win.title("The Pomodoro Timer")
win.config(padx=50, pady=50, bg="#FFD4D4")


# EVENT DRIVEN  - we wanna check after each second, if there are any changes or not
# IF there are, then we can act as per it, such programs are called as Event driven

# def some(word):
#     print(word)
    
# win.after(1000, some, "DAY")



# To hold the picture
canvas = Canvas(width=700,height=550, bg="#FFD4D4", highlightthickness=0)   # highlightthickness to remove border

# we cannot mention the picture directly, 
# we need to use class to run through the directories and get our image
thePIC = PhotoImage(file = "p1.png")

# Now we can create the image
canvas.create_image(350, 250, image = thePIC)   # 200 x 200 are (x,y) to put the image
canvas.pack()


timer = canvas.create_text(190,140,text="00:00", fill="dark green", font=("Arial", 30, "bold"))


# Creating the buttons

start = Button(command = Start,text = "Start", highlightthickness=0, font=("Arial", 14, "bold"), padx = 30, pady = 3,  bg="dark green", fg="white")
start.place(x=100,y=520)

reset = Button(command=Reset,text = "Reset", highlightthickness=0 ,font=("Arial", 14, "bold"), padx = 30, pady = 3,  bg="dark blue", fg="white")
reset.place(x=470,y=520)


# Text


info = Label(text="Welcome", fg="crimson", bg="#FFD4D4", font=("Arial", 28, "bold"))
info.place(x = 300, y = -45)

win.mainloop()