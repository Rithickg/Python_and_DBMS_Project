from tkinter import *
from tkinter import PhotoImage, Image
import back


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[1])
    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])
    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])
    entry4.delete(0, END)
    entry4.insert(END, selected_tuple[4])
    entry5.delete(0, END)
    entry5.insert(END, selected_tuple[5])
    entry6.delete(0, END)
    entry6.insert(END, selected_tuple[6])


def view_command():
    list1.delete(0, END)
    for row in back.view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in back.search(
        name_text.get(),
        address_text.get(),
        phone_number_text.get(),
        roomtype_text.get(),
        noof_text.get(),
        amount_text.get(),
    ):
        list1.insert(END, row)


def add_command():
    back.insert(
        name_text.get(),
        address_text.get(),
        phone_number_text.get(),
        noof_text.get(),
        roomtype_text.get(),
        amount_text.get(),
    )
    list1.delete(0, END)
    list1.insert(
        END,
        (
            name_text.get(),
            address_text.get(),
            phone_number_text.get(),
            noof_text.get(),
            roomtype_text.get(),
            amount_text.get(),
        ),
    )


def delete_command():
    back.delete(selected_tuple[0])


def update_command():
    back.update(
        selected_tuple[0],
        name_text.get(),
        address_text.get(),
        phone_number_text.get(),
        roomtype_text.get(),
        noof_text.get(),
        amount_text.get(),
    )


window = Tk()
window.title("Hotel Reservation System")

bg = PhotoImage(file="C:\\Users\\AJAY\\Desktop\\Python_and_DBMS_Project\\img2.png")
label1 = Label(window, image=bg)
label1.place(x=0, y=0)

window.geometry("1000x600")


font_1 = ("Helvetica", 12, "bold", "italic")
font_2 = ("Arial", 10, "normal", "italic")
font_3 = ("Courier", 14, "normal", "roman")
font_4 = ("Times", 22, "bold", "roman")
font_5 = ("Comic Sans MS", 20, "bold", "roman")


label1 = Label(window, text="Hotel Reservation System")
label1.grid(row=2, column=1)
label1.configure(font=font_4)

label2 = Label(window, text="Name")
label2.grid(row=3, column=0)
label2.configure(font=font_1)

label3 = Label(window, text="Address")
label3.grid(row=4, column=0)
label3.configure(font=font_1)

label4 = Label(window, text="Phone Number")
label4.grid(row=5, column=0)
label4.configure(font=font_1)

label5 = Label(window, text="Number of days you want to Stay In")
label5.grid(row=6, column=0)
label5.configure(font=font_1)

label6 = Label(window, text="Room Type(Normal , King or Delux)")
label6.grid(row=7, column=0)
label6.configure(font=font_1)

label7 = Label(window, text="Total Amount")
label7.grid(row=8, column=0)
label7.configure(font=font_1)


name_text = StringVar()
entry1 = Entry(window, textvariable=name_text)
entry1.grid(row=3, column=1)
entry1.configure(font=font_1)

address_text = StringVar()
entry2 = Entry(window, textvariable=address_text)
entry2.grid(row=4, column=1)
entry2.configure(font=font_1)

phone_number_text = StringVar()
entry3 = Entry(window, textvariable=phone_number_text)
entry3.grid(row=5, column=1)
entry3.configure(font=font_1)

noof_text = StringVar()
entry4 = Entry(window, textvariable=noof_text)
entry4.grid(row=6, column=1)
entry4.configure(font=font_1)

roomtype_text = StringVar()
entry5 = Entry(window, textvariable=roomtype_text)
entry5.grid(row=7, column=1)
entry5.configure(font=font_1)

amount_text = StringVar()
entry6 = Entry(window, textvariable=amount_text)
entry6.grid(row=8, column=1)
entry6.configure(font=font_1)

list1 = Listbox(window, height=21, width=60)
list1.grid(row=4, column=3, rowspan=6, columnspan=2)

scrl = Scrollbar(window)
scrl.grid(row=4, column=2, sticky="ns", rowspan=6)


list1.configure(yscrollcommand=scrl.set)
scrl.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

b1 = Button(window, text="view all", width=12, command=view_command)
b1.grid(row=10, column=0)
b1.configure(font=font_1)

b2 = Button(window, text="add entry", width=12, command=add_command)
b2.grid(row=12, column=0)
b2.configure(font=font_1)

b3 = Button(window, text="delete entry", width=12, command=delete_command)
b3.grid(row=14, column=0)
b3.configure(font=font_1)

b4 = Button(window, text="search", width=12, command=search_command)
b4.grid(row=11, column=1)
b4.configure(font=font_1)

b5 = Button(window, text="update", width=12, command=update_command)
b5.grid(row=13, column=1)
b5.configure(font=font_1)


window.mainloop()
