from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import sqlite3
from tkinter import ttk,messagebox
win=Tk()
win.config(bg="white")
win.title("Student Result Managment System")



var_id=None

#FUNCTIONS

def search():
    global var_id
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        if var_search.get()=="":

            messagebox.showerror("Error","Please Enter the student Roll No",parent=win)
        else:
            cur.execute("SELECT * from result where roll=?",(var_search.get(),))
            r=cur.fetchone()
            if r!=None:
                var_id = r[0]
                roll.config(text=r[1])
                name.config(text=r[2])
                course.config(text=r[3])
                mark_ob.config(text=r[4])
                full_mark.config(text=r[5])
                per.config(text=r[6])
            else:
                messagebox.showerror("Error","No record Found for the Given Roll no")
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to {str(ex)}")  
    finally:
        con.close()


def clear():
        var_id=""
        roll.config(text="")
        name.config(text="")
        course.config(text="")
        mark_ob.config(text="")
        full_mark.config(text="")
        per.config(text="")
        var_search.set("")

#---Set screen Size of the window----
width=win.winfo_screenwidth()
height=win.winfo_screenheight()
win.geometry(f"{width}x{height}")

#----Head----
head=Label(win,text="View Student Result",font=("Goudy old style",25,"bold"),bg="orange",fg="black").place(y=15,width=width,height=35)


#---Varriable-----
var_search=StringVar()



#----ENTER ROLL NO DETAILS---
lbl_search=Label(win,text="Search By | Roll No.",font=("Goudy old style",20,"bold"),bg="white").place(x=450,y=100)
ent_search=Entry(win,textvariable=var_search,font=("goudy old style",18),bg="light yellow").place(x=710,y=100,width=150)
btn_search=Button(win,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=search)
btn_search.place(x=870,y=100,width=100,height=32)
btn_clear=Button(win,text="Clear",font=("goudy old style",15,"bold"),bg="gray",fg="white",cursor="hand2",command=clear)
btn_clear.place(x=990,y=100,width=100,height=32)


#----CREATION OF TABLE----
lbl_roll=Label(win,text="Roll No",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=350,y=230,width=150,height=50)
lbl_name=Label(win,text="Name",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=500,y=230,width=150,height=50)
lbl_course=Label(win,text="Course",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=650,y=230,width=150,height=50)
lbl_mark_ob=Label(win,text="Marks Obtained",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=800,y=230,width=150,height=50)
lbl_full_mark=Label(win,text="Full Mark",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=950,y=230,width=150,height=50)
lbl_per=Label(win,text="Percentage",font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE).place(x=1100,y=230,width=150,height=50)


roll=Label(win,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE,wraplength=140, anchor="center")
roll.place(x=350,y=280,width=150,height=50)
name=Label(win,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE,wraplength=140, anchor="center")
name.place(x=500,y=280,width=150,height=50)
course=Label(win,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE,wraplength=140, anchor="center")
course.place(x=650,y=280,width=150,height=50)
mark_ob=Label(win,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE,wraplength=140, anchor="center")
mark_ob.place(x=800,y=280,width=150,height=50)
full_mark=Label(win,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE,wraplength=140, anchor="center")
full_mark.place(x=950,y=280,width=150,height=50)
per=Label(win,font=("goudy old style",15,"bold"),bg="white",bd=2,relief=GROOVE,wraplength=140, anchor="center")
per.place(x=1100,y=280,width=150,height=50)






win.mainloop()