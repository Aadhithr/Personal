from tkinter import *
import backendhealth as Backend
from tkinter import ttk
#takes the functions from the other file and puts it in here


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])
    e5.delete(0, END)
    e5.insert(END, selected_tuple[5])
#view button
#gets the stuff from the database in the other file and displays in a list(built in tkinter )

def view_command():
    list1.delete(0, END)
    for row in Backend.view():
        list1.insert(END, row)

#serach button
# gets the search command from other file and displays whatever has the terms 
def search_command():
    list1.delete(0, END)
    for row in Backend.search(recordid_text.get(), insurance_text.get(), firstname_text.get(), lastname_text.get(), medicaldetails_text.get()):
        list1.insert(END, row)

#add button
# makes a new entry in the database(refer to code on that)

def add_command():
    Backend.insert(recordid_text.get(), insurance_text.get(), firstname_text.get(), lastname_text.get(), medicaldetails_text.get())
    list1.delete(0, END)
    list1.insert(END,(recordid_text.get(), insurance_text.get(), firstname_text.get(), lastname_text.get(), medicaldetails_text.get()))

def addtofile_command():
  f = open(firstname_text.get() + ".txt", "w")
  f.write(recordid_text.get() + " - " + insurance_text.get() + " - " + firstname_text.get() + " - " + lastname_text.get() + " - " + medicaldetails_text.get())
  f.close()
#delete
# deletes the selected thing

def delete_command():
    Backend.delete(selected_tuple[0])

#update
#lets u change the entries and updates the database

def update_command():     
  Backend.update(selected_tuple[0], recordid_text.get(), insurance_text.get(), firstname_text.get(), lastname_text.get(), medicaldetails_text.get())

#the rest is just display so liike the actual search buttons, entrys, text, etc


  




def nextpage_command():
 
  app = tkinterApp()
  app.mainloop()

window = Tk()
window.geometry("500x300")

window.wm_title("Medical Records")

l1 = Label(window, text="Record ID")
l1.grid(row=0, column=0)

l2 = Label(window, text="Insurance")
l2.grid(row=1, column=0)

l3 = Label(window, text="First Name")
l3.grid(row=2, column=0)

l4 = Label(window, text="Last Name")
l4.grid(row=3, column=0)

l5 = Label(window, text="Medical Details")
l5.grid(row=4, column=0)

recordid_text = StringVar()
e1 = Entry(window, textvariable=recordid_text)
e1.grid(row=0, column=1)

insurance_text = StringVar()
e2 = Entry(window, textvariable=insurance_text)
e2.grid(row=1, column=1)

firstname_text = StringVar()
e3 = Entry(window, textvariable=firstname_text)
e3.grid(row=2, column=1)

lastname_text = StringVar()
e4 = Entry(window, textvariable=lastname_text)
e4.grid(row=3, column=1)

medicaldetails_text = StringVar()
e5 = Entry(window, textvariable=medicaldetails_text)
e5.grid(row=4, column=1)

b1=Button(window,text='Add to File',command=addtofile_command)
b1.grid(row=4, column=2)


list1 = Listbox(window, height=6, width=45)
list1.grid(row=6, column=1, rowspan=4, columnspan=5)

sb1 = Scrollbar(window)
sb1.grid(row=6, column=6, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

bottom_frame = Frame(window)
bottom_frame.grid(row=18, columnspan=6)

b1=Button(bottom_frame,text='View',command=view_command)
b1.grid(row=18, column=0)

b2=Button(bottom_frame,text='Search',command=search_command)
b2.grid(row=18, column=1)

b3=Button(bottom_frame,text='Add',command=add_command)
b3.grid(row=18, column=2)

b4=Button(bottom_frame,text='Update',command=update_command)
b4.grid(row=18, column=3)

b5 = Button(bottom_frame, text="Delete", command=delete_command)
b5.grid(row=18, column=4)

b6 = Button(window, text="Close", command=window.destroy)
b6.grid(row=18, column=5)

b7 = Button(window, text="Next Page", command=nextpage_command)
b7.grid(row=18, column=6)

window.mainloop()