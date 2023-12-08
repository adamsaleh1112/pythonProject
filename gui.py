#import all neceassary libraries
from tkinter import *
import tkinter as tk
from tkinter import ttk
from movement import *



# builds the gui with client's name
def backend(name):
  inner = Tk()
  inner.title("Welcome " + name)
  inner.geometry("900x825")

  frame1 = tk.Frame(inner, borderwidth=0, relief='ridge')
  frame1.grid(row=0, column=0, padx=(150, 150), pady=(70, 70))
  frame2 = tk.Frame(inner, borderwidth=0, relief='ridge')
  frame2.grid(row=0, column=1, padx=(150, 150), pady=(70, 70))
  frame3 = tk.Frame(inner, borderwidth=0, relief='ridge')
  frame3.grid(row=1, column=0, padx=(150, 150), pady=(70, 70))
  frame4 = tk.Frame(inner, borderwidth=0, relief='ridge', highlightbackground="black", highlightthickness = 5)
  frame4.grid(row=1, column=1, padx=(150, 150), pady=(70, 70))


  def updatelog():
    global logtext
    logtext = ""
    with open('log.txt', 'r') as f:
      lines = f.readlines()[-15:]
      for line in lines:
        line = str(line)
        logtext = logtext + line
    return (logtext)


  w4 = tk.Label(frame4, text = str(updatelog()), font = "90", fg="black")
  w4.grid(row=0, column=0)

  fwd = Button(frame2, text ='↑ ',height=3, width=8 , font = "90",fg="black", command = lambda: forward_and_update())
  fwd.grid(row=0, column=1, columnspan=2)

  lft = Button(frame2, text ='←',height=3, width=5 , font = "45", fg="black", command = lambda: left_and_update())
  lft.grid(row=1, column=0)

  rgt = Button(frame2, text='→',height=3, width=5 , font="45", fg="black", command = lambda: right_and_update())
  rgt.grid(row=1, column=3)

  bwd = Button(frame2, text ='↓',height=3, width=8 , font = "45", fg="black", command = lambda: backward_and_update())
  bwd.grid(row=2, column=1, columnspan=2)

  ply = Button(frame2, text='▶',height=3, width=2 , font="45", fg="Green", command=lambda: go_and_update())
  ply.grid(row=1, column=1)

  stp = Button(frame2, text='⏸',height=3, width=2 , font="45", fg="Red", command=lambda: stop_and_update())
  stp.grid(row=1, column=2)

  def forward_and_update(): #Forward command
    forward()
    w4.config(text=str(updatelog()))

  def left_and_update():
    left()
    w4.config(text=str(updatelog()))

  def right_and_update():
    right()
    w4.config(text=str(updatelog()))

  def backward_and_update():
    backward()
    w4.config(text=str(updatelog()))

  def go_and_update():
    go()
    w4.config(text=str(updatelog()))

  def stop_and_update():
    stop()
    w4.config(text=str(updatelog()))



  w3 = tk.Label(frame3, text ='Video', font = "90",fg="black")
  w3.grid(row=0, column=0)
  w3_1 = tk.Label(frame3, text ='Feed', font = "45", fg="black")
  w3_1.grid(row=1, column=0)

  w1 = tk.Label(frame1, text ='Blank', font = "90",fg="black")
  w1.grid(row=0, column=0)
  w1_1 = tk.Label(frame1, text ='Space', font = "45", fg="black")
  w1_1.grid(row=1, column=0)

  inner.mainloop()