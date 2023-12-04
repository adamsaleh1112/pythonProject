#import necessary libraries
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import os
import sqlite3
import random
from login import *
from createaccount import *
from gui import *
import os


if not os.path.exists("log.txt"):
    open("log.txt", "w").close()


#Builds Login Screen - has create account and make gui inside of it
loginscreen()