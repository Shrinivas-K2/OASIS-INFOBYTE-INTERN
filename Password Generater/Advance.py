import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("No character types selected. Please select at least one character type.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(length_var.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        result_var.set(password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Set up the main window
root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#f0f0f0")

# Variables for storing user options
length_var = tk.IntVar(value=12)
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)
result_var = tk.StringVar()

# Create frames
top_frame = tk.Frame(root, bg="#ffffff", pady=10, padx=10, bd=2, relief=tk.RIDGE)
top_frame.grid(row=0, column=0, padx=10, pady=5, sticky='ew')
middle_frame = tk.Frame(root, bg="#ffffff", pady=10, padx=10, bd=2, relief=tk.RIDGE)
middle_frame.grid(row=1, column=0, padx=10, pady=5, sticky='ew')
bottom_frame = tk.Frame(root, bg="#ffffff", pady=10, padx=10, bd=2, relief=tk.RIDGE)
bottom_frame.grid(row=2, column=0, padx=10, pady=5, sticky='ew')

# Top frame widgets
tk.Label(top_frame, text="Password Length:", bg="#ffffff").grid(row=0, column=0, sticky='e')
length_entry = tk.Entry(top_frame, textvariable=length_var)
length_entry.grid(row=0, column=1, padx=10, pady=5)

# Middle frame widgets
tk.Checkbutton(middle_frame, text="Include Letters", variable=letters_var, bg="#ffffff").grid(row=0, column=0, columnspan=2, sticky='w')
tk.Checkbutton(middle_frame, text="Include Numbers", variable=numbers_var, bg="#ffffff").grid(row=1, column=0, columnspan=2, sticky='w')
tk.Checkbutton(middle_frame, text="Include Symbols", variable=symbols_var, bg="#ffffff").grid(row=2, column=0, columnspan=2, sticky='w')
tk.Button(middle_frame, text="Generate Password", command=on_generate, bg="#4caf50", fg="#ffffff").grid(row=3, column=0, columnspan=2, pady=10)

# Bottom frame widgets
tk.Label(bottom_frame, text="Generated Password:", bg="#ffffff").grid(row=0, column=0, sticky='e')
tk.Entry(bottom_frame, textvariable=result_var, state='readonly').grid(row=0, column=1, padx=10, pady=5)
tk.Button(bottom_frame, text="Copy to Clipboard", command=copy_to_clipboard, bg="#2196f3", fg="#ffffff").grid(row=1, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
