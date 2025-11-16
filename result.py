from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
win=Tk()
win.config(bg="white")
win.geometry("1200x480+80+170")
win.title("Student Result Managment System")

#===function====
def fetch_rollno():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try: 
        cur.execute("select roll from student")
        rows=cur.fetchall()
        
        if len(rows)>0:
            for row in rows:
                var_roll_list.append(row[0]) 
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to {str(ex)}")   
    finally:
        con.close()


#----SEARCH BUTTON FUNCTION------
def search():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        if var_roll.get()=="":
            messagebox.showerror("Error","Roll no should be required ",parent=win)
        else:
            cur.execute("select name,course from student where roll =?",(var_roll.get(),))
            row=cur.fetchone()
            var_name.set(row[0])
            var_course.set(row[1]) 
            cur.execute("select ob_mark,full_mark from result where roll =?",(var_roll.get(),))
            row1=cur.fetchone()
            if row1==None:
                pass
            else:
                var_marks.set(row1[0])
                var_full_marks.set(row1[1])   
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to {str(ex)}")
    finally:
        con.close()

def reset_rid():
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()
    try:
        # Create a temporary table
        cur.execute("""
                CREATE TABLE IF NOT EXISTS temp_result(
                    rid INTEGER PRIMARY KEY AUTOINCREMENT,
                    roll text,
                    name text,
                    course text,
                    ob_mark text,
                    full_mark text,
                    per text
            )
        """)
        # Copy existing data to the temporary table
        cur.execute("INSERT INTO temp_result (roll,name,course,ob_mark,full_mark,per) SELECT roll,name,course,ob_mark,full_mark,per FROM result")
        con.commit()
        
        # Drop the old table and rename the temporary one
        cur.execute("DROP TABLE result")
        cur.execute("ALTER TABLE temp_result RENAME TO result")
        con.commit()
    except Exception as ex:
        messagebox.showerror("Error", f"Error during ID reset: {str(ex)}")
    finally:
        con.close()

# ----SUBMIT BUTTON FUNCTION----
def submit():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        if var_name.get()=="":
                messagebox.showerror("Error","First search student record",parent=win)
        else: 
            cur.execute("select * from result where roll=? and course=?",(var_roll.get(),var_course.get(),))
            row=cur.fetchone()
            if row != None:
                messagebox.showerror("Error", "Result is already present",parent=win)
            else:
                per=(int(var_marks.get())*100)/int(var_full_marks.get()) #calculate the percentage of the student
                cur.execute("INSERT INTO result (roll,name,course,ob_mark,full_mark,per) VALUES (?,?,?,?,?,?)", (
                var_roll.get(),
                var_name.get(),
                var_course.get(),
                var_marks.get(),
                var_full_marks.get(),
                str(per)
                ))
                con.commit()   
                reset_rid() 
                messagebox.showinfo("Success","Result added successfully ",parent=win)
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to {str(ex)}")
    finally:
        con.close()                     


#----CLEAR BUTTON FUNCTION------
def clear():
    var_roll.set("")
    var_name.set("")
    var_course.set("") 
    var_marks.set("")
    var_full_marks.set("")
    

#----DELETE BUTTON FUNCTION------
def delete():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try: 
        if var_roll.get() == "":
            messagebox.showerror("Error","Search student Result first",parent=win)
        else:
            cur.execute("select * from result where roll =?",(var_roll.get(),))
            row=cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "No result found",parent=win)
            else:
                op=messagebox.askyesno("Confirm","Do you really want to delete", parent=win)
                if op==True:
                    cur.execute("delete from result where roll=?",(var_roll.get(),))
                    con.commit()
                    messagebox.showinfo("Delete","Result Deleted Successfully",parent=win)
                    clear()
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to {str(ex)}")  
    finally:
        con.close()


#----Head----
head=Label(win,text="Add Student Result Details",font=("Goudy old style",20,"bold"),bg="orange",fg="#262626").place(x=10,y=15,width=1180,height=50)

#----Varibales---
var_name=StringVar()
var_course=StringVar()
var_marks=StringVar()
var_full_marks=StringVar()
var_roll_list=[]
fetch_rollno()
var_roll=StringVar()


#----label defined----
txt_student=Label(win,text="Select student",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=100)
txt_name=Label(win,text="Name",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=160)
txt_course=Label(win,text="Course",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=220)
txt_mark=Label(win,text="Mark obtained",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=280)
txt_fullmark=Label(win,text="Full Mark",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=340)


ent_student_roll=ttk.Combobox(win,textvariable=var_roll,font=("Goudy old style",15,"bold"),values=var_roll_list,justify=CENTER,state="readonly")
ent_student_roll.place(x=280,y=100,width=200)
ent_student_roll.set("Select")

btn_search=Button(win,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=search)
btn_search.place(x=500,y=100,width=100,height=28)


ent_name=Entry(win,textvariable=var_name,font=("Goudy old style",20,"bold"),bg="light yellow",state='readonly').place(x=280,y=160,width=320)
ent_course=Entry(win,textvariable=var_course,font=("Goudy old style",20,"bold"),bg="light yellow",state='readonly').place(x=280,y=220,width=320)
ent_marks=Entry(win,textvariable=var_marks,font=("Goudy old style",20,"bold"),bg="light yellow").place(x=280,y=280,width=320)
ent_full_marks=Entry(win,textvariable=var_full_marks,font=("Goudy old style",20,"bold"),bg="light yellow").place(x=280,y=340,width=320)

#---BUTTON DELEAT---
btn_add=Button(win,text="Submit",font=("times new roam",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=submit).place(x=170,y=420,width=120,height=35)
btn_clear=Button(win,text="Clear",font=("times new roam",15),bg="#959595",activebackground="#959595",cursor="hand2",command=clear).place(x=430,y=420,width=120,height=35)
btn_delete=Button(win,text="Delete",font=("goudy old style",15,"bold"),bg="red",fg="white",cursor="hand2",command=delete).place(x=300,y=420,width=120,height=35)

#---image----
dash_image=Image.open("images/Result.png")
dash_image=dash_image.resize((500,300))
dash_image=ImageTk.PhotoImage(dash_image)
win.dashbg=Label(win,image=dash_image,bd=0).place(x=650,y=100)





win.mainloop()