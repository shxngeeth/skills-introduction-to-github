# #from tkinter import *
#
# # Function to handle button clicks
# def button_click(value):
#     current_text = entry.get()
#     entry.delete(0, END)
#     entry.insert(0, current_text + str(value))
#
# # Function to clear the input field
# def clear():
#     entry.delete(0, END)
#
# # Function to evaluate the expression
# def evaluate():
#     try:
#         result = eval(entry.get())  # Safely evaluate the expression
#         entry.delete(0, END)
#         entry.insert(0, str(result))
#     except Exception as e:
#         entry.delete(0, END)
#         entry.insert(0, "Error")
#
# # Create the main window
# window = Tk()
# window.title("Shxngeeth Calculator")
# window.geometry("400x500")
#
# # Entry widget to display the input and output
# entry = Entry(window, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
# entry.grid(row=0, column=0, columnspan=4, pady=10)
#
# # Define button labels and positions
# buttons = [
#     ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
#     ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
#     ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
#     ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
# ]
#
# # Create and place buttons dynamically
# for (text, row, col) in buttons:
#     if text == "=":
#         btn = Button(window, text=text, width=4, height=2, bg="lightgreen", command=evaluate)
#     elif text == "C":
#         btn = Button(window, text=text, width=4, height=2, bg="red", fg="white", command=clear)
#     else:
#         btn = Button(window, text=text, width=4, height=2, command=lambda val=text: button_click(val))
#     btn.grid(row=row, column=col, padx=5, pady=5)
#
# # Run the Tkinter event loop
# window.mainloop()

# from tkinter import *
# window=Tk()
# window.title("Shxngeeth Calculator")
# window.geometry("600x600")
# frame=Frame(window)
# bt1=Button(text=1,width=4, height=2)
# bt1.grid(row=0, column=2)
#
# bt2=Button(text=1,width=4, height=2)
# bt2.grid(row=0, column=2)
import tkinter as tk
calculation=""

def add_to_calculation(symbol):
    pass

def evaluate_calculation():
    pass

def clear_field():
    pass

root= tk.Tk()
root.geometry("300x275")

text_result= tk.Text(root, height=2, width=16, font=('Arial', 24))
text_result.grid(columnspan=5)
root.mainloop()