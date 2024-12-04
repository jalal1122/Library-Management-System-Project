from tkinter import *
import login_page
import start_page
import sqlite3

# connecting to the database file
conn = sqlite3.connect("database.db")
cur = conn.cursor()

background_color = "#6cc3d7"
second_background_color = "#e9f2f6"
third_color = "#324556"

# function for login up
def signup_func(root):
    email = email_login_page_entry.get()
    password = password_login_page_entry.get()
    pass_confirm = password_confirm_login_page_entry.get()

    cur.execute("SELECT * FROM user_data")
    email_for_c = []
    data_from_fdb = cur.fetchall()
    for item in data_from_fdb:
        email_for_c.append(item[0])
    
    global dup_email
    dup_email = False

    for em in email_for_c:
        if email == em:
            dup_email = True

    if pass_confirm == password and not dup_email:
        # adding user credentials to the database
        cur.execute("INSERT INTO user_data VALUES(?,?)",(email,password))
        conn.commit()
        # goto admin login page
        login_page.login_page(root)
    elif dup_email:
        pass_confirm_var.set("email already found, try another email")
    else:
        pass_confirm_var.set("Password does not match!")
        

def sign_up_page(root):
    global password_confirm_login_page_entry,password_login_page_entry,email_login_page_entry,pass_confirm_var

    pass_confirm_var = StringVar()

    # main frame of sign_up page
    sign_up_page_frame = Frame(root,background=background_color)
    sign_up_page_frame.place(x=0,y=0,relheight=1,relwidth=1)

    # main heading of sign up page
    Label(sign_up_page_frame,text="Sign Up",font="Verdana 35 bold",background=background_color,foreground=third_color).pack(side="top",pady=15)

    # details frame of sign up page
    sign_up_page_details_frame = Frame(sign_up_page_frame,background=background_color,)
    sign_up_page_details_frame.pack(pady=40)

    # email sign up entry and label in a grid
    email_login_page = Label(sign_up_page_details_frame,text="Email:",background=background_color,font="Verdana 20 bold")
    email_login_page.grid(row=0,column=0,ipadx=10,ipady=10)
    email_login_page_entry = Entry(sign_up_page_details_frame,font="Verdana 15 bold",highlightbackground="grey80")
    email_login_page_entry.grid(row=0,column=1,ipadx=10,ipady=5)

    # password sign up entry and label in a grid
    password_login_page = Label(sign_up_page_details_frame,text="Password:",background=background_color,font="Verdana 20 bold")
    password_login_page.grid(row=1,column=0,ipadx=10,ipady=10)
    password_login_page_entry = Entry(sign_up_page_details_frame,font="Verdana 15 bold")
    password_login_page_entry.grid(row=1,column=1,ipadx=10,ipady=5)

    # password confirm sign up page entry and label in a grid
    password_confirm_login_page = Label(sign_up_page_details_frame,text="Password Confirm:",background=background_color,font="Verdana 20 bold")
    password_confirm_login_page.grid(row=2,column=0,ipadx=10,ipady=10)
    password_confirm_login_page_entry = Entry(sign_up_page_details_frame,textvariable=pass_confirm_var,font="Verdana 15 bold")
    password_confirm_login_page_entry.grid(row=2,column=1,ipadx=10,ipady=5)

    # login button
    login_button_sign_up_page = Button(sign_up_page_details_frame,text="Login",command=lambda:login_page.login_page(root),relief=RAISED,background=second_background_color,foreground=third_color,activebackground=background_color,font="Verdana 20 bold",pady=5)
    login_button_sign_up_page.grid(row=3,column=0,ipadx=10,ipady=2)

    # sign up button 
    sign_up_button_sign_up_page = Button(sign_up_page_details_frame,text="Sign Up",command=lambda:signup_func(root),relief=RAISED,background=second_background_color,foreground=third_color,activebackground=background_color,font="Verdana 20 bold",pady=5)
    sign_up_button_sign_up_page.grid(row=3,column=1,ipadx=10,ipady=2)

    # go to start_page button
    home_button = Button(sign_up_page_frame,text="Home page",command=lambda:start_page.start_page(root),font="Verdana 25 bold",relief=RAISED,background=second_background_color,foreground=third_color,activebackground=background_color)
    home_button.pack()