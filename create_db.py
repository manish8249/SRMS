import sqlite3

con=sqlite3.connect(database="rms.db")
cur=con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS course(Course_ID INTEGER PRIMARY KEY AUTOINCREMENT, Course_Name text,Duration text,Charges text,Description text )")
con.commit()

cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,Name text, Email text,Gender text,DOB text,Contact text, Addmission text, Course text,State text,City text,Pin text,Address text)")
con.commit()

cur.execute("CREATE TABLE IF NOT EXISTS result (rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text, course text, ob_mark text, full_mark text,per text)")
con.commit()

cur.execute("CREATE TABLE IF NOT EXISTS admin_login (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL,password TEXT NOT NULL)")
con.commit()

cur.execute("CREATE TABLE IF NOT EXISTS student_login (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL,password TEXT NOT NULL)")
con.commit()