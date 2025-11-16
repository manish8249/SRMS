from io import open_code
from tkinter import *
from PIL import Image,ImageTk
import os
import sqlite3
from tkinter import ttk,messagebox
win=Tk()

def open_course():
    os.system('python course.py')

def open_student():
    os.system('python student.py')

def open_result():
    os.system('python result.py')  

def open_change_password():
    os.system('python change_password.py')
    win.destroy()  


def logout_():
    win.destroy()
    os.system('python login.py')

def exit_():
    win.destroy()

def update_details():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        cur.execute("select * from course")
        cr=cur.fetchall()
        coursedetails.config(text=f"Total students\n[{str(len(cr))}]")

        cur.execute("select * from student")
        cr=cur.fetchall()
        studentdetails.config(text=f"Total course\n[{str(len(cr))}]")

        cur.execute("select * from result")
        cr=cur.fetchall()
        resultdetails.config(text=f"Total result\n[{str(len(cr))}]")

        coursedetails.after(200,update_details)   

    except Exception as ex:
        messagebox.showerror("Error", f"Error during ID reset: {str(ex)}")
    finally:
        con.close()
win.title("Student Result Managment System")

#---Set screen Size of the window----
width=win.winfo_screenwidth()
height=win.winfo_screenheight()
win.geometry(f"{width}x{height}")

#---bg image-----
bgimage=Image.open("images/image00.jpeg")
bgimage=bgimage.resize((7680,3402))
bgimage=ImageTk.PhotoImage(bgimage)
win.bg=Label(win,image=bgimage).place(x=0,y=0)
# win.config(bg="white")

#---ICON---
logo=Image.open("images/logo1.png")
logo=logo.resize((60,32))
logo=ImageTk.PhotoImage(logo) #Convert the image to a format Tkinter understands

#---TITLE---
win.head=Label(text="Student Result Managment System",compound=LEFT,image=logo, padx=10,font=("goudy old style",20,"bold"), bg="#033054", fg="white").place(relwidth=1,height=40)

#---MENU---
m_frame=LabelFrame(win,text="Menus",font=("Times new roam",8))
m_frame.place(x=10,y=60,width=1500,height=70)

#----BUTTONS IN DASHBOARD----

btn_crs=Button(m_frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=open_course)
btn_crs.place(x=20,y=5,width=200,height=40)

btn_student=Button(m_frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=open_student)
btn_student.place(x=240,y=5,width=200,height=40)

btn_result=Button(m_frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=open_result)
btn_result.place(x=460,y=5,width=200,height=40)

btn_change_password=Button(m_frame,text="Change Password",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=open_change_password)
btn_change_password.place(x=680,y=5,width=200,height=40)

btn_logout=Button(m_frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=logout_)
btn_logout.place(x=900,y=5,width=200,height=40)

btn_exit=Button(m_frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=exit_)
btn_exit.place(x=1120,y=5,width=200,height=40)

#---ADD THE DASHBOARD IMAGE----
dash_image=Image.open("images/7.jpg")
dash_image=dash_image.resize((714,260))
dash_image=ImageTk.PhotoImage(dash_image)
win.dashbg=Label(win,image=dash_image,bd=0).place(x=100,y=250)


#---Update details---
coursedetails=Label(win,font=("goudy old style",18,"bold"),bg="#24a0ed",fg="white",relief=RIDGE,bd=10)
coursedetails.place(x=950,y=250,width=300,height=80)
studentdetails=Label(win,text="Student \n[0]",font=("goudy old style",18,"bold"),bg="#f45900",fg="white",relief=RIDGE,bd=10)
studentdetails.place(x=950,y=350,width=300,height=80)
resultdetails=Label(win,text="Result\n [0]",font=("goudy old style",18,"bold"),bg="#767676",fg="white",relief=RIDGE,bd=10)
resultdetails.place(x=950,y=440,width=300,height=80)


#---Footer----
win.footer=Label(win,text="Student Result Management System\nFor any techinical issue contact : Computer Science(Group-3)",font=("Times new roam",10),bg="#8c7468",fg="white").pack(side=BOTTOM,fill=X)
update_details()


win.mainloop()