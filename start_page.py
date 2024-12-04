from tkinter import *
import login_page
import admin_login_page

background_color = "#6cc3d7"
second_background_color = "#e9f2f6"
third_color = "#324556"
fourth_color = "#324556"
fifth_color = "#BD51DF"
sixth_color = "#242A31"
seventh_color = "#BCCECF"
eight_color = "#5FC7F1"

def start_page(root):
    root.geometry("800x540")

    start_page_frame = Frame(root,background=background_color)
    start_page_frame.place(relheight=1,relwidth=1)

    # start heading
    Label(start_page_frame,text="Welcome to Library Management System",font="Verdana 20 bold",background=background_color,foreground=fourth_color).pack(side=TOP,pady=10)
    Label(start_page_frame,text="by",font="Verdana 20 bold",background=background_color,foreground=fourth_color).pack(side=TOP,pady=5)
    Label(start_page_frame,text="MJ DEV STUDIO",font="Verdana 40 bold",background=background_color,foreground=fourth_color).pack(side=TOP,pady=10)

    inside_start_page_frame = Frame(start_page_frame,background=background_color)
    inside_start_page_frame.pack()

    admin_button = Button(inside_start_page_frame,text="Admin Login",command=lambda:admin_login_page.admin_login_page(root),font="Verdana 20 bold",padx=20,pady=5,relief=RAISED,background=second_background_color,foreground=third_color,activebackground=background_color)
    admin_button.pack(side=LEFT,padx=50,pady=50)
    user_button = Button(inside_start_page_frame,command=lambda:login_page.login_page(root),text="User Login",font="Verdana 20 bold",padx=20,pady=5,relief=RAISED,background=second_background_color,foreground=third_color,activebackground=background_color)
    user_button.pack(padx=50,pady=50)
    exit_button = Button(start_page_frame,text="Exit",command=root.destroy,font="Verdana 20 bold",padx=20,pady=5,relief=RAISED,background=second_background_color,foreground=third_color,activebackground=background_color)
    exit_button.pack(pady=30)