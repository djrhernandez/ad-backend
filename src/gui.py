import tkinter as tk
from tkinter import messagebox

def calculate(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {str(e)}"

def on_click(button_text, entry):
    if button_text == "=":
        result = calculate(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

def launch_gui():
    root = tk.Tk()
    root.title("Calculator")

    entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=2, relief="solid")
    entry.grid(row=0, column=0, columnspan=4)

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]

    for text, row, col in buttons:
        button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 18),
                           command=lambda t=text: on_click(t, entry))
        button.grid(row=row, column=col)

    root.mainloop()

if __name__ == "__main__":
    launch_gui()
