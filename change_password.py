import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from tkinter import *
import os

# Connect to SQLite3 database
con = sqlite3.connect(database="rms.db")
cur = con.cursor()

# Function to change password
def change_password():
    username = entry_username.get()
    old_password = entry_old_password.get()
    new_password = entry_new_password.get()
    user_type = combo_user_type.get()

    if user_type == "Admin":
        # Check if the old password is correct
        cur.execute('SELECT * FROM admin_login WHERE username=? AND password=?', (username, old_password))
        user = cur.fetchone()
        if user:
            # Update the password
            cur.execute('UPDATE admin_login SET password=? WHERE username=?', (new_password, username))
            con.commit()
            messagebox.showinfo("Success", "Password changed successfully!")
            win.destroy()  # Close the change password window
            os.system('python login.py')  # Redirect to the login page
        else:
            messagebox.showerror("Error", "Invalid username or old password")
    elif user_type == "Student":
        # Check if the old password is correct
        cur.execute('SELECT * FROM student_login WHERE username=? AND password=?', (username, old_password))
        user = cur.fetchone()
        if user:
            # Update the password
            cur.execute('UPDATE student_login SET password=? WHERE username=?', (new_password, username))
            con.commit()
            messagebox.showinfo("Success", "Password changed successfully!")
            win.destroy()  # Close the change password window
            os.system('python login.py')  # Redirect to the login page
        else:
            messagebox.showerror("Error", "Invalid username or old password")

# Function to go back to the login page
def go_to_login():
    win.destroy()  # Close the change password window
    os.system('python login.py')  # Redirect to the login page

# Main Window
win = Tk()
win.title("Change Password")

#---Set screen Size of the window----
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry(f"{width}x{height}")

# Gradient Background
canvas = Canvas(win, width=width, height=height)
canvas.pack()
canvas.create_rectangle(0, 0, width, height, fill="#c37562", outline="")

# Frame to Center Widgets
center_frame = Frame(win, bg="#c37562")
center_frame.place(relx=0.5, rely=0.5, anchor="center")

# User Type Combobox
select_user_lbl = Label(center_frame, text="Select user:", font=("Goudy old style", 15, "bold"), bg="#c37562", fg="white")
select_user_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="w")

combo_user_type = ttk.Combobox(center_frame, values=["Admin", "Student"], font=("Goudy old style", 15), width=20,state="readonly",justify=CENTER)
combo_user_type.set("Admin")
combo_user_type.grid(row=0, column=1, padx=10, pady=10)

# Username Entry
label_username = Label(center_frame, text="Username:", bg="#c37562", fg="white", font=("Goudy old style", 15, "bold"))
label_username.grid(row=1, column=0, padx=10, pady=10, sticky="w")

entry_username = Entry(center_frame, font=("Goudy old style", 15), width=22)
entry_username.grid(row=1, column=1, padx=10, pady=10)

# Old Password Entry
label_old_password = Label(center_frame, text="Old Password:", bg="#c37562", fg="white", font=("Goudy old style", 15, "bold"))
label_old_password.grid(row=2, column=0, padx=10, pady=10, sticky="w")

entry_old_password = Entry(center_frame, show="*", font=("Goudy old style", 15), width=22)
entry_old_password.grid(row=2, column=1, padx=10, pady=10)

# New Password Entry
label_new_password = Label(center_frame, text="New Password:", bg="#c37562", fg="white", font=("Goudy old style", 15, "bold"))
label_new_password.grid(row=3, column=0, padx=10, pady=10, sticky="w")

entry_new_password = Entry(center_frame, show="*", font=("Goudy old style", 15), width=22)
entry_new_password.grid(row=3, column=1, padx=10, pady=10)

# Change Password Button
btn_change_password = Button(center_frame, text="Change Password", command=change_password, font=("Goudy old style", 15, "bold"), bg="#0078D7", fg="white", width=20,cursor="hand2")
btn_change_password.grid(row=4, column=0, columnspan=2, pady=20)

# Login Link
label_login = Label(center_frame, text="Back to Login", fg="white", cursor="hand2", bg="#c37562", font=("Goudy old style", 12, "underline"))
label_login.grid(row=5, column=0, columnspan=2, pady=10)
label_login.bind("<Button-1>", lambda e: go_to_login())

win.mainloop()