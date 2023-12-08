
from tkinter import * # Importing everything in tkinter
import tkinter as tk # Importing specific part of tkinter
from tkinter import ttk # Importing specific part of tkinter
from movement import * # Importing everything from movement



def backend(name): # Function thta creates window titled the first name of the username that logged in
  inner = Tk() # Creating window
  inner.title("Welcome " + name) # Creating title
  inner.geometry("900x825") # Setting dimensions

  frame1 = tk.Frame(inner, borderwidth=0, relief='ridge') # Creating top left frame
  frame1.grid(row=0, column=0, padx=(150, 150), pady=(70, 70))
  frame2 = tk.Frame(inner, borderwidth=0, relief='ridge') # Creating top right frame
  frame2.grid(row=0, column=1, padx=(150, 150), pady=(70, 70))
  frame3 = tk.Frame(inner, borderwidth=0, relief='ridge') # Creating bottom left frame
  frame3.grid(row=1, column=0, padx=(150, 150), pady=(70, 70))
  frame4 = tk.Frame(inner, borderwidth=0, relief='ridge', highlightbackground="black", highlightthickness = 5) # Creating bottom right
  frame4.grid(row=1, column=1, padx=(150, 150), pady=(70, 70))


  def updatelog(): # Function for log updating
    global logtext
    logtext = "" # Initializing varible
    with open('log.txt', 'r') as f: # Opening log.txt
      lines = f.readlines()[-15:] # Reading last 14 lines
      for line in lines: # Iterating lines
        line = str(line)
        logtext = logtext + line # Adding each iteration line to a variable
    return (logtext) # Returning chunk of log text


  w4 = tk.Label(frame4, text = str(updatelog()), font = "90", fg="black") # Creating log frame
  w4.grid(row=0, column=0)

  fwd = Button(frame2, text ='↑ ',height=3, width=8 , font = "90",fg="black", command = lambda: forward_and_update()) # Making forward button
  fwd.grid(row=0, column=1, columnspan=2)

  lft = Button(frame2, text ='←',height=3, width=5 , font = "45", fg="black", command = lambda: left_and_update()) # Making left button
  lft.grid(row=1, column=0)

  rgt = Button(frame2, text='→',height=3, width=5 , font="45", fg="black", command = lambda: right_and_update()) # Making right button
  rgt.grid(row=1, column=3)

  bwd = Button(frame2, text ='↓',height=3, width=8 , font = "45", fg="black", command = lambda: backward_and_update()) # Making backward button
  bwd.grid(row=2, column=1, columnspan=2)

  ply = Button(frame2, text='▶',height=3, width=2 , font="45", fg="Green", command=lambda: go_and_update()) # Making go button
  ply.grid(row=1, column=1)

  stp = Button(frame2, text='⏸',height=3, width=2 , font="45", fg="Red", command=lambda: stop_and_update()) # Making stop button
  stp.grid(row=1, column=2)

  def forward_and_update(): # Importing forward command and adding log update command to it to send to buttons
    forward()
    w4.config(text=str(updatelog()))

  def left_and_update(): # Importing left command and adding log update command to it to send to buttons
    left()
    w4.config(text=str(updatelog()))

  def right_and_update(): # Importing right command and adding log update command to it to send to buttons
    right()
    w4.config(text=str(updatelog()))

  def backward_and_update(): # Importing backward command and adding log update command to it to send to buttons
    backward()
    w4.config(text=str(updatelog()))

  def go_and_update(): # Importing go command and adding log update command to it to send to buttons
    go()
    w4.config(text=str(updatelog()))

  def stop_and_update(): # Importing stop command and adding log update command to it to send to buttons
    stop()
    w4.config(text=str(updatelog()))



  w3 = tk.Label(frame3, text ='Video', font = "90",fg="black") # Creating placeholder frame
  w3.grid(row=0, column=0)
  w3_1 = tk.Label(frame3, text ='Feed', font = "45", fg="black")
  w3_1.grid(row=1, column=0)

  w1 = tk.Label(frame1, text ='Blank', font = "90",fg="black") # Creating placeholder frame
  w1.grid(row=0, column=0)
  w1_1 = tk.Label(frame1, text ='Space', font = "45", fg="black")
  w1_1.grid(row=1, column=0)

  inner.mainloop()