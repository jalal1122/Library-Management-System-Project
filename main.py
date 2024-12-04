from tkinter import *
import start_page


# variables for width and height of window 
win_width=800
win_height=540


background_color = "#6cc3d7"
second_background_color = "#e9f2f6"
third_color = "#324556"



root = Tk()

# setting size of the window
root.geometry(f"{win_width}x{win_height}")
# root.wm_iconbitmap("icons8-library-building-16.png")

root.config(background="grey")

# making it non resizable
root.wm_resizable(NO,NO)

start_page.start_page(root)




root.mainloop()

