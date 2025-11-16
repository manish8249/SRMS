import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkinter import *
import os

# Connect to SQLite3 database
con = sqlite3.connect(database="rms.db")
cur = con.cursor()

#----FUNCTIONS-----
def open_dashboard():
    os.system('python dashboard.py')

def open_report():
    os.system('python report.py')

    

#---LOGIN FUNCTION----
def login():
    username = entry_username.get()
    password = entry_password.get()
    user_type = combo_user_type.get()
    try:
        if user_type == "Admin":
            cur.execute('SELECT * FROM admin_login WHERE username=? AND password=?', (username, password))
            user = cur.fetchone()
            if user:
                messagebox.showinfo("Login Successful", "Welcome Admin!")
                win.destroy()  # Close the login window
                open_dashboard()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
        elif user_type == "Student":
            cur.execute('SELECT * FROM student_login WHERE username=? AND password=?', (username, password))
            user = cur.fetchone()
            if user:
                messagebox.showinfo("Login Successful", "Welcome Student!")
                win.destroy()  # Close the login window
                open_report()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
    except sqlite3.OperationalError as e:
        messagebox.showerror("Database Error", f"Error: {e}")


def go_to_register():
    win.destroy()  # Close the login window
    os.system('python register.py')  # Redirect to the registration page

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

combo_user_type = ttk.Combobox(center_frame, values=["Admin", "Student"], font=("Goudy old style", 15), width=20,justify=CENTER,state="readonly")
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

# Login Button
btn_login = Button(center_frame, text="Login", command=login, font=("Goudy old style", 15, "bold"), bg="#0078D7", fg="white", width=20,cursor="hand2")
btn_login.grid(row=3, column=0, columnspan=2, pady=20)

# Register Link
label_register = Label(center_frame, text="Don't have an account? Register here", fg="white", cursor="hand2", bg="#4e54c8", font=("Goudy old style", 12, "underline"))
label_register.grid(row=4, column=0, columnspan=2, pady=10)
label_register.bind("<Button-1>", lambda e: go_to_register())

win.mainloop()