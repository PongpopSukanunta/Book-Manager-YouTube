from tkinter import *
from tkinter import messagebox
from db import Database


db = Database('Bookshelf.db')

def populate_list():
    books_list.delete(0, END)
    for row in db.fetch():
        books_list.insert(END, row)


def add_item():
    if book_text.get() == '' or author_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(book_text.get(), author_text.get())
    books_list.delete(0, END)
    books_list.insert(END, (book_text.get(), author_text.get()))
    clear_item()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = books_list.curselection()[0]
        selected_item = books_list.get(index)
        
        book_entry.delete(0, END)
        book_entry.insert(END, selected_item[1])

        author_entry.delete(0, END)
        author_entry.insert(END, selected_item[2])
    except IndexError:
        pass

def remove_item():
    db.remove(selected_item[0])
    clear_item()
    populate_list()


def update_item():
    db.update(selected_item[0],book_text.get(), author_text.get())
    populate_list()


def clear_item():
    book_entry.delete(0, END)
    author_entry.delete(0, END)



# create window object
app = Tk()

# Book
book_text = StringVar()
book_label = Label(app, text='Book Name', font=('bold',14), pady=20)
book_label.grid(row=0, column=0, sticky=W)
book_entry = Entry(app, textvariable=book_text,)
book_entry.grid(row=0, column=1)

# Author
author_text = StringVar()
author_label = Label(app, text='Author Name', font=('bold',14), pady=20)
author_label.grid(row=0, column=2, sticky=W)
author_entry = Entry(app, textvariable=author_text,)
author_entry.grid(row=0, column=3)

# Book List
books_list = Listbox(app, height=8, width=50, border=0)
books_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=10)

# Create scrokllbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

# Set scroll to lisbox
books_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=books_list.yview)

# Bind select
books_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add Book', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=10)

remove_btn = Button(app, text='Remove Book', width=12, command=remove_item)
remove_btn.grid(row=2, column=1, pady=10)

update_btn = Button(app, text='Update Book', width=12, command=update_item)
update_btn.grid(row=2, column=2, pady=10)

clear_btn = Button(app, text='Clear Book', width=12, command=clear_item)
clear_btn.grid(row=2, column=3, pady=10)


app.title('Book Manager')
app.geometry('700x350')

# Populate data
populate_list()

# Start program
app.mainloop()
