
import tkinter as tk # Importing UI library for python, tkinter, allowing to make buttons and text labels
from tkinter import ttk # Importing specific part of tkinter
import sqlite3 # Importing sqlite3 which allows SQL queries to be called in python
import random # Importing random library, which allows for random values to be generated
from tkinter import * # Importing everything in tkinter
from tkinter import messagebox # Importing messagebox from tkinter, allowing for message box pop-ups
import os # Importing file managing library, which allows for editing and reading other files

from createaccount import * # Importing everything from createaccount.py
from gui import * # Importing everything from gui.py

db = sqlite3.connect('database.db') # Setting query destination to database.db
cursor = db.cursor() # Setting up query-er


def loginscreen():
    # builds internal screen
    def login(): # Getting username and password
        user = username.get()
        passw = pasword.get()

        # Finding username and password in database
        cursor.execute(
            f"SELECT fn FROM database WHERE username = '{user}' AND password = '{passw}'"
        )
        name = cursor.fetchone()

        if name:
            name = str(name)
            name = name[2:len(name) - 3]
            root.destroy()
            backend(name)

            with open('usernamelog.txt', 'w') as f:
                f.write(user)
        else:
            messagebox.showinfo("Username or password does not exist", "Please try again")

    # ------------------------------------------

    # Log In Screen
    root = Tk()
    root.geometry("500x500") # Setting dimensions

    root.title("Sign-in or Create an Account") # Setting title

    L1 = Label(root, text="Username: ") # Label for top textbox
    L1.grid(row=0, column=0) # Position for top textbox

    L2 = Label(root, text="Password: ") # Label for bottom textbox
    L2.grid(row=1, column=0) # Position for bottom textbox

    e1 = StringVar() # Setting top textbox variable
    e2 = StringVar() # Setting bottom textbox variable

    username = Entry(root, textvariable=e1) # Assigning top textbox var to top texbox
    username.grid(row=0, column=1) # Positioning top textbox

    pasword = Entry(root, textvariable=e2, show="\u00B7")  # Assigining bottom textbox var to bottom textbox + masks password
    pasword.grid(row=1, column=1) # Positioning bottom textbox

    lgn_button = Button(root, text="Login", command=lambda: login()) # Creating login button and assinging it to login function
    lgn_button.grid(row=4, column=1) # Positioning login button

    create_button = Button(root, text="Create new account", command=lambda: cw()) # Creating create account button and assigning it to create account window function
    create_button.grid(row=5, column=1) # Positioning create account button

    root.mainloop() # Running windows
