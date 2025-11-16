import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkinter import *
import os
import time



# Registration Page
def register():
    username = entry_username.get()
    password = entry_password.get()
    user_type = combo_user_type.get()
    try:
        with sqlite3.connect("rms.db", timeout=10) as con:
            con.execute("PRAGMA journal_mode=WAL;")  # Enable WAL mode for multiple access
            cur = con.cursor()
            if user_type == "Admin":
                cur.execute('INSERT INTO admin_login (username, password) VALUES (?, ?)', (username, password))
            elif user_type == "Student":
                cur.execute('INSERT INTO student_login (username, password) VALUES (?, ?)', (username, password))

            con.commit()

        messagebox.showinfo("Registration Successful", "You have been registered!")

    except sqlite3.OperationalError as e:
        messagebox.showerror("Database Error", f"Error: {e}")

    time.sleep(1)  # Small delay to ensure database is closed before reopening
    win.destroy()  # Close registration window
    os.system('python login.py')  # Redirect to login page
    
def go_to_login():
    win.destroy()  # Close the registration window
    os.system('python login.py')  # Redirect to the login page

# Main Window
win = Tk()
win.title("Student Result Management System")

#---Set screen Size of the window----
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry(f"{width}x{height}")

# Gradient Background
canvas = Canvas(win, width=width, height=height)
canvas.pack()
canvas.create_rectangle(0, 0, width, height, fill="#4e54c8", outline="")

# Frame to Center Widgets
center_frame = Frame(win, bg="#4e54c8")
center_frame.place(relx=0.5, rely=0.5, anchor="center")

# User Type Combobox
select_user_lbl = Label(center_frame, text="Select user:", font=("Goudy old style", 15, "bold"), bg="#4e54c8", fg="white")
select_user_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")

combo_user_type = ttk.Combobox(center_frame, values=["Admin", "Student"], font=("Goudy old style", 15), width=20,state="readonly",justify=CENTER)
combo_user_type.set("Admin")
combo_user_type.grid(row=0, column=1, padx=10, pady=10)

# Username Entry
label_username = Label(center_frame, text="Username:", bg="#4e54c8", fg="white", font=("Goudy old style", 15, "bold"))
label_username.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_username = Entry(center_frame, font=("Goudy old style", 15), width=22)
entry_username.grid(row=1, column=1, padx=10, pady=10)

# Password Entry
label_password = Label(center_frame, text="Password:", bg="#4e54c8", fg="white", font=("Goudy old style", 15, "bold"))
label_password.grid(row=2, column=0, padx=10, pady=10, sticky="w")

entry_password = Entry(center_frame, show="*", font=("Goudy old style", 15), width=22)
entry_password.grid(row=2, column=1, padx=10, pady=10)

# Register Button
btn_register = Button(center_frame, text="Register", command=register, font=("Goudy old style", 15, "bold"), bg="#0078D7", fg="white", width=20,cursor="hand2")
btn_register.grid(row=3, column=0, columnspan=2, pady=20)

# Login Link
label_login = Label(center_frame, text="Already have an account? Login here", fg="white", cursor="hand2", bg="#4e54c8", font=("Goudy old style", 12, "underline"))
label_login.grid(row=4, column=0, columnspan=2, pady=10)
label_login.bind("<Button-1>", lambda e: go_to_login())

win.mainloop()