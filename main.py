#!/usr/bin/env python3
from tkinter import *
from tkinter import ttk
import tkinter
from calc import *

def button_calculator(equation):
    T.delete(0, 'end')
    global queue
    signs = ['+', '-', '*' , '/']
    A = ''
    B = ''
    sign = ''
    addingB = False
    for char in equation:
        if addingB == True:
            if char in signs:
                A = calc_ifs(A, B, sign)
                B = ''
                sign = char
                continue
            B += char
            continue
        if char in signs:
            sign = char
            addingB = True
            continue
        A += char
    AB = calc_ifs(A, B, sign)
    T.insert(0, AB)
    queue = AB
    return AB

def append(string):
    global queue
    queue = queue + string
    T.insert('end', string)

def empty():
    global queue
    queue = ''
    T.delete(0, 'end')

def backspace():
    global queue
    T.delete(len(queue)-1, 'end')
    queue = queue[:-1]

if __name__ == '__main__':
    queue = '' #FIFO
    root = Tk()
    T = tkinter.Entry(root, justify=RIGHT)
    T.grid(row=0)
    frame = ttk.Frame(root, padding=15)
    frame.grid()
    ttk.Label(frame, text='Very simple GUI calculator')
    b1 = ttk.Button(frame, text='1', command=lambda: append('1')).grid(column=1, row=1)
    b2 = ttk.Button(frame, text='2', command=lambda: append('2')).grid(column=2, row=1)
    b3 = ttk.Button(frame, text='3', command=lambda: append('3')).grid(column=3, row=1)
    b4 = ttk.Button(frame, text='4', command=lambda: append('4')).grid(column=1, row=2)
    b5 = ttk.Button(frame, text='5', command=lambda: append('5')).grid(column=2, row=2)
    b6 = ttk.Button(frame, text='6', command=lambda: append('6')).grid(column=3, row=2)
    b7 = ttk.Button(frame, text='7', command=lambda: append('7')).grid(column=1, row=3)
    b8 = ttk.Button(frame, text='8', command=lambda: append('8')).grid(column=2, row=3)
    b9 = ttk.Button(frame, text='9', command=lambda: append('9')).grid(column=3, row=3)
    b0 = ttk.Button(frame, text='0', command=lambda: append('9')).grid(column=2, row=4)
    bPlus = ttk.Button(frame, text='+', command=lambda: append('+')).grid(column=4, row=1)
    bMinus = ttk.Button(frame, text='-', command=lambda: append('-')).grid(column=4, row=2)
    bMultiplicate = ttk.Button(frame, text='*', command=lambda: append('*')).grid(column=4, row=3)
    bDivide = ttk.Button(frame, text='/', command=lambda: append('/')).grid(column=4, row=4)
    bEquals = ttk.Button(frame, text='=', command=lambda: button_calculator(queue)).grid(column=3, row=4)
    bClear = ttk.Button(frame, text='C', command=lambda: empty()).grid(column=4, row=0)
    bDelete = ttk.Button(frame, text='Del', command=lambda: backspace()).grid(column=3, row=0)
    bExit = ttk.Button(frame, text='EXIT', command=root.destroy).grid(column=1, row=4)
    root.mainloop()