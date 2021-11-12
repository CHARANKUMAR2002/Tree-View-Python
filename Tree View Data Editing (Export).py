import csv
from tkinter import *
from tkinter import ttk, filedialog, messagebox
import os

window = Tk()
window.geometry("850x400")
window.config(bg='black')


frame = Frame(window,bg =  'black')
frame.pack()

lbl_name = Label(frame, text="Name : ", font=("rosemary", 15,'italic'), bg='black', fg='white').grid(row=2, column=0, sticky=E)
name = Entry(frame, font=('arial', 10))
name.grid(row=2, column=1)
lbl_ad = Label(frame, text="Subject : ", font=("rosemary", 15,'italic'), bg='black', fg='white').grid(row=3, column=0, sticky=E)
address = Entry(frame, font=('arial', 10))
address.grid(row=3, column=1)
lbl_contact = Label(frame, text="Contact Number : ", font=("rosemary", 15,'italic'), bg='black', fg='white').grid(row=4, column=0, sticky=E)
contact = Entry(frame, font=('arial', 10))
contact.grid(row=4, column=1)

global sno
sno=1


def add():
    if name.get() !=" " and address.get() != " " and contact.get() != "":
        global sno
        tree.insert('', index='end', iid=sno, values=(sno, name.get(), address.get(), contact.get()))
        name.delete(0, END)
        address.delete(0, END)
        contact.delete(0, END)
        sno+=1
    else:
        messagebox.showerror('Error', "All Fields Should be Filled!")


def select():
    selected = tree.focus()
    values = tree.item(selected, 'values')
    name.insert(0, values[1])
    address.insert(0, values[2])
    contact.insert(0, values[3])
    return None

def update():
    if name.get() != " " and address.get() != " " and contact.get() != "":
        no = tree.focus()[0]
        selected = tree.focus()
        tree.item(selected, values=(no, name.get(), address.get(), contact.get()))
        name.delete(0, END)
        address.delete(0, END)
        contact.delete(0, END)
    else:
        messagebox.showerror('Error', "No Data to update!")


def delete():
    data = tree.selection()
    for datum in data:
        tree.delete(datum)


def clear_all():
    for data in tree.get_children():
        tree.delete(data)


def export_File():
    if len(tree.get_children()) == 0:
        messagebox.showerror('Export Error', 'No Data Available To Export')
        return False
    file = filedialog.asksaveasfilename(initialdir=os.getcwd(), title='Export file'
                                        , filetype=(("CSV File", "*.csv"), ("All Files", "*.*")))
    with open(file, mode='a', newline= '')as export_file:
        export = csv.writer(export_file, delimiter='\t')
        for i in tree.get_children():
            row = tree.item(i)['values']
            export.writerow(row)
    messagebox.showinfo('Export', 'Exported Successfully!')


frame1 = Frame(window, bg='black')
frame1.pack()
add = Button(frame1, text='Add Data', bg='green', fg='white', activebackground='green', activeforeground='white'
             , font=('rosemary', 10, 'bold'), command= add)
add.grid(row=1, column=1,pady=15, padx=10)
select = Button(frame1, text='Select Data', bg='blue', fg='white', activebackground='blue', activeforeground='white'
             , font=('rosemary', 10, 'bold'), command= select)
select.grid(row=1, column=2,pady=15, padx=10)
delete = Button(frame1, text='Delete Selected', bg='red', fg='white', activebackground='red', activeforeground='white'
             , font=('rosemary', 10, 'bold'), command=delete)
delete.grid(row=1, column=4,pady=15, padx=10)
clear = Button(frame1, text='Clear All', bg='#EF3912', fg='white', activebackground='#EF3912', activeforeground='white'
             , font=('rosemary', 10, 'bold'), command=clear_all)
clear.grid(row=1, column=5,pady=15, padx=10)
export_data = Button(frame1, text='Export Data', bg='olive', fg='white', activebackground='olive', activeforeground='white'
             , font=('rosemary', 10, 'bold'), command=export_File)
export_data.grid(row=1, column=6,pady=15, padx=15)
update_data = Button(frame1, text='Update', bg='olive', fg='white', activebackground='olive', activeforeground='white'
             , font=('rosemary', 10, 'bold'), command= update)
update_data.grid(row=1, column=3,pady=15, padx=10)


tree = ttk.Treeview(window)



tree['columns'] = ('S.NO', 'Name', 'Locality', 'Contact Number')
tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=10)
tree.column('#2', width=80)
tree.column('#3', width=80)
tree.column('#4', width=80)

tree.heading('#0', text='')
tree.heading('#1', text='S.NO')
tree.heading('#2', text='Name')
tree.heading('#3', text='Subject')
tree.heading('#4', text='Contact Number')


tree.pack(fill=X)

window.mainloop()
