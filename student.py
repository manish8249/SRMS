from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import sqlite3
from tkinter import ttk,messagebox
win=Tk()
win.config(bg="white")
win.geometry("1200x480+80+170")
win.title("Student Result Managment System")

#=====FUNCTIONS=======


#----ADD/SAVE BUTTON FUNCTION------
def add():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        if var_roll.get()=="":
            messagebox.showerror("Error","Roll No should be required ",parent=win)
        else:
            cur.execute("select * from Student where roll =?",(var_roll.get(),))
            row=cur.fetchone()
            if row != None:
                messagebox.showerror("Error", "Roll No is already present",parent=win)
            else:
                add_text=ent_addess.get("1.0", "end-1c")
                cur.execute("INSERT INTO student (roll, Name, Email,Gender,DOB,Contact, Addmission, Course,State,City,Pin,Address) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (
                    var_roll.get(),
                    var_name.get(),
                    var_email.get(),
                    var_gender.get(),
                    var_DOB.get(),
                    var_contact.get(),
                    var_a_date.get(),
                    var_coure.get(),
                    var_state.get(),
                    var_city.get(),
                    var_pin.get(),
                    add_text,
                    ))
                con.commit()
                messagebox.showinfo("Success","Student detials added successfully ",parent=win)
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
        if var_roll.get()=="":
            messagebox.showerror("Error","Roll no should be required ",parent=win)
        else:
            cur.execute("select * from student where roll =?",(var_roll.get(),))
            row=cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Select course from list",parent=win)
            else:
                add_text=ent_addess.get("1.0", "end-1c")
                cur.execute("update student set Name=?, Email=?,Gender=?,DOB=?,Contact=?, Addmission=?, Course=?,State=?,City=?,Pin=?,Address=? where roll=?", (
                    var_name.get(),
                    var_email.get(),
                    var_gender.get(),
                    var_DOB.get(),
                    var_contact.get(),
                    var_a_date.get(),
                    var_coure.get(),
                    var_state.get(),
                    var_city.get(),
                    var_pin.get(),
                    add_text,
                    var_roll.get(),
                    ))
                con.commit()
                messagebox.showinfo("Success","Student Details Update successfully ",parent=win)
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
        if var_roll.get()=="":
            messagebox.showerror("Error","Roll should be required ",parent=win)
        else:
            cur.execute("select * from student where roll =?",(var_roll.get(),))
            row=cur.fetchone()
            if row == None:
                messagebox.showerror("Error", "Select roll from list",parent=win)
            else:
                op=messagebox.askyesno("Confirm","Do you really want to delete", parent=win)
                if op==True:
                    cur.execute("delete from student where roll=?",(var_roll.get(),))
                    con.commit()
                    messagebox.showinfo("Delete","Student Record Deleted Successfully",parent=win)
                   
                    cur.execute("delete from result where roll=?",(var_roll.get(),))
                    con.commit()
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
            messagebox.showerror("Error", "Please enter a Roll No to search", parent=win)
        else:
            cur.execute("SELECT * from student where roll=?",(var_search.get(),))
            r=cur.fetchone()
            if r!=None:
                tree.delete(*tree.get_children())
                tree.insert("","end", values=r)
            else:
                messagebox.showerror("Error","No search result fonud")       
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to {str(ex)}")  
    finally:
        con.close()

#----CLEAR BUTTON FUNCTION------
def clear():
    show()
   
    var_name.set("")
    var_roll.set("")
    var_email.set("")
    var_gender.set("")
    var_DOB.set("")
    var_contact.set("")
    var_a_date.set("")
    var_coure.set("")
    var_state.set("")
    var_city.set("")
    var_pin.set("")
    ent_addess.delete('1.0',END)
    var_search.set("")
    ent_roll.config(state=NORMAL)

#----SHOW DATA  in frame function----
def show():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try:
        
        cur.execute("select * from student")
        rows=cur.fetchall()
        tree.delete(*tree.get_children())
        for row in rows:
            tree.insert('',END,values=row)
            
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to {str(ex)}")   
    finally:
        con.close() 

#---FETCH DATA FROM COURSE TO MENTION IN COURSE----
def fetch_course():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    try: 
        cur.execute("select Course_Name from course")
        rows=cur.fetchall()
        
        if len(rows)>0:
            for row in rows:
                course_list.append(row[0])
        # print(v)    
    except Exception as ex:
        messagebox.showerror("Error",f"Error due to {str(ex)}")   
    finally:
        con.close()

#----GET DATA FROM DB AND PUT ON ENTERY FIELDS-----
def get_data(ev):
    ent_roll.config(state='readonly')
    r=tree.focus()
    content=tree.item(r)
    row=content["values"]
    var_roll.set(row[0])
    var_name.set(row[1])
    var_email.set(row[2])
    var_gender.set(row[3])
    var_DOB.set(row[4])
    var_contact.set(row[5])
    var_a_date.set(row[6])
    var_coure.set(row[7])
    var_state.set(row[8])
    var_city.set(row[9])
    var_pin.set(row[10])
    ent_addess.delete('1.0',END)
    ent_addess.insert(END,row[11])    
    
#====END OF FUNCTIONS====


#----Head----
head=Label(win,text="Manage Student Details",font=("Goudy old style",20,"bold"),bg="#033054",fg="white").place(x=10,y=15,width=700,height=35)

#---Desciption----
#column-1
lbl_roll=Label(win,text="Roll No.",font=("Goudy old style",15,"bold"),bg="white").place(x=10,y=60)
lbl_name=Label(win,text="Name",font=("Goudy old style",15,"bold"),bg="white").place(x=10,y=100)
lbl_email=Label(win,text="Email ID",font=("Goudy old style",15,"bold"),bg="white").place(x=10,y=140)
lbl_gender=Label(win,text="Gender",font=("Goudy old style",15,"bold"),bg="white").place(x=10,y=180)
lbl_state=Label(win,text="State",font=("Goudy old style",15,"bold"),bg="white").place(x=10,y=220)
lbl_address=Label(win,text="Address",font=("Goudy old style",15,"bold"),bg="white").place(x=10,y=265)

#column-2
lbl_DOB=Label(win,text="D.O.B",font=("goudy old style",15,"bold"),bg="white").place(x=370,y=60)
lbl_contact=Label(win,text="Contact",font=("goudy old style",15,"bold"),bg="white").place(x=370,y=100)
lbl_addmission=Label(win,text="Addmission",font=("goudy old style",15,"bold"),bg="white").place(x=370,y=140)
lbl_course=Label(win,text="Course",font=("goudy old style",15,"bold"),bg="white").place(x=370,y=180)
lbl_city=Label(win,text="City",font=("goudy old style",15,"bold"),bg="white").place(x=310,y=220)
lbl_pin=Label(win,text="Pin",font=("goudy old style",15,"bold"),bg="white").place(x=500,y=220)
#---create variabel---
var_roll=StringVar()
var_name=StringVar()
var_email=StringVar()
var_search=StringVar()
var_gender=StringVar()
var_DOB=StringVar()
var_contact=StringVar()
var_coure=StringVar()
var_a_date=StringVar()
var_state=StringVar()
var_city=StringVar()
var_pin=StringVar()

#---create entery fields----
#column-1
ent_roll=Entry(win,textvariable=var_roll,font=("Goudy old style",15,"bold"),bg="light yellow")
ent_roll.place(x=150,y=60,width=200)
ent_name=Entry(win,textvariable=var_name,font=("Goudy old style",15,"bold"),bg="light yellow").place(x=150,y=100,width=200)
ent_email=Entry(win,textvariable=var_email,font=("Goudy old style",15,"bold"),bg="light yellow").place(x=150,y=140,width=200)
ent_gender=ttk.Combobox(win,textvariable=var_gender,font=("Goudy old style",15,"bold"),values=("Select","Male","Female","Other"),justify=CENTER,state="readonly")
ent_gender.place(x=150,y=180,width=200)
ent_gender.current(0)
ent_state=Entry(win,textvariable=var_state,font=("goudy old style",15,"bold"),bg="light yellow").place(x=150,y=220,width=150)
ent_addess=Text(win,font=("Goudy old style",15,"bold"),bg="light yellow")
ent_addess.place(x=150,y=265,width=530,height=100)
#column-2
course_list=[]
fetch_course()
ent_DOB=Entry(win,textvariable=var_DOB,font=("goudy old style",15,"bold"),bg="light yellow").place(x=490,y=60,width=200)
ent_contact=Entry(win,textvariable=var_contact,font=("goudy old style",15,"bold"),bg="light yellow").place(x=490,y=100,width=200)
ent_addmission=Entry(win,textvariable=var_a_date,font=("goudy old style",15,"bold"),bg="light yellow").place(x=490,y=140,width=200)

ent_course=ttk.Combobox(win,textvariable=var_coure,font=("Goudy old style",15,"bold"),values=course_list,justify=CENTER,state="readonly")
ent_course.place(x=490,y=180,width=200)
ent_course.set("Select")
ent_city=Entry(win,textvariable=var_city,font=("goudy old style",15,"bold"),bg="light yellow").place(x=380,y=220,width=100)
ent_pin=Entry(win,textvariable=var_pin,font=("goudy old style",15,"bold"),bg="light yellow").place(x=560,y=220,width=130)

#---Adding of search button and entery field-----
lbl_search=Label(win,text="Student Roll",font=("Goudy old style",15,"bold"),bg="white").place(x=735,y=15)
ent_search=Entry(win,textvariable=var_search,font=("Goudy old style",15,"bold"),bg="light yellow").place(x=865,y=15,width=150)
btn_search=Button(win,text="Search",font=("goudy old style",15,"bold"),bg="#03a9f4",fg="white",cursor="hand2",command=search)
btn_search.place(x=1025,y=15,width=110,height=28)

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
sd_frame=Frame(win,bd=2,relief=RIDGE)
sd_frame.place(x=720,y=55,width=470,height=340)
columns=("Roll","Name", "Email","Gender","DOB","Contact", "Addmission", "Course","State","City","Pin","Address")
x_scrollbar=ttk.Scrollbar(sd_frame,orient="horizontal")
y_scrollbar=ttk.Scrollbar(sd_frame,orient="vertical")
tree=ttk.Treeview(sd_frame,columns=columns,show="headings",xscrollcommand=x_scrollbar,yscrollcommand=y_scrollbar)

x_scrollbar.config(command=tree.xview)
y_scrollbar.config(command=tree.yview)

x_scrollbar.pack(side="bottom", fill="x")
y_scrollbar.pack(side="right", fill="y")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="center")

tree.pack(fill="both", expand=True)
tree.bind("<ButtonRelease-1>",get_data)
show()



win.mainloop()