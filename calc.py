from tkinter import *
from tkinter import ttk
import tkinter

# Functions used for calculating result of multiplication, division, addition and substracion.
# Imported in main.py
def calc_ifs(A, B, sign):
    A, B = float(A), float(B)
    if sign == '+':
        AB=A+B
    elif sign == '-':
        AB=A-B
    elif sign == '*':
        AB=A*B
    elif sign == '/':
        AB=A/B
    if AB.is_integer():
        AB = int(AB)
    return str(AB)