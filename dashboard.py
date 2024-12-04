from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import start_page
import sqlite3

# connecting to the database file
conn = sqlite3.connect("database.db")
cur = conn.cursor()

background_color = "#6cc3d7"
second_background_color = "#e9f2f6"
third_color = "#324556"


# function for deleting book
def delete_book_func():
    # for creating a new window
    delete_book_window = Toplevel()

    delete_book_window.geometry("600x250")
    delete_book_window.title("Delete Book")
    delete_book_window.config(background=background_color)

    # window resizing
    delete_book_window.resizable(NO,NO)

    # creating a frame
    delete_book_window_frame = Frame(delete_book_window,background=background_color)
    delete_book_window_frame.place(relheight=1,relwidth=1)

    frame3 = Frame(delete_book_window_frame,background=background_color)
    frame3.pack(pady=[20,0])
    delete_book_book_title = Label(frame3,text="Book Title: ",background=background_color,font="Verdana 20 bold")
    delete_book_book_title.grid(row=0,column=0)
    delete_book_book_title_entry = Entry(frame3,font="Verdana 15 bold",highlightbackground="grey80")
    delete_book_book_title_entry.grid(row=0,column=1,padx=[20,0])

    frame2 = Frame(delete_book_window_frame,background=background_color)
    frame2.pack()
    delete_book_book_isbn = Label(frame2,text="Book ISBN: ",background=background_color,font="Verdana 20 bold")
    delete_book_book_isbn.grid(row=0,column=0)
    delete_book_book_isbn_entry = Entry(frame2,font="Verdana 15 bold",highlightbackground="grey80")
    delete_book_book_isbn_entry.grid(row=0,column=1,padx=[15,0])

    frame3 = Frame(delete_book_window_frame,background=background_color)
    frame3.pack()
    delete_book_book_author = Label(frame3,text="Book Author: ",background=background_color,font="Verdana 20 bold")
    delete_book_book_author.grid(row=0,column=0)
    delete_book_book_author_entry = Entry(frame3,font="Verdana 15 bold",highlightbackground="grey80")
    delete_book_book_author_entry.grid(row=0,column=1)

    # function for Deletin  the book from the database
    def delete_book_com():
        # getting the book data from the entry widgets
        book_isbn_fdb = delete_book_book_isbn_entry.get()

        # deleting the book data into the database
        cur.execute(f"DELETE from book_data WHERE book_isbn LIKE '{book_isbn_fdb}'")
        conn.commit()

        for i in book_records_treeview.get_children():
            book_records_treeview.delete(i)

        insert_data_book_records_treeview()
        
        # exiting the window
        delete_book_window.destroy()

    delete_book_delete_button = Button(delete_book_window_frame,command=delete_book_com,text="Delete",background=background_color,font="Verdana 20 bold")
    delete_book_delete_button.pack(ipadx=25,ipady=5,pady=30)

# function for reserved books
def reserved_book_func():

    # for creating a new window
    reserved_book_window = Toplevel()

    reserved_book_window.geometry("700x600")
    reserved_book_window.title("Reserved Books")
    reserved_book_window.config(background=background_color)

    # window resize no
    reserved_book_window.resizable(NO,NO)

    # creating a frame
    reserved_book_window_frame = Frame(reserved_book_window,background=background_color)
    reserved_book_window_frame.place(relheight=1,relwidth=1)

    # heading 
    Label(reserved_book_window_frame,text="Reserved Books",font="Verdana 25 bold",background=background_color).pack(pady=10)

    # making it global so we can update it
    global reserved_books_tree_view

    frame_scroll = Frame(reserved_book_window_frame,background=background_color)
    frame_scroll.pack()

    # tree view for reserved books
    reserved_books_tree_view = ttk.Treeview(frame_scroll,height=17,columns=("user_rollno_col","book_title_col","book_isbn_col","book_author_col"))

    # giving treeview heading its name
    reserved_books_tree_view.heading("#0",text="Name")
    reserved_books_tree_view.heading("user_rollno_col",text="RollNo")
    reserved_books_tree_view.heading("book_title_col",text="Title")
    reserved_books_tree_view.heading("book_isbn_col",text="ISBN")
    reserved_books_tree_view.heading("book_author_col",text="Author")

    # showing data from the database in the tree veiw of reserved books
    insert_data_reserved_book_treeview()

    # setting columns width
    reserved_books_tree_view.column(column="#0",width=120)
    reserved_books_tree_view.column(column="user_rollno_col",width=120)
    reserved_books_tree_view.column(column="book_title_col",width=120)
    reserved_books_tree_view.column(column="book_isbn_col",width=120)
    reserved_books_tree_view.column(column="book_author_col",width=120)

    reserved_books_tree_view.pack(side=LEFT)

    scroll_reserved_treeview = Scrollbar(frame_scroll)
    scroll_reserved_treeview.pack(side=RIGHT,fill=Y)
    scroll_reserved_treeview.config(command=reserved_books_tree_view.yview)
    reserved_books_tree_view.config(yscrollcommand=scroll_reserved_treeview.set)

    # heading for search
    Label(reserved_book_window_frame,text="Search Reserved Books",font="Verdana 25 bold",background=background_color).pack(pady=10)

    # frames for placing buttons
    frame1btn = Frame(reserved_book_window_frame,background=background_color)
    frame1btn.pack()
    frame2btn = Frame(reserved_book_window_frame,background=background_color)
    frame2btn.pack()

    # functions for search filters buttons

    # function for fillter search by name
    def by_name_button_com():
        global by_name_search_window_frame

        # for creating a new window
        by_name_search_window = Toplevel()

        by_name_search_window.geometry("700x300")
        by_name_search_window.title("By Name Search Books")
        by_name_search_window.config(background=background_color)

        # window resize no
        by_name_search_window.resizable(NO,NO)

        # creating a frame
        by_name_search_window_frame = Frame(by_name_search_window,background=background_color)
        by_name_search_window_frame.place(relheight=1,relwidth=1)

        # function for search in database
        def by_name_com():
            # making it global for updating 
            global by_name_search_tree_view

            frame_scroll = Frame(by_name_search_window_frame,background=background_color)
            frame_scroll.pack()
            
            # tree view for reserved books
            by_name_search_tree_view = ttk.Treeview(frame_scroll,columns=("user_rollno_col","book_title_col","book_isbn_col","book_author_col"))

            # giving treeview heading its name
            by_name_search_tree_view.heading("#0",text="Name")
            by_name_search_tree_view.heading("user_rollno_col",text="RollNo")
            by_name_search_tree_view.heading("book_title_col",text="Title")
            by_name_search_tree_view.heading("book_isbn_col",text="ISBN")
            by_name_search_tree_view.heading("book_author_col",text="Author")

            # setting columns width
            by_name_search_tree_view.column(column="#0",width=120)
            by_name_search_tree_view.column(column="user_rollno_col",width=120)
            by_name_search_tree_view.column(column="book_title_col",width=120)
            by_name_search_tree_view.column(column="book_isbn_col",width=120)
            by_name_search_tree_view.column(column="book_author_col",width=120)

            # getting the data from the entry for search
            search_data = by_name_entry.get()

            # getting the data from the database
            user_name = []
            user_rollno = []
            book_title = []
            book_isbn = []
            book_author = []

            if len(search_data) >= 1 :
                cur.execute(f"SELECT * FROM reserved_book_data WHERE user_name LIKE '%{search_data}%'")
                search_by_name_dbf = cur.fetchall()
                for item in search_by_name_dbf:
                    user_name.append(item[0])
                    user_rollno.append(item[1])
                    book_title.append(item[2])
                    book_isbn.append(item[3])
                    book_author.append(item[4])

                # inserting data in treeview
                for limit in range(len(book_title)):
                    by_name_search_tree_view.insert("",END,text=user_name[limit],values=[user_rollno[limit],book_title[limit],book_isbn[limit],book_author[limit]])

            by_name_search_tree_view.pack(side=LEFT)

            scroll_byname_treeview = Scrollbar(frame_scroll)
            scroll_byname_treeview.pack(side=RIGHT,fill=Y)
            scroll_byname_treeview.config(command=by_name_search_tree_view.yview)
            by_name_search_tree_view.config(yscrollcommand=scroll_byname_treeview.set)
            
        

        # frame for label and entry
        f1 = Frame(by_name_search_window_frame,background=background_color)
        f1.pack(pady=5)

        global by_name_entry

        # label and entry for search input
        by_name_label = Label(f1,text="By Name Search:",font="Verdana 10 bold",background=background_color)
        by_name_label.pack(side=LEFT,padx=10)
        by_name_entry = Entry(f1,font="Verdana 10 bold")
        by_name_entry.pack(side=LEFT,padx=5)
        by_name_search_btn = Button(f1,text="Search",command=by_name_com,relief=RAISED,background=second_background_color,foreground=third_color,activebackground="grey60",font="Verdana 10 bold")
        by_name_search_btn.pack(side=LEFT,padx=5)
        
    # function for fillter search by roll no
    def by_rollno_button_com():
       
        global by_rollno_search_window_frame

        # for creating a new window
        by_rollno_search_window = Toplevel()

        by_rollno_search_window.geometry("700x300")
        by_rollno_search_window.title("BY Roll No Search Books")
        by_rollno_search_window.config(background=background_color)

        # window resize no
        by_rollno_search_window.resizable(NO,NO)

        # creating a frame
        by_rollno_search_window_frame = Frame(by_rollno_search_window,background=background_color)
        by_rollno_search_window_frame.place(relheight=1,relwidth=1)

        # function for search in database
        def by_rollno_com():
            # making it global for updating 
            global by_rollno_search_tree_view

            frame_scroll = Frame(by_rollno_search_window_frame,background=background_color)
            frame_scroll.pack()
            
            # tree view for reserved books
            by_rollno_search_tree_view = ttk.Treeview(frame_scroll,columns=("user_rollno_col","book_title_col","book_isbn_col","book_author_col"))

            # giving treeview heading its name
            by_rollno_search_tree_view.heading("#0",text="Name")
            by_rollno_search_tree_view.heading("user_rollno_col",text="RollNo")
            by_rollno_search_tree_view.heading("book_title_col",text="Title")
            by_rollno_search_tree_view.heading("book_isbn_col",text="ISBN")
            by_rollno_search_tree_view.heading("book_author_col",text="Author")

            # setting columns width
            by_rollno_search_tree_view.column(column="#0",width=120)
            by_rollno_search_tree_view.column(column="user_rollno_col",width=120)
            by_rollno_search_tree_view.column(column="book_title_col",width=120)
            by_rollno_search_tree_view.column(column="book_isbn_col",width=120)
            by_rollno_search_tree_view.column(column="book_author_col",width=120)

            # getting the data from the entry for search
            search_data = by_rollno_entry.get()

            # getting the data from the database
            user_name = []
            user_rollno = []
            book_title = []
            book_isbn = []
            book_author = []

            if len(search_data) >= 1 :
                cur.execute(f"SELECT * FROM reserved_book_data WHERE user_roll_no LIKE '%{search_data}%'")
                search_by_rollno_dbf = cur.fetchall()
                for item in search_by_rollno_dbf:
                    user_name.append(item[0])
                    user_rollno.append(item[1])
                    book_title.append(item[2])
                    book_isbn.append(item[3])
                    book_author.append(item[4])

                # inserting data in treeview
                for limit in range(len(book_title)):
                    by_rollno_search_tree_view.insert("",END,text=user_name[limit],values=[user_rollno[limit],book_title[limit],book_isbn[limit],book_author[limit]])

            by_rollno_search_tree_view.pack(side=LEFT)

            scroll_byrollno_treeview = Scrollbar(frame_scroll)
            scroll_byrollno_treeview.pack(side=RIGHT,fill=Y)
            scroll_byrollno_treeview.config(command=by_rollno_search_tree_view.yview)
            by_rollno_search_tree_view.config(yscrollcommand=scroll_byrollno_treeview.set)

        # frame for label and entry
        f1 = Frame(by_rollno_search_window_frame,background=background_color)
        f1.pack(pady=5)

        global by_rollno_entry

        # label and entry for search input
        by_rollno_label = Label(f1,text="By ROll No Search:",font="Verdana 10 bold",background=background_color)
        by_rollno_label.pack(side=LEFT,padx=10)
        by_rollno_entry = Entry(f1,font="Verdana 10 bold")
        by_rollno_entry.pack(side=LEFT,padx=5)
        by_rollno_search_btn = Button(f1,text="Search",command=by_rollno_com,relief=RAISED,background=second_background_color,foreground=third_color,activebackground="grey60",font="Verdana 10 bold")
        by_rollno_search_btn.pack(side=LEFT,padx=5)

    # function for fillter search by title no
    def by_booktitle_button_com():
        global by_title_search_window_frame

        # for creating a new window
        by_title_search_window = Toplevel()

        by_title_search_window.geometry("700x300")
        by_title_search_window.title("By Title Search Books")
        by_title_search_window.config(background=background_color)

        # window resize no
        by_title_search_window.resizable(NO,NO)

        # creating a frame
        by_title_search_window_frame = Frame(by_title_search_window,background=background_color)
        by_title_search_window_frame.place(relheight=1,relwidth=1)

        # function for search in database
        def by_title_com():
            # making it global for updating 
            global by_title_search_tree_view

            frame_scroll = Frame(by_title_search_window_frame,background=background_color)
            frame_scroll.pack()
            
            # tree view for reserved books
            by_title_search_tree_view = ttk.Treeview(frame_scroll,columns=("user_rollno_col","book_title_col","book_isbn_col","book_author_col"))

            # giving treeview heading its name
            by_title_search_tree_view.heading("#0",text="Name")
            by_title_search_tree_view.heading("user_rollno_col",text="RollNo")
            by_title_search_tree_view.heading("book_title_col",text="Title")
            by_title_search_tree_view.heading("book_isbn_col",text="ISBN")
            by_title_search_tree_view.heading("book_author_col",text="Author")

            # setting columns width
            by_title_search_tree_view.column(column="#0",width=120)
            by_title_search_tree_view.column(column="user_rollno_col",width=120)
            by_title_search_tree_view.column(column="book_title_col",width=120)
            by_title_search_tree_view.column(column="book_isbn_col",width=120)
            by_title_search_tree_view.column(column="book_author_col",width=120)

            # getting the data from the entry for search
            search_data = by_title_entry.get()

            # getting the data from the database
            user_name = []
            user_rollno = []
            book_title = []
            book_isbn = []
            book_author = []

            if len(search_data) >= 1 :
                cur.execute(f"SELECT * FROM reserved_book_data WHERE book_title LIKE '%{search_data}%'")
                search_by_title_dbf = cur.fetchall()
                for item in search_by_title_dbf:
                    user_name.append(item[0])
                    user_rollno.append(item[1])
                    book_title.append(item[2])
                    book_isbn.append(item[3])
                    book_author.append(item[4])

                # inserting data in treeview
                for limit in range(len(book_title)):
                    by_title_search_tree_view.insert("",END,text=user_name[limit],values=[user_rollno[limit],book_title[limit],book_isbn[limit],book_author[limit]])

            by_title_search_tree_view.pack(side=LEFT)

            scroll_bytitle_treeview = Scrollbar(frame_scroll)
            scroll_bytitle_treeview.pack(side=RIGHT,fill=Y)
            scroll_bytitle_treeview.config(command=by_title_search_tree_view.yview)
            by_title_search_tree_view.config(yscrollcommand=scroll_bytitle_treeview.set)

        # frame for label and entry
        f1 = Frame(by_title_search_window_frame,background=background_color)
        f1.pack(pady=5)

        global by_title_entry

        # label and entry for search input
        by_title_label = Label(f1,text="By Title Search:",font="Verdana 10 bold",background=background_color)
        by_title_label.pack(side=LEFT,padx=10)
        by_title_entry = Entry(f1,font="Verdana 10 bold")
        by_title_entry.pack(side=LEFT,padx=5)
        by_title_search_btn = Button(f1,text="Search",command=by_title_com,relief=RAISED,background=second_background_color,foreground=third_color,activebackground="grey60",font="Verdana 10 bold")
        by_title_search_btn.pack(side=LEFT,padx=5)

    # function for fillter search by ISBN no
    def by_bookisbn_button_com():
        
        global by_isbn_search_window_frame

        # for creating a new window
        by_isbn_search_window = Toplevel()

        by_isbn_search_window.geometry("700x300")
        by_isbn_search_window.title("By ISBN Search Books")
        by_isbn_search_window.config(background=background_color)

        # window resize no
        by_isbn_search_window.resizable(NO,NO)

        # creating a frame
        by_isbn_search_window_frame = Frame(by_isbn_search_window,background=background_color)
        by_isbn_search_window_frame.place(relheight=1,relwidth=1)

        # function for search in database
        def by_isbn_com():
            # making it global for updating 
            global by_isbn_search_tree_view

            frame_scroll = Frame(by_isbn_search_window_frame,background=background_color)
            frame_scroll.pack()

            
            # tree view for reserved books
            by_isbn_search_tree_view = ttk.Treeview(frame_scroll,columns=("user_rollno_col","book_title_col","book_isbn_col","book_author_col"))

            # giving treeview heading its name
            by_isbn_search_tree_view.heading("#0",text="Name")
            by_isbn_search_tree_view.heading("user_rollno_col",text="RollNo")
            by_isbn_search_tree_view.heading("book_title_col",text="Title")
            by_isbn_search_tree_view.heading("book_isbn_col",text="ISBN")
            by_isbn_search_tree_view.heading("book_author_col",text="Author")

            # setting columns width
            by_isbn_search_tree_view.column(column="#0",width=120)
            by_isbn_search_tree_view.column(column="user_rollno_col",width=120)
            by_isbn_search_tree_view.column(column="book_title_col",width=120)
            by_isbn_search_tree_view.column(column="book_isbn_col",width=120)
            by_isbn_search_tree_view.column(column="book_author_col",width=120)

            # getting the data from the entry for search
            search_data = by_isbn_entry.get()

            # getting the data from the database
            user_name = []
            user_rollno = []
            book_title = []
            book_isbn = []
            book_author = []

            if len(search_data) >= 1 :
                cur.execute(f"SELECT * FROM reserved_book_data WHERE book_isbn LIKE '{search_data}%'")
                search_by_isbn_dbf = cur.fetchall()
                for item in search_by_isbn_dbf:
                    user_name.append(item[0])
                    user_rollno.append(item[1])
                    book_title.append(item[2])
                    book_isbn.append(item[3])
                    book_author.append(item[4])

                # inserting data in treeview
                for limit in range(len(book_title)):
                    by_isbn_search_tree_view.insert("",END,text=user_name[limit],values=[user_rollno[limit],book_title[limit],book_isbn[limit],book_author[limit]])

            by_isbn_search_tree_view.pack(side=LEFT)

            scroll_byisbn_treeview = Scrollbar(frame_scroll)
            scroll_byisbn_treeview.pack(side=RIGHT,fill=Y)
            scroll_byisbn_treeview.config(command=by_isbn_search_tree_view.yview)
            by_isbn_search_tree_view.config(yscrollcommand=scroll_byisbn_treeview.set)
            
        

        # frame for label and entry
        f1 = Frame(by_isbn_search_window_frame,background=background_color)
        f1.pack(pady=5)

        global by_isbn_entry

        # label and entry for search input
        by_isbn_label = Label(f1,text="By Title Search:",font="Verdana 10 bold",background=background_color)
        by_isbn_label.pack(side=LEFT,padx=10)
        by_isbn_entry = Entry(f1,font="Verdana 10 bold")
        by_isbn_entry.pack(side=LEFT,padx=5)
        by_isbn_search_btn = Button(f1,text="Search",command=by_isbn_com,relief=RAISED,background=second_background_color,foreground=third_color,activebackground="grey60",font="Verdana 10 bold")
        by_isbn_search_btn.pack(side=LEFT,padx=5)

    # function for fillter search by Author no
    def by_bookauthor_button_com():
        
        global by_author_search_window_frame

        # for creating a new window
        by_author_search_window = Toplevel()

        by_author_search_window.geometry("700x300")
        by_author_search_window.title("By Author Search Books")
        by_author_search_window.config(background=background_color)

        # window resize no
        by_author_search_window.resizable(NO,NO)

        # creating a frame
        by_author_search_window_frame = Frame(by_author_search_window,background=background_color)
        by_author_search_window_frame.place(relheight=1,relwidth=1)

        # function for search in database
        def by_author_com():
            # making it global for updating 
            global by_author_search_tree_view

            frame_scroll = Frame(by_author_search_window_frame,background=background_color)
            frame_scroll.pack()
            
            # tree view for reserved books
            by_author_search_tree_view = ttk.Treeview(frame_scroll,columns=("user_rollno_col","book_title_col","book_isbn_col","book_author_col"))

            # giving treeview heading its name
            by_author_search_tree_view.heading("#0",text="Name")
            by_author_search_tree_view.heading("user_rollno_col",text="RollNo")
            by_author_search_tree_view.heading("book_title_col",text="Title")
            by_author_search_tree_view.heading("book_isbn_col",text="ISBN")
            by_author_search_tree_view.heading("book_author_col",text="Author")

            # setting columns width
            by_author_search_tree_view.column(column="#0",width=120)
            by_author_search_tree_view.column(column="user_rollno_col",width=120)
            by_author_search_tree_view.column(column="book_title_col",width=120)
            by_author_search_tree_view.column(column="book_isbn_col",width=120)
            by_author_search_tree_view.column(column="book_author_col",width=120)

            # getting the data from the entry for search
            search_data = by_author_entry.get()

            # getting the data from the database
            user_name = []
            user_rollno = []
            book_title = []
            book_isbn = []
            book_author = []

            if len(search_data) >= 1 :
                cur.execute(f"SELECT * FROM reserved_book_data WHERE book_author LIKE '%{search_data}%'")
                search_by_author_dbf = cur.fetchall()
                for item in search_by_author_dbf:
                    user_name.append(item[0])
                    user_rollno.append(item[1])
                    book_title.append(item[2])
                    book_isbn.append(item[3])
                    book_author.append(item[4])

                # inserting data in treeview
                for limit in range(len(book_title)):
                    by_author_search_tree_view.insert("",END,text=user_name[limit],values=[user_rollno[limit],book_title[limit],book_isbn[limit],book_author[limit]])

            by_author_search_tree_view.pack(side=LEFT)

            scroll_byauthor_treeview = Scrollbar(frame_scroll)
            scroll_byauthor_treeview.pack(side=RIGHT,fill=Y)
            scroll_byauthor_treeview.config(command=by_author_search_tree_view.yview)
            by_author_search_tree_view.config(yscrollcommand=scroll_byauthor_treeview.set)

        # frame for label and entry
        f1 = Frame(by_author_search_window_frame,background=background_color)
        f1.pack(pady=5)

        global by_author_entry

        # label and entry for search input
        by_author_label = Label(f1,text="By Title Search:",font="Verdana 10 bold",background=background_color)
        by_author_label.pack(side=LEFT,padx=10)
        by_author_entry = Entry(f1,font="Verdana 10 bold")
        by_author_entry.pack(side=LEFT,padx=5)
        by_author_search_btn = Button(f1,text="Search",command=by_author_com,relief=RAISED,background=second_background_color,foreground=third_color,activebackground="grey60",font="Verdana 10 bold")
        by_author_search_btn.pack(side=LEFT,padx=5)

    # button for search filters    
    by_name_button = Button(frame1btn,text="By Name Search",command=by_name_button_com,relief=RAISED,background=second_background_color,foreground=third_color,activebackground="grey60",font="Verdana 12 bold")
    by_name_button.pack(side=LEFT,padx=5,pady=5)
    by_rollno_button = Button(frame1btn,text="By Roll No Search",command=by_rollno_button_com,relief=RAISED,background=second_background_color,foreground=third_color,activebackground="grey60",font="Verdana 12 bold")
    by_rollno_button.pack(side=LEFT,padx=5,pady=5)
    by_booktitle_button = Button(frame1btn,text="By Book Title Search",command=by_booktitle_button_com,relief=RAISED,background=second_background_color,foreground=third_color,activebackground="grey60",font="Verdana 12 bold")
    by_booktitle_button.pack(side=LEFT,padx=5,pady=5)
    by_bookisbn_button = Button(frame2btn,text="By Book ISBN Search",command=by_bookisbn_button_com,relief=RAISED,background=second_background_color,foreground=third_color,activebackground="grey60",font="Verdana 12 bold")
    by_bookisbn_button.pack(side=LEFT,padx=5,pady=5)
    by_bookauthor_button = Button(frame2btn,text="By Book Author Search",command=by_bookauthor_button_com,relief=RAISED,background=second_background_color,foreground=third_color,activebackground="grey60",font="Verdana 12 bold")
    by_bookauthor_button.pack(padx=5,pady=5)

# function for return book
def return_book_func():
    # for creating a new window
    return_book_window = Toplevel()

    return_book_window.geometry("700x320")
    return_book_window.title("Issue Book")
    return_book_window.config(background=background_color)

    # window resize no
    return_book_window.resizable(NO,NO)

    # creating a frame
    return_book_window_frame = Frame(return_book_window,background=background_color)
    return_book_window_frame.place(relheight=1,relwidth=1)

    frame1 = Frame(return_book_window_frame,background=background_color)
    frame1.pack(pady=[20,0])
    return_book_user_name = Label(frame1,text="User Name: ",background=background_color,font="Verdana 20 bold")
    return_book_user_name.grid(row=0,column=0)
    return_book_user_name_entry = Entry(frame1,font="Verdana 15 bold",highlightbackground="grey80")
    return_book_user_name_entry.grid(row=0,column=1,padx=[20,0])

    frame2 = Frame(return_book_window_frame,background=background_color)
    frame2.pack()
    return_book_user_rollno = Label(frame2,text="User Rollno: ",background=background_color,font="Verdana 20 bold")
    return_book_user_rollno.grid(row=0,column=0)
    return_book_user_rollno_entry = Entry(frame2,font="Verdana 15 bold",highlightbackground="grey80")
    return_book_user_rollno_entry.grid(row=0,column=1,padx=[20,0])

    frame3 = Frame(return_book_window_frame,background=background_color)
    frame3.pack()
    return_book_book_title = Label(frame3,text="Book Title: ",background=background_color,font="Verdana 20 bold")
    return_book_book_title.grid(row=0,column=0)
    return_book_book_title_entry = Entry(frame3,font="Verdana 15 bold",highlightbackground="grey80")
    return_book_book_title_entry.grid(row=0,column=1,padx=[20,0])

    frame4 = Frame(return_book_window_frame,background=background_color)
    frame4.pack()
    return_book_book_isbn = Label(frame4,text="Book ISBN: ",background=background_color,font="Verdana 20 bold")
    return_book_book_isbn.grid(row=0,column=0)
    return_book_book_isbn_entry = Entry(frame4,font="Verdana 15 bold",highlightbackground="grey80")
    return_book_book_isbn_entry.grid(row=0,column=1,padx=[15,0])

    frame5 = Frame(return_book_window_frame,background=background_color)
    frame5.pack()
    return_book_book_author = Label(frame5,text="Book Author: ",background=background_color,font="Verdana 20 bold")
    return_book_book_author.grid(row=0,column=0)
    return_book_book_author_entry = Entry(frame5,font="Verdana 15 bold",highlightbackground="grey80")
    return_book_book_author_entry.grid(row=0,column=1)

    # function for returning  the book implementing in the database
    def return_book_com():
        # getting the book data from the entry widgets
        book_isbn_fdb = return_book_book_isbn_entry.get()

        # inserting the book data into the database
        if len(book_isbn_fdb) >=1 :
            cur.execute(f"DELETE from reserved_book_data WHERE book_isbn LIKE '{book_isbn_fdb}'")
            conn.commit()
        
        # exiting the window
        return_book_window.destroy()

    return_book_return_button = Button(return_book_window_frame,command=return_book_com,text="Return",background=background_color,font="Verdana 20 bold")
    return_book_return_button.pack(ipadx=25,ipady=5,pady=[30,0])

# function for issue book
def issue_book_func():
    # for creating a new window
    issue_book_window = Toplevel()

    issue_book_window.geometry("700x320")
    issue_book_window.title("Issue Book")
    issue_book_window.config(background=background_color)

    # window resize no
    issue_book_window.resizable(NO,NO)

    # creating a frame
    issue_book_window_frame = Frame(issue_book_window,background=background_color)
    issue_book_window_frame.place(relheight=1,relwidth=1)

    frame1 = Frame(issue_book_window_frame,background=background_color)
    frame1.pack(pady=[20,0])
    issue_book_user_name = Label(frame1,text="User Name: ",background=background_color,font="Verdana 20 bold")
    issue_book_user_name.grid(row=0,column=0)
    issue_book_user_name_entry = Entry(frame1,font="Verdana 15 bold",highlightbackground="grey80")
    issue_book_user_name_entry.grid(row=0,column=1,padx=[20,0])

    frame2 = Frame(issue_book_window_frame,background=background_color)
    frame2.pack()
    issue_book_user_rollno = Label(frame2,text="User Rollno: ",background=background_color,font="Verdana 20 bold")
    issue_book_user_rollno.grid(row=0,column=0)
    issue_book_user_rollno_entry = Entry(frame2,font="Verdana 15 bold",highlightbackground="grey80")
    issue_book_user_rollno_entry.grid(row=0,column=1,padx=[20,0])

    frame3 = Frame(issue_book_window_frame,background=background_color)
    frame3.pack()
    issue_book_book_title = Label(frame3,text="Book Title: ",background=background_color,font="Verdana 20 bold")
    issue_book_book_title.grid(row=0,column=0)
    issue_book_book_title_entry = Entry(frame3,font="Verdana 15 bold",highlightbackground="grey80")
    issue_book_book_title_entry.grid(row=0,column=1,padx=[20,0])

    frame4 = Frame(issue_book_window_frame,background=background_color)
    frame4.pack()
    issue_book_book_isbn = Label(frame4,text="Book ISBN: ",background=background_color,font="Verdana 20 bold")
    issue_book_book_isbn.grid(row=0,column=0)
    issue_book_book_isbn_entry = Entry(frame4,font="Verdana 15 bold",highlightbackground="grey80")
    issue_book_book_isbn_entry.grid(row=0,column=1,padx=[15,0])

    frame5 = Frame(issue_book_window_frame,background=background_color)
    frame5.pack()
    issue_book_book_author = Label(frame5,text="Book Author: ",background=background_color,font="Verdana 20 bold")
    issue_book_book_author.grid(row=0,column=0)
    issue_book_book_author_entry = Entry(frame5,font="Verdana 15 bold",highlightbackground="grey80")
    issue_book_book_author_entry.grid(row=0,column=1)

    # function for adding the book in the database
    def issue_book_com():
        # getting the book data from the entry widgets
        book_user_name_fdb = issue_book_user_name_entry.get()
        book_user_rollno_fdb = issue_book_user_rollno_entry.get()
        book_title_fdb = issue_book_book_title_entry.get()
        book_isbn_fdb = issue_book_book_isbn_entry.get()
        book_author_fdb = issue_book_book_author_entry.get()

        # inserting the book data into the database
        if len(book_title_fdb) >=1 and len(book_isbn_fdb) >=1 and len(book_author_fdb) >=1:
            cur.execute("INSERT INTO reserved_book_data VALUES(?,?,?,?,?)",(book_user_name_fdb,book_user_rollno_fdb,book_title_fdb,book_isbn_fdb,book_author_fdb))
            conn.commit()
        
        # exiting the window
        issue_book_window.destroy()

    issue_book_issue_button = Button(issue_book_window_frame,command=issue_book_com,text="Issue",background=background_color,font="Verdana 20 bold")
    issue_book_issue_button.pack(ipadx=25,ipady=5,pady=[30,0])

# function for add book
def add_book_func():
    # for creating a new window
    add_book_window = Toplevel()

    add_book_window.geometry("600x250")
    add_book_window.title("Add Book")
    add_book_window.config(background=background_color)

    # window resizing
    add_book_window.resizable(NO,NO)

    # creating a frame
    add_book_window_frame = Frame(add_book_window,background=background_color)
    add_book_window_frame.place(relheight=1,relwidth=1)

    frame3 = Frame(add_book_window_frame,background=background_color)
    frame3.pack(pady=[20,0])
    add_book_book_title = Label(frame3,text="Book Title: ",background=background_color,font="Verdana 20 bold")
    add_book_book_title.grid(row=0,column=0)
    add_book_book_title_entry = Entry(frame3,font="Verdana 15 bold",highlightbackground="grey80")
    add_book_book_title_entry.grid(row=0,column=1,padx=[20,0])

    frame2 = Frame(add_book_window_frame,background=background_color)
    frame2.pack()
    add_book_book_isbn = Label(frame2,text="Book ISBN: ",background=background_color,font="Verdana 20 bold")
    add_book_book_isbn.grid(row=0,column=0)
    add_book_book_isbn_entry = Entry(frame2,font="Verdana 15 bold",highlightbackground="grey80")
    add_book_book_isbn_entry.grid(row=0,column=1,padx=[15,0])

    frame3 = Frame(add_book_window_frame,background=background_color)
    frame3.pack()
    add_book_book_author = Label(frame3,text="Book Author: ",background=background_color,font="Verdana 20 bold")
    add_book_book_author.grid(row=0,column=0)
    add_book_book_author_entry = Entry(frame3,font="Verdana 15 bold",highlightbackground="grey80")
    add_book_book_author_entry.grid(row=0,column=1)


    # function for adding the book in the database
    def add_book_com():
        # getting the book data from the entry widgets
        book_title_fdb = add_book_book_title_entry.get()
        book_isbn_fdb = add_book_book_isbn_entry.get()
        book_author_fdb = add_book_book_author_entry.get()

        # inserting the book data into the database
        if len(book_title_fdb) >=1 and len(book_isbn_fdb) >=1 and len(book_author_fdb) >=1:
            cur.execute("INSERT INTO book_data VALUES(?,?,?)",(book_title_fdb,book_isbn_fdb,book_author_fdb))
            conn.commit()

            # calling the function to inset the new book
            # insert_data_book_records_treeview()

            # calling the function to inset the new book
            book_records_treeview.insert("",END,text=book_title_fdb,values=[book_isbn_fdb,book_author_fdb])
        
        # exiting the window
        add_book_window.destroy()


    add_book_add_button = Button(add_book_window_frame,command=add_book_com,text="Add",background=background_color,font="Verdana 20 bold")
    add_book_add_button.pack(ipadx=25,ipady=5,pady=30)

def about():
    message_ = "for later"
    mb.showinfo(title="About",message=message_)

# for removing frame
def clear_frame(frame):
   for widgets in frame.winfo_children():
      widgets.destroy()

def help():
    message_ = "for later"
    mb.showinfo(title="Help",message=message_)

def update_tree_view():
        book_records_treeview.update()

# inserting data in tree view
def insert_data_reserved_book_treeview():
    # getting the data of books from the database
    user_name = []
    user_rollno = []
    book_title = []
    book_isbn = []
    book_author = []

    cur.execute("SELECT * FROM reserved_book_data")
    data_from_reserved_book_data = cur.fetchall()
    for item in data_from_reserved_book_data:
        user_name.append(item[0])
        user_rollno.append(item[1])
        book_title.append(item[2])
        book_isbn.append(item[3])
        book_author.append(item[4])
    
    # inserting data in treeview
    for limit in range(len(book_title)):
        reserved_books_tree_view.insert("",END,text=user_name[limit],values=[user_rollno[limit],book_title[limit],book_isbn[limit],book_author[limit]])

# inserting data in tree view
def insert_data_book_records_treeview():
    # getting the data of books from the database
    book_title = []
    book_isbn = []
    book_author = []

    cur.execute("SELECT * FROM book_data")
    data_from_book_data = cur.fetchall()
    for item in data_from_book_data:
        book_title.append(item[0])
        book_isbn.append(item[1])
        book_author.append(item[2])
    
    # inserting data in treeview
    for limit in range(len(book_title)):
        book_records_treeview.insert("",END,text=book_title[limit],values=[book_isbn[limit],book_author[limit]])


def dashboard(root):

    # creating menu bar
    menu_bar = Menu(root,tearoff=0)

    # navigation menu in menu bar
    navigation_menu = Menu(menu_bar,tearoff=0,foreground=third_color,background=second_background_color)
    # navigation_menu.add_command(label="Dashboard",command=lambda:dashboard.dashboard(root),activebackground=second_background_color)
    navigation_menu.add_command(label="Exit",command=root.destroy,activebackground=background_color,foreground=third_color,background=second_background_color)
    menu_bar.add_cascade(label="Navigation",menu=navigation_menu,activebackground=background_color,foreground=third_color,background=second_background_color)

    about_menu = Menu(menu_bar,tearoff=0,activebackground=background_color,foreground=third_color,background=second_background_color)
    about_menu.add_command(label="About",command=about,activebackground=background_color,foreground=third_color,background=second_background_color)
    about_menu.add_command(label="Help",command=help,activebackground=background_color,foreground=third_color,background=second_background_color)
    menu_bar.add_cascade(label="About",menu=about_menu,activebackground=background_color,foreground=third_color,background=second_background_color)

    # dashboard frame
    dashboard_frame = Frame(root,background=background_color)
    dashboard_frame.place(relheight=1,relwidth=1)

    # left frame for buttons
    left_frame = Frame(dashboard_frame,background=background_color)
    left_frame.grid(row=0,column=0,sticky=NSEW)

    # add book button
    add_book_button = Button(left_frame,text="Add Book",command=add_book_func,relief=RAISED,background=second_background_color,foreground=third_color,activebackground="grey60",font="Verdana 15 bold")
    add_book_button.pack(padx=50,pady=[40,15])

    # issue book button
    issue_book_button = Button(left_frame,text="Issue Book",command=issue_book_func,relief=RAISED,background=second_background_color,foreground=third_color,activebackground="grey60",font="Verdana 15 bold")
    issue_book_button.pack(padx=50,pady=15)

    # return book button
    return_book_button = Button(left_frame,text="Return Book",command=return_book_func,relief=RAISED,background=second_background_color,foreground=third_color,activebackground="grey60",font="Verdana 15 bold")
    return_book_button.pack(padx=50,pady=15)
    
    # reserved book button
    reserved_book_button = Button(left_frame,text="Reserved Books",command=reserved_book_func,relief=RAISED,background=second_background_color,foreground=third_color,activebackground="grey60",font="Verdana 15 bold")
    reserved_book_button.pack(padx=50,pady=15)

    # delete book button
    delete_book_button = Button(left_frame,text="Delete Book",command=delete_book_func,relief=RAISED,background=second_background_color,foreground=third_color,activebackground="grey60",font="Verdana 15 bold")
    delete_book_button.pack(padx=50,pady=15)

    # logout button
    logout_button = Button(left_frame,text="Logout",command=lambda:start_page.start_page(root),relief=RAISED,background=second_background_color,foreground=third_color,activebackground="grey60",font="Verdana 15 bold")
    logout_button.pack(padx=50,pady=15)

    # right frame for tree view for data
    right_frame = Frame(dashboard_frame,background=background_color)
    right_frame.grid(row=0,column=1,sticky=NSEW)

    # creating another frame inside right frame
    inside_right_frame = Frame(right_frame,background=background_color)
    inside_right_frame.pack(pady=10)

    # making treeview global so i can update it
    global book_records_treeview

    # Tree view for book records
    book_records_treeview = ttk.Treeview(inside_right_frame,height=25,columns=("ISBN_col","Author_col"))

    # making heading in the tree view
    book_records_treeview.heading("#0",text="Title")
    book_records_treeview.heading("ISBN_col",text="ISBN")
    book_records_treeview.heading("Author_col",text="Author")

    insert_data_book_records_treeview()


    # setting columns width
    book_records_treeview.column(column="#0",width=150)
    book_records_treeview.column(column="ISBN_col",width=150)
    book_records_treeview.column(column="Author_col",width=150)



    book_records_treeview.pack(side=LEFT)

    scroll_treeview = Scrollbar(inside_right_frame)
    scroll_treeview.pack(side=RIGHT,fill=Y)
    scroll_treeview.config(command=book_records_treeview.yview)
    book_records_treeview.config(yscrollcommand=scroll_treeview.set)

    

    root.config(menu=menu_bar)



    

    

