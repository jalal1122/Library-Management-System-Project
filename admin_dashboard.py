from tkinter import *
from tkinter import ttk
import start_page
import sqlite3

conn = sqlite3.connect("database.db")
cur = conn.cursor()

background_color = "#6cc3d7"
second_background_color = "#e9f2f6"
third_color = "#324556"

# function for add book
def reset_pass_func():
    # for creating a new window
    reset_pass_window = Toplevel()

    reset_pass_window.geometry("600x220")
    reset_pass_window.title("Add Book")
    reset_pass_window.config(background=background_color)

    # window resizing
    reset_pass_window.resizable(NO,NO)

    # creating a frame
    reset_pass_window_frame = Frame(reset_pass_window,background=background_color)
    reset_pass_window_frame.place(relheight=1,relwidth=1)

    frame2 = Frame(reset_pass_window_frame,background=background_color)
    frame2.pack(pady=[20,0])
    user_email_label = Label(frame2,text="Email: ",background=background_color,font="Verdana 20 bold")
    user_email_label.grid(row=0,column=0)
    user_email_entry = Entry(frame2,font="Verdana 15 bold",highlightbackground=second_background_color)
    user_email_entry.grid(row=0,column=1,padx=[40,0])

    frame3 = Frame(reset_pass_window_frame,background=background_color)
    frame3.pack(pady=[20,0])
    password_reset_label = Label(frame3,text="New Password: ",background=background_color,font="Verdana 20 bold")
    password_reset_label.grid(row=0,column=0)
    password_reset_entry = Entry(frame3,font="Verdana 15 bold",highlightbackground=second_background_color)
    password_reset_entry.grid(row=0,column=1,padx=[40,0])

    def reset_pass_com():
        pass_reset = password_reset_entry.get()

        cur.execute(f"UPDATE user_data SET user_password = '{pass_reset}' WHERE user_email = '{user_email_entry.get()}'")
        conn.commit()
    
        for i in user_accounts_treeview.get_children():
            user_accounts_treeview.delete(i)

        insert_user_accounts_treeview()

        reset_pass_window.destroy()
        

    reset_pass_add_button = Button(reset_pass_window_frame,command=reset_pass_com,text="Reset Password",background=background_color,font="Verdana 20 bold")
    reset_pass_add_button.pack(ipadx=25,pady=30)

# function for add book
def delete_user_func():
    # for creating a new window
    delete_user_window = Toplevel()

    delete_user_window.geometry("600x220")
    delete_user_window.title("Add Book")
    delete_user_window.config(background=background_color)

    # window resizing
    delete_user_window.resizable(NO,NO)

    # creating a frame
    delete_user_window_frame = Frame(delete_user_window,background=background_color)
    delete_user_window_frame.place(relheight=1,relwidth=1)

    frame3 = Frame(delete_user_window_frame,background=background_color)
    frame3.pack(pady=[20,0])
    user_email_label = Label(frame3,text="Email: ",background=background_color,font="Verdana 20 bold")
    user_email_label.grid(row=0,column=0)
    user_email_entry = Entry(frame3,font="Verdana 15 bold",highlightbackground=second_background_color)
    user_email_entry.grid(row=0,column=1,padx=[40,0])

    frame2 = Frame(delete_user_window_frame,background=background_color)
    frame2.pack()
    user_password_label = Label(frame2,text="Password: ",background=background_color,font="Verdana 20 bold")
    user_password_label.grid(row=0,column=0)
    user_password_label_entry = Entry(frame2,font="Verdana 15 bold",highlightbackground=second_background_color)
    user_password_label_entry.grid(row=0,column=1,padx=[15,0])

    def delete_user_account_com():
        email = user_email_entry.get()
        password = user_password_label_entry.get()
        cur.execute(f"DELETE FROM user_data WHERE user_email LIKE {email} AND user_password LIKE {password}")
        conn.commit()
    
        for i in user_accounts_treeview.get_children():
            user_accounts_treeview.delete(i)

        insert_user_accounts_treeview()

        delete_user_window.destroy()
        

    add_book_add_button = Button(delete_user_window_frame,command=delete_user_account_com,text="Delete",background=background_color,font="Verdana 20 bold")
    add_book_add_button.pack(ipadx=25,pady=30)

# insert in to the user accounts treeview 
def insert_user_accounts_treeview():
    # data from the database
    user_email = []
    user_password = []

    cur.execute("SELECT * FROM user_data")
    data_from_user_data = cur.fetchall()
    for item in data_from_user_data:
        user_email.append(item[0])
        user_password.append(item[1])
    
    # inserting data in treeview
    for limit in range(len(user_email)):
        user_accounts_treeview.insert("",END,text=user_email[limit],values=[user_password[limit]])

def admin_dashboard(root):
    global user_accounts_treeview

    # changing windows size
    root.geometry("800x360")

    # admin dashbaord frame
    admin_dashboard_frame = Frame(root,background=background_color)
    admin_dashboard_frame.place(relheight=1,relwidth=1)

    # heading label
    Label(admin_dashboard_frame,text="Admin Dashboard",font="Verdana 25 bold",background=background_color).pack(pady=5)

    # frame for left and right frame
    flfframe = Frame(admin_dashboard_frame,background=background_color)
    flfframe.pack()

    # left frame
    left_admin_dashboard_frame = Frame(flfframe,background=background_color)
    left_admin_dashboard_frame.grid(row=0,column=0,sticky=NSEW,padx=[0,100])

    # delete account button
    delete_account_btn = Button(left_admin_dashboard_frame,command=delete_user_func,text="Delete Account",font="Verdana 15 bold",background=second_background_color,foreground=third_color,activebackground=background_color)
    delete_account_btn.pack(pady=[60,10])

    # reset password button
    reset_password_btn = Button(left_admin_dashboard_frame,command=reset_pass_func,text="Reset Password",font="Verdana 15 bold",background=second_background_color,foreground=third_color,activebackground=background_color)
    reset_password_btn.pack(pady=10)

    # logout button
    logout_btn = Button(left_admin_dashboard_frame,command=lambda:start_page.start_page(root),text="Logout",font="Verdana 15 bold",background=second_background_color,foreground=third_color,activebackground=background_color)
    logout_btn.pack(pady=10)
    
    # right frame
    right_admin_dashboard_frame = Frame(flfframe,background=background_color)
    right_admin_dashboard_frame.grid(row=0,column=1,sticky=NSEW)

    
    user_account_label = Label(right_admin_dashboard_frame,text="Users Accounts",font="Verdana 20 bold",background=background_color,foreground=third_color)
    user_account_label.pack(pady=5)

     # Tree view for book records
    user_accounts_treeview = ttk.Treeview(right_admin_dashboard_frame,columns=("user_password_col"))

    # making heading in the tree view
    user_accounts_treeview.heading("#0",text="Email")
    user_accounts_treeview.heading("user_password_col",text="Password")

    # setting columns width
    user_accounts_treeview.column(column="#0",width=200)
    user_accounts_treeview.column(column="user_password_col",width=200)

    # showing data in the treeview from the database
    insert_user_accounts_treeview()

    user_accounts_treeview.pack()