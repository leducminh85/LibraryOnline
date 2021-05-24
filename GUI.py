from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

TITLE = "LOGIN"

def PlaceWindow(window, window_width, window_height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

def CloseWindow(root):
    root.destroy()

def __init__window():
    def Login(event):
        def LoginCheck():
            #check
            LoginFail()

        def LoginFail():
            RootLoginFail = Toplevel(Client_windows)
            RootLoginFail.grab_set()

            RootLoginFail.title(10*' '+"Lỗi đăng nhập")
            PlaceWindow(RootLoginFail, 300, 180)

            FailLabel = Label(RootLoginFail, text = "Tài khoản hoặc mật khẩu của bạn không chính xác!\n Vui lòng nhập lại")
            FailLabel.place(x=10, y = 40)
            OkButton = Button(RootLoginFail, text = "OK",command = lambda: CloseWindow(RootLoginFail))
            OkButton.place(x = 85, y = 110, width = 130)

        def LoginSuccessful():
            pass
        
        LoginCheck()

    def Register(event):
        def checkRegistry():
            #check
            #RegisterSuccessful()
            RegisterFail()

        def RegisterSuccessful():
            RootRS = Toplevel(RootRegister)
            RootRS.grab_set()
            RootRS.title(10*' '+"Thông báo")
            PlaceWindow(RootRS, 300, 150)

            SuccessfulLabel = Label(RootRS, text = "Đăng kí thành công!")
            SuccessfulLabel.place(x=100, y = 30)
            OkButton = Button(RootRS, text = "OK",command = lambda: [CloseWindow(RootRS),CloseWindow(RootRegister)])
            OkButton.place(x = 85, y = 80, width = 130)

        def RegisterFail():
            RootRF = Toplevel(RootRegister)
            RootRF.grab_set()
            RootRF.title(10*' '+"Thông báo")
            PlaceWindow(RootRF, 300, 150)

            SuccessfulLabel = Label(RootRF, text = "Tài khoản của bạn đã tồn tại!\n Vui lòng đăng ký lại")
            SuccessfulLabel.place(x=80, y = 30)
            OkButton = Button(RootRF, text = "OK",command = lambda: CloseWindow(RootRF))
            OkButton.place(x = 85, y = 80, width = 130)

        
        RootRegister = Toplevel(Client_windows)
        RootRegister.grab_set()

        RootRegister.title(30*' '+"Đăng ký tài khoản")
        PlaceWindow(RootRegister, 400, 150)

        usernameLabel = Label(RootRegister, text = "Username: ")
        usernameLabel.place(x = 30, y = 10)
        usernameEntry = Entry(RootRegister)
        usernameEntry.place(x= 130, y = 10, width = 200)

        passwordLabel = Label(RootRegister, text = "Password: ")
        passwordLabel.place(x = 30, y = 50)
        passwordEntry = Entry(RootRegister)
        passwordEntry.place(x= 130, y = 50, width = 200)

        #checkButton
        OkButton = Button(RootRegister, text = "OK",command = checkRegistry)
        OkButton.place(x = 140, y = 95, width = 130)

    #init window
    Client_windows.title(80*" "+TITLE)
    PlaceWindow(Client_windows, 600, 400)
    Client_windows.resizable(0, 0)

    #label Library
    Label_Library = Text(Client_windows, bd = 0)
    Label_Library.place(x = 200, y = 60, width = 200, height = 20)
    Label_Library.insert('end',6*" "+"LIBRARY ONLINE")
    Label_Library.configure(state='disabled')

    #username va password
    usernameLabel = Label(Client_windows, text = "Username: ")
    usernameLabel.place(x = 100, y = 140)

    usernameEntry = Entry(Client_windows)
    usernameEntry.place(x= 200, y = 140, width = 200)

    passwordLabel = Label(Client_windows, text = "Password: ")
    passwordLabel.place(x = 100, y = 190)

    passwordEntry = Entry(Client_windows)
    passwordEntry.place(x= 200, y = 190, width = 200)

    #Dang nhap, dang ki
    LoginButton = Button(Client_windows, text = "Đăng nhập")
    LoginButton.bind("<Button-1>",Login)
    LoginButton.place(x = 320, y = 250, width = 80)

    RegisterButton = Button(Client_windows, text = "Đăng ký")
    RegisterButton.bind("<Button-1>",Register)
    RegisterButton.place(x = 200, y = 250, width = 80)

        

        
Client_windows = Tk()
__init__window()

Client_windows.mainloop()