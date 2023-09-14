from tkinter import *
import tkinter.messagebox as Messagebox
import mysql.connector

def checkIfExits(stu_roll):
    # Given student_roll to check

    mydb = mysql.connector.connect(auth_plugin='mysql_native_password',host="localhost", user="root", password="Itsme1283",database="stumgmt")
    mycursor = mydb.cursor()
    data = (stu_roll,)
    mycursor.execute("SELECT * FROM student WHERE stu = %s",data)
    result=mycursor.fetchone() 
    if result:
        return True   
    else:
        return False



def insert():
    stu=stu_entry.get()
    name=name_entry.get()
    contact=contact_entry.get() 
    
     
    print(stu,name,contact)
    
    if(stu=="" and name=="" and contact==""):
        Messagebox.showinfo("insert err","all field are required")
    elif(checkIfExits(stu)):
        Messagebox.showinfo("already exist ") 
    else:
           mydb =mysql.connector.connect(auth_plugin='mysql_native_password', host="localhost",user="root",password="Itsme1283",database="stumgmt")
           mycursor=mydb.cursor()
           sql="insert into student values(%s,%s,%s)"
           data=(stu,name,contact)
           mycursor.execute(sql,data)
           mydb.commit()
           stu_entry.delete(0,'end')
           name_entry.delete(0,'end')
           contact_entry.delete(0,'end')
           row=mycursor.rowcount
           show()
           Messagebox.showinfo("successful",f"{row}row is inserted")

# def delete():
#     if(stu_entry.get()==""):
#         Messagebox.showinfo("error","Insert the valid value")
#     else:
#         mydb=mysql.connector.connect(auth_plugin='mysql_native_password',host="localhost",user="root",password="Itsme1283",database="stumgmt")
#         mycursor=mydb.cursor()
#         mycursor.execute("delete from student where stu = "+stu_entry.get()+"")
#         mydb.commit()
#         stu_entry.delete(0,'end')
#         name_entry.delete(0,'end')
#         contact_entry.delete(0,'end')
#         row=mycursor.rowcount
#         show()
#         Messagebox.showinfo("successful",f"{row}Row deleted ")                               

def update():
    stu=stu_entry.get()
    name=name_entry.get()
    contact=contact_entry.get()
    
    if(stu==""or name==""or contact==""):
        Messagebox.showinfo("invalid entry")
    else:
        mydb=mysql.connector.connect(auth_plugin='mysql_native_password',host="localhost",user="root",password="Itsme1283",database="stumgmt")
        mycursor=mydb.cursor()
        mycursor.execute("update student set stu ='"+stu+"',name='"+name+"',contact='"+contact+"'")
        mydb.commit()
        stu_entry.delete(0,'end')
        name_entry.delete(0,'end')
        contact_entry.delete(0,'end')
        row=mycursor.rowcount
        show()
        Messagebox.showinfo("successful",f"{row}row updated")

def get():
    if(stu_entry.get()==""):
         Messagebox.showinfo("get status ",'enter stu for fetch result ')
    else:
       mydb = mysql.connector.connect(auth_plugin='mysql_native_password',host="localhost", user="root", password="Itsme1283",database="stumgmt")
       mycursor = mydb.cursor()
       mycursor.execute("select * from student where stu= '" + stu_entry.get() +"'")
       result=mycursor.fetchall() 
       for row in result:
            name_entry.insert(0,row[1])
            contact_entry.insert(0,row[2])
            
       mydb.commit()
       
       
       
def show():
       mydb = mysql.connector.connect(auth_plugin='mysql_native_password',host="localhost", user="root", password="Itsme1283",database="stumgmt")
       mycursor = mydb.cursor()
       mycursor.execute("select * from student")
       result=mycursor.fetchall() 
       list.delete(0,list.size())
       for row in result:
           insertdata=str(row[0])+'   '+row[1]+'    '+row[2]
           list.insert(list.size()+1,insertdata)
           
           
           
       
                  
root = Tk()

root.title("Login Page")
root.geometry("800x500")
root.maxsize(800,500)
root.minsize(800,500)

def showdetails():
    print(f"ID is: {stu_entry.get()} and Name is: {name_entry.get()}")

stu = Label(text="Student_ID")
stu.place(x=50, y=20)

stu_entry=Entry()
stu_entry.place(x=120, y=20)

name = Label(text="Name")
name.place(x=50, y=50)

name_entry = Entry()
name_entry.place(x=120, y=50)

contact=Label(text="contact")
contact.place(x=50,y=90)

contact_entry=Entry()
contact_entry.place(x=120,y=90)


submitbtn = Button(text="Submit", command=showdetails)
submitbtn.place(x=50, y=120)
insert = Button(root,text="Insert", font=('lucida',10,'bold'),bg="white", command=insert)
insert.place(x=20,y=140)

# delete = Button(root,text="Delete", font=('lucida',10,'bold'),bg="white",command=delete)
# delete.place(x=70,y=140)

update = Button(root,text="Update", font=('lucida',10,'bold'),bg="white",command=update)
update.place(x=130,y=140)

get = Button(root,text="Get", font=('lucida',10,'bold'),bg="white",command=get)
get.place(x=190,y=140)

list = Listbox(root)
list.place(x=300, y=30, width=230)
show()



root.mainloop()


