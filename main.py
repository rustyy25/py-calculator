import lib, tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Python Calculator")
root.geometry("400x400")
root.configure(bg="#f0f0f5")

def calculate():
    try:
        x = int(entry_x.get())
        y = int(entry_y.get())
        choice = int(option_var.get())
        
        if choice == 1:
            result = lib.add(x, y)
        elif choice == 2:
            result = lib.subtract(x, y)
        elif choice == 3:
            result = lib.multiply(x, y)
        elif choice == 4:
            if y == 0:
                raise ZeroDivisionError("Can't divide by 0")
            else:
                result = lib.divide(x, y)
        elif choice == 5:
            result = lib.exponent(x, y)
        elif choice == 6:
            if y == 0:
                raise ZeroDivisionError("Can't divide by 0")
            else:
                result = lib.module(x, y)
        
        show_result(result)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        messagebox.showerror("Error", str(e))

def show_result(result):
    messagebox.showinfo("Result", f"The result is: {result}")

input_frame = tk.Frame(root, bg="#e0e0eb", bd=5, relief="ridge")
input_frame.pack(pady=15, padx=10)

tk.Label(input_frame, text="Enter first number:", font=lib.font, bg="#e0e0eb").grid(row=0, column=0, padx=10, pady=5)
entry_x = tk.Entry(input_frame, font=(lib.font, 12), width=10, justify="center")
entry_x.grid(row=0, column=1, padx=10, pady=5)

tk.Label(input_frame, text="Enter second number:", font=lib.font, bg="#e0e0eb").grid(row=1, column=0, padx=10, pady=5)
entry_y = tk.Entry(input_frame, font=(lib.font, 12), width=10, justify="center")
entry_y.grid(row=1, column=1, padx=10, pady=5)

option_var = tk.StringVar(value="1")
operation_frame = tk.Frame(root, bg="#f0f0f5")
operation_frame.pack(pady=10)

tk.Label(operation_frame, text="Choose an operation:", font=(lib.font, 14, "bold"), bg="#f0f0f5").pack(anchor="w", padx=20)
tk.Label(operation_frame, text="", bg="#f0f0f5").pack()

operations = [
    ("1. Addition", 1),
    ("2. Subtraction", 2),
    ("3. Multiplication", 3),
    ("4. Division", 4),
    ("5. Exponentiation", 5),
    ("6. Modulus", 6)
]

for text, value in operations:
    tk.Radiobutton(operation_frame, text=text, variable=option_var, value=value, bg="#f0f0f5", font=(lib.font, 10), anchor="w").pack(anchor="w", padx=40)

calculate_button = tk.Button(root, text="Calculate", command=calculate, font=(lib.font, 12), bg="#4CAF50", fg="white", padx=15, pady=10)
calculate_button.pack(pady=(5,10))

root.mainloop()