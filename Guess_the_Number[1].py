import tkinter as tk
import random as r
import time as t

#perparing!
random_var = r.randint(1, 100)
root = tk.Tk()
root.title("Guess the Number by Mithun Creations")
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

ti = tk.Entry(root)
ti.pack()
var = ti.get()

def lab ():
    label = tk.Label(root, text="Hello! Welcome to random!", fg="blue", font=("Speak Pro", 12, "bold"))
    label.pack()
def lab2 ():
    label2 = tk.Label (root, text=f"You Won! The answer is: {random_var}", fg = "green", font=("Speak Pro", 12, "bold")) 
    label2.pack()
def lab3 ():
    label3 = tk.Label (root, text=f"You Lost! The answer is: {random_var}", fg = "red", font=("Speak Pro", 12, "bold"))
    label3.pack()
def check ():
    root.update()
    root.update_idletasks()
    random_var = r.randint(1,100)

    if var == random_var:
        lab2()
    if not var == random_var:
        lab3()
button = tk.Button(root, text="Check your number", command=check)        
button.pack()
lab()

root.mainloop()
