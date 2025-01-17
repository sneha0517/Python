import tkinter as tk
from tkinter import messagebox
from password_generator import generate_password  # Import the function from your other script

def on_generate_password():
    """Handles the password generation based on GUI input."""
    try:
        # Get inputs from the GUI
        length = int(entry_length.get())
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        use_uppercase = var_uppercase.get()
        use_digits = var_digits.get()
        use_symbols = var_symbols.get()

        # Generate the password using the imported function
        password = generate_password(
            length=length,
            use_uppercase=use_uppercase,
            use_digits=use_digits,
            use_symbols=use_symbols
        )
        result.set(password)  # Update the result field

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def copy_to_clipboard():
    """Copies the generated password to the clipboard."""
    gui.clipboard_clear()
    gui.clipboard_append(result.get())
    gui.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create the GUI window
gui = tk.Tk()
gui.title("Random Password Generator")
gui.geometry("400x300")
gui.resizable(False, False)

# Input field for password length
tk.Label(gui, text="Password Length:").pack(pady=10)
entry_length = tk.Entry(gui, width=10)
entry_length.pack()

# Checkboxes for password options
var_uppercase = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(gui, text="Include Uppercase Letters", variable=var_uppercase).pack()
tk.Checkbutton(gui, text="Include Digits", variable=var_digits).pack()
tk.Checkbutton(gui, text="Include Symbols", variable=var_symbols).pack()

# Generate button
tk.Button(gui, text="Generate Password", command=on_generate_password).pack(pady=10)

# Output field for the generated password
result = tk.StringVar()
tk.Entry(gui, textvariable=result, state="readonly", width=30).pack(pady=10)

# Copy to clipboard button
tk.Button(gui, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)

# Run the GUI event loop
gui.mainloop()