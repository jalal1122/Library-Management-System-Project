from tkinter import *
import start_page
import admin_dashboard
import sqlite3

# connecting to the database file
conn = sqlite3.connect("database.db")
cur = conn.cursor()

background_color = "#6cc3d7"
second_background_color = "#e9f2f6"
third_color = "#324556"

def login_admin_page_func(root):
    email = email_admin_login_page_entry.get()
    password = password_admin_login_page_entry.get()

    user_email = ""
    user_pass = ""

    cur.execute("SELECT * FROM admin_acc")
    data = cur.fetchall()
    for item in data:
        user_email = item[0]
        user_pass = item[1]
    
    if email == user_email and password == user_pass:
        admin_dashboard.admin_dashboard(root)
    else:
        pass_var.set("!Incorect Email or Password")




def admin_login_page(root):
    global email_admin_login_page_entry,password_admin_login_page_entry,pass_var

    pass_var = StringVar()

    # main frame of login page
    admin_login_page_frame = Frame(root,background=background_color)
    admin_login_page_frame.place(x=0,y=0,relheight=1,relwidth=1)

    # main heading of login page
    Label(admin_login_page_frame,text="Admin Login",font="Verdana 35 bold",background=background_color,foreground=third_color).pack(side="top",pady=15)

    # details frame of login page
    admin_login_page_details_frame = Frame(admin_login_page_frame,background=background_color,)
    admin_login_page_details_frame.pack(pady=70)

    # email login entry and label in a grid
    email_admin_login_page = Label(admin_login_page_details_frame,text="Email:",background=background_color,font="Verdana 20 bold")
    email_admin_login_page.grid(row=0,column=0,ipadx=10,ipady=10)
    email_admin_login_page_entry = Entry(admin_login_page_details_frame,font="Verdana 15 bold",highlightbackground="grey80")
    email_admin_login_page_entry.grid(row=0,column=1,ipadx=10,ipady=5)

    # password login entry and label in a grid
    password_admin_login_page = Label(admin_login_page_details_frame,text="Password:",background=background_color,font="Verdana 20 bold")
    password_admin_login_page.grid(row=1,column=0,ipadx=10,ipady=10)
    password_admin_login_page_entry = Entry(admin_login_page_details_frame,textvariable=pass_var,font="Verdana 15 bold")
    password_admin_login_page_entry.grid(row=1,column=1,ipadx=10,ipady=5)

    # login button
    login_button_admin_login_page = Button(admin_login_page_details_frame,text="Login",command=lambda:login_admin_page_func(root),relief=RAISED,background=second_background_color,foreground=third_color,activebackground=background_color,font="Verdana 20 bold")
    login_button_admin_login_page.grid(row=2,column=1,ipadx=10,ipady=2)

    # go to start_page button
    home_button = Button(admin_login_page_frame,text="Home page",command=lambda:start_page.start_page(root),font="Verdana 25 bold",relief=RAISED,background=second_background_color,foreground=third_color,activebackground=background_color)
    home_button.pack()