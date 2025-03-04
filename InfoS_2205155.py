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
    for attempt in itertools.product(chars, repeat=5):  
        attempt = ''.join(attempt)
        if attempt == correct_password:
            return True, attempt
    return False, None

def on_submit():
    username = username_entry.get().strip()
    attack_type = attack_var.get()
    result_text.set("Searching for password...")
    root.update()
    
    if not username:
        result_text.set("Please enter a username.")
        return
    
    success, password = (dictionary_attack(username) if attack_type == "Dictionary Attack" else brute_force_attack(username))
    
    if success:
        result_text.set(f"Password found: {password}")
    else:
        result_text.set("Password not found")

root = tk.Tk()
root.title("Secure Password Cracker")
root.geometry("500x400")
root.configure(bg="#34495E")

modern_font = ("Helvetica", 14)
title_font = ("Helvetica", 20, "bold")

style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#34495E")
style.configure("TLabel", background="#34495E", foreground="#ECF0F1", font=modern_font)
style.configure("TButton", background="#1ABC9C", foreground="#FFFFFF", font=modern_font, padding=10)
style.configure("TEntry", fieldbackground="#FFFFFF", foreground="#2C3E50", font=modern_font)
style.configure("TCombobox", fieldbackground="#FFFFFF", foreground="#2C3E50", font=modern_font)

frame = ttk.Frame(root, padding="20")
frame.pack(pady=20)

title_label = ttk.Label(frame, text="Password Cracker Tool", font=title_font)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

username_label = ttk.Label(frame, text="Enter Username:")
username_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")
username_entry = ttk.Entry(frame, width=30)
username_entry.grid(row=1, column=1, pady=10, padx=10)

attack_var = tk.StringVar(value="Dictionary Attack")
attack_label = ttk.Label(frame, text="Select Attack Type:")
attack_label.grid(row=2, column=0, pady=10, padx=10, sticky="w")
attack_dropdown = ttk.Combobox(frame, textvariable=attack_var, values=["Dictionary Attack", "Brute Force Attack"], width=27)
attack_dropdown.grid(row=2, column=1, pady=10, padx=10)
attack_dropdown.current(0)

submit_button = ttk.Button(frame, text="Start Attack", command=on_submit)
submit_button.grid(row=3, column=0, columnspan=2, pady=20)

result_text = tk.StringVar()
result_text.set("Result will appear here")
result_label = ttk.Label(frame, textvariable=result_text, font=modern_font, background="#34495E", foreground="#ECF0F1", anchor="center")
result_label.grid(row=4, column=0, columnspan=2, pady=20)

root.mainloop()