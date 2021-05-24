from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

TITLE = "Client"

def DangNhap():
    def __init__window():
        Client_windows.title(80*" "+TITLE)
        screen_width = Client_windows.winfo_screenwidth()
        screen_height = Client_windows.winfo_screenheight()
        x_cordinate = int((screen_width/2) - (600/2))
        y_cordinate = int((screen_height/2) - (400/2))
        Client_windows.geometry("{}x{}+{}+{}".format(600, 400, x_cordinate, y_cordinate))

    __init__window()
        
Client_windows = Tk()



DangNhap()
Client_windows.mainloop()