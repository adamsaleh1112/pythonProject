
import tkinter as tk # Importing UI library for python, tkinter, allowing to make buttons and text labels
from tkinter import ttk # Importing specific part of tkinter
import sqlite3 # Importing sqlite3 which allows SQL queries to be called in python
import random # Importing random library, which allows for random values to be generated
from tkinter import * # Importing everything in tkinter
from tkinter import messagebox # Importing messagebox from tkinter, allowing for message box pop-ups
import os # Importing file managing library, which allows for editing and reading other files


db = sqlite3.connect('database.db') # Connecting queries to file 'database.db'
cursor = db.cursor() # Setting up database query-er

try: # Testing to see if file exists
    if os.path.exists("database.db"):
        pass # If it does, pass
except: # If it doesn't create a file called database.db
    os.mknod("database.db")

try:
    cursor.execute("SELECT id FROM database")
except:
    cursor.execute("CREATE TABLE database (id, fn, ln, username, password)")


# Checks if username already exists and if not, creates a new account
def create(fn, ln, username, password):
    cursor.execute(f"SELECT username FROM database WHERE username = '{username}'")
    un = cursor.fetchone()
    if un:
        messagebox.showinfo("Pick Something Else", "Username Already Exists")
    else:
        randy = random.randint(100000, 999999)
        cursor.execute(f"SELECT id FROM database WHERE id = '{randy}'")
        inty = cursor.fetchone()
        while inty:
            randy = random.randint(100000, 999999)
            cursor.execute(f"SELECT id FROM database WHERE id = '{randy}'")
            inty = cursor.fetchone()

        cursor.execute(
            f"INSERT INTO database VALUES ('{randy}', '{fn}', '{ln}', '{username}', '{password}')"
        )
        cursor.close()
        db.commit()

        messagebox.showinfo("Your account was created", "You can sign in now!")


# Makes the Create Window
def cw():
    root = Tk()
    root.geometry("500x500")
    root.title("Create Account")

    e1 = StringVar()
    e2 = StringVar()
    e3 = StringVar()
    e4 = StringVar()

    fn = Label(root, text="First name: ")
    fn.grid(row=0, column=0)
    enterfn = Entry(root, textvariable=e1)
    enterfn.grid(row=0, column=1)

    ln = Label(root, text="Last name: ")
    ln.grid(row=1, column=0)
    enterln = Entry(root, textvariable=e2)
    enterln.grid(row=1, column=1)

    user = Label(root, text="Username: ")
    user.grid(row=2, column=0)
    enteruser = Entry(root, textvariable=e3)
    enteruser.grid(row=2, column=1)

    password = Label(root, text="Password: ")
    password.grid(row=3, column=0)
    enterpass = Entry(root, textvariable=e4, show="\u00B7")  # masks password
    enterpass.grid(row=3, column=1)

    create_button = Button(root, text="Create account", command=lambda: create(enterfn.get(), enterln.get(), enteruser.get(), enterpass.get()))

    create_button.grid(row=4, column=0)