from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
win=Tk()
win.config(bg="white")
win.geometry("1200x480+80+170")
win.title("Student Result Managment System")

 #=====FUNCTIONS====

def reset_course_id():
    con = sqlite3.connect(database="rms.db")
    cur = con.cursor()
    try:
        # Create a temporary table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS temp_course(
                Course_ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                Course_Name TEXT, 
                Duration TEXT, 
                Charges TEXT, 
                Description TEXT
            )
        """)
        # Copy existing data to the temporary table
        cur.execute("INSERT INTO temp_course (Course_Name, Duration, Charges, Description) SELECT Course_Name, Duration, Charges, Description FROM course")
        con.commit()
        
        # Drop the old table and rename the temporary one
        cur.execute("DROP TABLE course")
        cur.execute("ALTER TABLE temp_course RENAME TO course")
        con.commit()
    except Exception as ex:
        messagebox.showerror("Error", f"Error during ID reset: {str(ex)}")
    finally:
        con.close()



 #----ADD/SAVE BUTTON FUNCTION------
def add():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        if var_course.get()=="":
            messagebox.showerror("Error","course name should be required ",parent=win)
        else:
            cur.execute("select * from course where Course_name =?",(var_course.get(),))
            row=cur.fetchone()
            if row != None:
                messagebox.showerror("Error", "Course name is already present",parent=win)
            else:
                desc_text=ent_description.get("1.0", "end-1c")
                cur.execute("INSERT INTO course (Course_Name,Duration,Charges,Description) VALUES (?,?,?,?)", (
                    var_course.get(),
                    var_duration.get(),
                    var_charges.get(),
                    desc_text,
                    ))
                con.commit()
                reset_course_id()
                messagebox.showinfo("Success","Course added successfully ",parent=win)
                show()
                clear()
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to {str(ex)}")
    finally:
        con.close()
    

#----UPDATE BUTTON FUNCTION------
def update():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        if var_course.get()=="":
            messagebox.showerror("Error","course name should be required ",parent=win)
        else:
            cur.execute("select * from course where Course_name =?",(var_course.get(),))
            row=cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Select course from list",parent=win)
            else:
                desc_text=ent_description.get("1.0", "end-1c")
                cur.execute("update course set Duration=?,Charges=?,Description=? where Course_Name=?", (
                    var_duration.get(),
                    var_charges.get(),
                    desc_text,
                    var_course.get(),
                    ))
                con.commit()
                messagebox.showinfo("Success","Course Update successfully ",parent=win)
                show()
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to {str(ex)}")
    finally:
        con.close()    


 #----DELETE BUTTON FUNCTION------
def delete():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        if var_course.get()=="":
            messagebox.showerror("Error","course name should be required ",parent=win)
        else:
            cur.execute("select * from course where Course_name =?",(var_course.get(),))
            row=cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Select course from list",parent=win)
            else:
                op=messagebox.askyesno("Confirm","Do you really want to delete", parent=win)
                if op==True:
                    cur.execute("delete from course where course_name=?",(var_course.get(),))
                    con.commit()
                    messagebox.showinfo("Delete","Course Deleted Successfully",parent=win)
                    clear()
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to {str(ex)}")  
    finally:
        con.close()


#----SEARCH BUTTON FUNCTION------
def search():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        if var_search.get() == "":
            messagebox.showerror("Error", "Please enter a course name to search", parent=win)
        else:
            cur.execute("SELECT * from course where Course_name LIKE ?",(f"%{var_search.get()}%",))
            r=cur.fetchall()
            tree.delete(*tree.get_children())
            for row in r:
                 tree.insert("","end", values=row)
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to {str(ex)}")  
    finally:
        con.close()

#----CLEAR BUTTON FUNCTION------
def clear():
    show()
    var_course.set("")
    var_duration.set("")
    var_charges.set("")
    var_search.set("")
    ent_description.delete('1.0',END)
    ent_course.config(state='normal')



#----SHOW DATA  in frame function----
def show():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        
        cur.execute("select * from course")
        rows=cur.fetchall()
        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert('',END,values=row)
            
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to {str(ex)}")   
    finally:
        con.close()    



#----GET DATA FROM DB AND PUT ON ENTERY FIELDS-----
def get_data(ev):
    ent_course.config(state='readonly')
    r=tree.focus()
    content=tree.item(r)
    row=content["values"]
    var_course.set(row[1])
    var_duration.set(row[2])
    var_charges.set(row[3])
    ent_description.delete('1.0',END)
    ent_description.insert(END,row[4])    
    
#====END OF FUNCTIONS====


#----Head----
head=Label(win,text="Manage Course Details",font=("Goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=1180,height=35)

#---Entery fields desciption---
lbl_course=Label(win,text="Course Name",font=("Goudy old style",15,"bold"),bg="white").place(x=10,y=60)
lbl_duration=Label(win,text="Duration",font=("Goudy old style",15,"bold"),bg="white").place(x=10,y=100)
lbl_charges=Label(win,text="Charges",font=("Goudy old style",15,"bold"),bg="white").place(x=10,y=140)
lbl_description=Label(win,text="Description",font=("Goudy old style",15,"bold"),bg="white").place(x=10,y=180)

#---create variabel---
var_course=StringVar()
var_duration=StringVar()
var_charges=StringVar()
var_search=StringVar()

#---create entery fields----
ent_course=Entry(win,textvariable=var_course,font=("Goudy old style",15,"bold"),bg="light yellow")
ent_course.place(x=150,y=60,width=200)
ent_duration=Entry(win,textvariable=var_duration,font=("Goudy old style",15,"bold"),bg="light yellow").place(x=150,y=100,width=200)
ent_charges=Entry(win,textvariable=var_charges,font=("Goudy old style",15,"bold"),bg="light yellow").place(x=150,y=140,width=200)
ent_description=Text(win,font=("Goudy old style",15,"bold"),bg="light yellow")
ent_description.place(x=150,y=180,width=450,height=100)


#---Search button and entery field-----
lbl_search=Label(win,text="Course Name",font=("Goudy old style",15,"bold"),bg="white").place(x=735,y=60)
ent_search=Entry(win,textvariable=var_search,font=("Goudy old style",15,"bold"),bg="light yellow").place(x=865,y=60,width=150)
btn_search=Button(win,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=search)
btn_search.place(x=1025,y=60,width=110,height=28)

#---Adding buttons-----

btn_save=Button(win,text="Save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=add)
btn_save.place(x=150,y=400,width=110,height=40)

btn_Update=Button(win,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=update)
btn_Update.place(x=270,y=400,width=110,height=40)

btn_Delete=Button(win,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=delete)
btn_Delete.place(x=390,y=400,width=110,height=40)

btn_Clear=Button(win,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=clear)
btn_Clear.place(x=510,y=400,width=110,height=40)

#---create the table view---
co_frame=Frame(win,bd=2,relief=RIDGE)
co_frame.place(x=720,y=100,width=470,height=340)
columns=("Course ID","Course Name", "Duration","Charges","Description")
x_scrollbar=ttk.Scrollbar(co_frame,orient="horizontal")
y_scrollbar=ttk.Scrollbar(co_frame,orient="vertical")
tree=ttk.Treeview(co_frame,columns=columns,show="headings",xscrollcommand=x_scrollbar,yscrollcommand=y_scrollbar)

x_scrollbar.config(command=tree.xview)
y_scrollbar.config(command=tree.yview)

x_scrollbar.pack(side="bottom", fill="x")
y_scrollbar.pack(side="right", fill="y")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor="center")

tree.pack(fill="both", expand=True)
tree.bind("<ButtonRelease-1>",get_data)
show()

win.mainloop()