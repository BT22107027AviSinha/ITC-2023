import tkinter as tk

def button_click(number):
    current_expression = expression_entry.get()
    expression_entry.delete(0, tk.END)
    expression_entry.insert(tk.END, current_expression + str(number))

def button_clear():
    expression_entry.delete(0, tk.END)

def button_add():
    current_expression = expression_entry.get()
    expression_entry.delete(0, tk.END)
    expression_entry.insert(tk.END, current_expression + "+")

def button_subtract():
    current_expression = expression_entry.get()
    expression_entry.delete(0, tk.END)
    expression_entry.insert(tk.END, current_expression + "-")

def button_multiply():
    current_expression = expression_entry.get()
    expression_entry.delete(0, tk.END)
    expression_entry.insert(tk.END, current_expression + "*")

def button_divide():
    current_expression = expression_entry.get()
    expression_entry.delete(0, tk.END)
    expression_entry.insert(tk.END, current_expression + "/")

def button_equal():
    expression = expression_entry.get()
    result = eval(expression)
    expression_entry.delete(0, tk.END)
    expression_entry.insert(tk.END, str(result))

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry field
expression_entry = tk.Entry(window, width=30)
expression_entry.grid(row=0, column=0, columnspan=4)

# Create the number buttons
button_1 = tk.Button(window, text="1", command=lambda: button_click(1))
button_1.grid(row=1, column=0)
button_2 = tk.Button(window, text="2", command=lambda: button_click(2))
button_2.grid(row=1, column=1)
button_3 = tk.Button(window, text="3", command=lambda: button_click(3))
button_3.grid(row=1, column=2)
button_4 = tk.Button(window, text="4", command=lambda: button_click(4))
button_4.grid(row=2, column=0)
button_5 = tk.Button(window, text="5", command=lambda: button_click(5))
button_5.grid(row=2, column=1)
button_6 = tk.Button(window, text="6", command=lambda: button_click(6))
button_6.grid(row=2, column=2)
button_7 = tk.Button(window, text="7", command=lambda: button_click(7))
button_7.grid(row=3, column=0)
button_8 = tk.Button(window, text="8", command=lambda: button_click(8))
button_8.grid(row=3, column=1)
button_9 = tk.Button(window, text="9", command=lambda: button_click(9))
button_9.grid(row=3, column=2)
button_0 = tk.Button(window, text="0", command=lambda: button_click(0))
button_0.grid(row=4, column=1)

# Create the operator buttons
button_plus = tk.Button(window, text="+", command=button_add)
button_plus.grid(row=1, column=3)
button_minus = tk.Button(window, text="-", command=button_subtract)
button_minus.grid(row=2, column=3)
button_multiply = tk.Button(window, text="*", command=button_multiply)
button_multiply.grid(row=3, column=3)
button_divide = tk.Button(window, text="/", command=button_divide)
button_divide.grid(row=4, column=3)

# Create the special buttons
button_clear = tk.Button(window, text="C", command=button_clear)
button_clear.grid(row=4, column=0)
button_equal = tk.Button(window, text="=", command=button_equal)
button_equal.grid(row=4, column=2)

# Start the main event loop
window.mainloop()
