import tkinter as tk
from tkinter import ttk
import itertools
import string

USER_PASSWORDS = {
    "ahmed": "apple",  
    "hager": "banana",  
    "layla": "cherry", 
    "youssef": "dragon" 
}

DICTIONARY = ["apple", "banana", "cherry", "dragon", "elephant", "fish", "grape"]

def dictionary_attack(username):
    correct_password = USER_PASSWORDS.get(username, "")
    for password in DICTIONARY:
        if password == correct_password:
            return True, password
    return False, None

def brute_force_attack(username):
    correct_password = USER_PASSWORDS.get(username, "")
    chars = string.ascii_letters 
    for length in range(1, 6): 
        for attempt in itertools.product(chars, repeat=length):
            attempt = ''.join(attempt)
            if attempt == correct_password:
                return True, attempt
    return False, None

def on_submit():
    username = username_var.get()
    result_text.set("Searching for password...")
    result_label.config(font=("Helvetica", 15)) 
    root.update() 

    success, password = dictionary_attack(username)
    
    if success:
        result_text.set(f"Password found: {password}")
        result_label.config(text=f"Password found: {password}", font=("Helvetica", 15))
        result_label.config(text=f"Password found: {password}", font=("Helvetica", 15, "bold"), wraplength=400)
    else:
        success, password = brute_force_attack(username)
        if success:
            result_text.set(f"Password found: {password}")
            result_label.config(text=f"Password found: {password}", font=("Helvetica", 15))
            result_label.config(text=f"Password found: {password}", font=("Helvetica", 15, "bold"), wraplength=400)
        else:
            result_text.set("Password not found")
            result_label.config(text="Password not found", font=("Helvetica", 15, "bold")) 

root = tk.Tk()
root.title("Secure Password Cracker")
root.configure(bg="#2C3E50") 

modern_font = ("Helvetica", 15)
title_font = ("Helvetica", 18, "bold")

frame = ttk.Frame(root, padding="20")
frame.grid(row=1, column=0, sticky="nsew")
frame.configure(style="Dark.TFrame")

style = ttk.Style()
style.theme_use("clam")
style.configure("Dark.TFrame", background="#2C3E50")
style.configure("TLabel", background="#2C3E50", foreground="#ECF0F1", font=modern_font)
style.configure("TButton", background="#3498DB", foreground="#ECF0F1", font=modern_font, padding=10)
style.configure("TCombobox", fieldbackground="#FFFFFF", foreground="#2C3E50", font=modern_font)

username_label = ttk.Label(frame, text="Select Username:")
username_label.grid(row=0, column=0, pady=10)
username_var = tk.StringVar()
username_dropdown = ttk.Combobox(frame, textvariable=username_var, width=27)
username_dropdown['values'] = ("ahmed", "hager", "layla", "youssef") 
username_dropdown.grid(row=0, column=1, pady=10)
username_dropdown.current(0)  

submit_button = ttk.Button(frame, text="Submit", command=on_submit)
submit_button.grid(row=1, column=0, columnspan=2, pady=20)

result_text = tk.StringVar()
result_text.set("Result will appear here")
result_label = ttk.Label(frame, textvariable=result_text, font=modern_font, background="#2C3E50", foreground="#ECF0F1")
result_label.grid(row=2, column=0, columnspan=2, pady=20, sticky="w")

root.mainloop()