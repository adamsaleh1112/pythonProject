import tkinter as tk  # Importing UI library for python, tkinter, allowing to make buttons and text labels
from tkinter import ttk # Importing specific part of tkinter
from tkinter import * # Importing everything in tkinter
from tkinter import messagebox # Importing messagebox from tkinter, allowing for message box pop-ups
import sqlite3 # Importing sqlite3 which allows SQL queries to be called in python
import random # Importing random library, which allows for random values to be generated
from login import loginscreen # Importing login screen function from login.py
from createaccount import * # Importing everything from createaccount.py
from gui import * # Importing everything from gui.py
import os # Importing file managing library, which allows for editing and reading other files


if not os.path.exists("log.txt"): # Checks if log.txt doesnt exist
    open("log.txt", "w").close() # If not, then it creates one


#Builds Login Screen - has create account and make gui inside of it
loginscreen()