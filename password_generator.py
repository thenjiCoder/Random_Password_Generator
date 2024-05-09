import random
import string
import tkinter as tk
from tkinter import messagebox

# Define a function to generate a password
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    # Concatenate character sets based on user input
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Raise an error if no character types are selected
    if not characters:
        raise ValueError("At least one character type should be selected.")

    # Generate password using random characters from the concatenated set
    return ''.join(random.choice(characters) for _ in range(length))

# Event handler for the "Generate Password" button
def generate_password_clicked():
    try:
        # Retrieve user input from entry fields and checkboxes
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()
        
        # Generate password based on user input
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        
        # Enable password display, clear previous content, insert new password, and disable display again
        password_display.config(state=tk.NORMAL)
        password_display.delete("1.0", tk.END)
        password_display.insert(tk.END, password)
        password_display.config(state=tk.DISABLED)
    except ValueError as ve:
        # Display error message if input is invalid
        messagebox.showerror("Error", ve)

# Create a tkinter window
root = tk.Tk()
root.title("Password Generator")

# Labels and Entry fields for user input
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Checkbuttons for including character types
letters_var = tk.BooleanVar(value=True)
letters_check = tk.Checkbutton(root, text="Include letters", variable=letters_var)
letters_check.grid(row=1, column=0, padx=10, pady=5, sticky="w")

numbers_var = tk.BooleanVar(value=True)
numbers_check = tk.Checkbutton(root, text="Include numbers", variable=numbers_var)
numbers_check.grid(row=2, column=0, padx=10, pady=5, sticky="w")

symbols_var = tk.BooleanVar(value=True)
symbols_check = tk.Checkbutton(root, text="Include symbols", variable=symbols_var)
symbols_check.grid(row=3, column=0, padx=10, pady=5, sticky="w")

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password_clicked)
generate_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Text widget to display generated password
password_display = tk.Text(root, height=3, width=30, state=tk.DISABLED)
password_display.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Run the tkinter event loop
root.mainloop()