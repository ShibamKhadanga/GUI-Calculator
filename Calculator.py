from tkinter import *


def click(event):
    global sv
    txt = event.widget.cget("text") # event.widget ---> give the button & .cget(text) ---> get text from button widget
    print(txt)
    if txt == "=":
        try:
            result = eval(sv.get())  # Evaluate the expression
            sv.set(result)  # Display result
        except Exception as e:
            sv.set("Error")  # Handle errors gracefully
        screen.update()
    elif txt == 'C':
        sv.set("")          # Clear the screen
        screen.update()
    elif txt == '<=':
        sv.set(sv.get()[:-1])    #Remove the last character
        screen.update()
    else:
        sv.set(sv.get() + txt)    # add clicked button value to screen value  
        screen.update()   # Update the screen


root = Tk()
root.geometry("355x600")  #applied width x height
root.title("Calculator - By Shibam K.") #Calculator Name


'''.......................................................................................'''
sv = StringVar()          # variable containing String value
sv.set("")
screen = Entry(root, textvar=sv, font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)
#................padx = distance of screen box from side margine
#................pady = distance of screen box from top margine


'''.......................................................................................'''
f1 = Frame(root, bg="grey")
b = Button(f1,text="C", padx=5, pady=5, font='lucida 25 bold')
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="<=", padx=5, pady=5, font='lucida 25 bold')
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="%", padx=5, pady=5, font='lucida 25 bold')
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="/", padx=5, pady=5, font='lucida 25 bold')
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack()


f1 = Frame(root, bg="grey")  # color of button background (frame color)

#................padx = x-axis of button
#................pady = y-axis of button
b = Button(f1,text="9", padx=10, pady=10, font='lucida 25 bold')
#................side=LEFT ---> next button will be on left side
#................By default it will be down
#................padx & pady ---> distace of button from frame margin and other button
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="8", padx=10, pady=10, font='lucida 25 bold')
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="7", padx=10, pady=10, font='lucida 25 bold')
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="*", padx=5, pady=10, font='lucida 25 bold')
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack()


f1 = Frame(root, bg="grey")
b = Button(f1,text="6", padx=10, pady=10, font='lucida 25 bold')
b.pack(side = LEFT, padx=11, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="5", padx=10, pady=10, font='lucida 25 bold')
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="4", padx=10, pady=10, font='lucida 25 bold')
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="-", padx=5, pady=10, font='lucida 25 bold')
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack()


f1 = Frame(root, bg="grey")
b = Button(f1,text="3", padx=10, pady=10, font='lucida 25 bold')
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="2", padx=10, pady=10, font='lucida 25 bold')
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="1", padx=10, pady=10, font='lucida 25 bold')
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="+", padx=2, pady=10, font='lucida 25 bold')
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

f1.pack()


f1 = Frame(root, bg="grey")
b = Button(f1,text="0", padx=8.5, pady=10, font='lucida 25 bold')
b.pack(side = LEFT, padx=9, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="00", padx=1.45
           , pady=10, font='lucida 25 bold')
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text=".", padx=9, pady=10, font='lucida 25 bold')
b.pack(side = LEFT, padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1,text="=", padx=8, pady=10, font='lucida 25 bold')
b.pack(side = LEFT, padx=11, pady=10)
b.bind("<Button-1>", click)

f1.pack()

root.mainloop()
