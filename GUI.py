from tkinter import *
from tkinter import ttk
import tkinter as tk
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

def Function():
    def Logout():
        print("Logout")
        RootFunction.destroy()
        main()

    def Search():
        print("Search")
        
    def SelectFunction(event):
        def ReadBook():    
            def Back():
                CloseWindow(RootRead)
                FunctionChoosen.set("Chọn chức năng") 

            RootRead = Toplevel(RootFunction)
            RootRead.grab_set()
            RootRead.title(220*' '+"Đọc sách")
            PlaceWindow(RootRead, 1500, 800)
            RootRead.resizable(0, 0)

            #BackToMenu
            BackButton = Button(RootRead, text = "Trở lại", command = Back)
            BackButton.place(x= 20, y = 20, width = 100)

            #Input BookID
            BookIDInput = Text(RootRead)
            BookIDInput.insert('end',"Nhập ID sách....")
            BookIDInput.place(x = 20, y = 70, width = 800, height = 20)

            #Input ID Button
            InputIDButton = Button(RootRead, text = "Xem sách")
            InputIDButton.place(x= 830, y = 70, width = 200)
        
            #BookContent
            BookContent = Text(RootRead)
            BookContent.configure(state='disabled')
            BookContent.place(x = 20, y = 110, width = 1450, height = 650)
            vsb = ttk.Scrollbar(RootRead, command=BookContent.yview)
            vsb.place(x = 1470, y = 110, height =650)



        def DownloadBook():
            print("Download book")
        
        s= FunctionChoosen.get()
        if  s == " Đọc sách": ReadBook()
        if  s == " Tải sách": DownloadBook()
   

    RootFunction = Tk()
    RootFunction.title(220*' '+"MENU")
    PlaceWindow(RootFunction, 1500, 700)
    RootFunction.resizable(0, 0)

    #Library Label
    LibraryLabel = Text(RootFunction, bd = 0)
    LibraryLabel.insert('end',80*" "+"ONLINE LIBRARY")
    LibraryLabel.configure(state='disabled')
    LibraryLabel.place(x = 20, y = 20, height = 20, width = 1460)

    #HelloLabel
    userName = ".........."  #insert userName here
    HelloLabel = Label(RootFunction, text = "Xin chào " + userName)
    HelloLabel.place(x = 1200-userName.__len__(), y = 50)

    #LogoutButton
    SearchButton = Button(RootFunction, text ="Đăng xuất", command = Logout)
    SearchButton.place(x=1300, y = 50, width = 180)
    
    #ChooseFunction
    FunctionChoosen = ttk.Combobox(RootFunction,state="readonly")
    FunctionChoosen.set("Chọn chức năng") 
    FunctionChoosen['values'] = (' Đọc sách',' Tải sách')
    FunctionChoosen.place(x = 20, y = 60, width = 200)
    FunctionChoosen.bind('<<ComboboxSelected>>', SelectFunction)

    #SearchBook
    SearchBox = Text(RootFunction)
    SearchBox.insert('end',"Tra cứu tại đây...")
    SearchBox.place(x = 20, y = 100, height = 20, width = 1200)

    #SearchButton
    SearchButton = Button(RootFunction, text ="Tra cứu", command = Search)
    SearchButton.place(x=1250, y = 100, width = 230)


    #TableBook
    tree =ttk.Treeview(RootFunction, column=("c1", "c2", "c3","c4","c5","c6"), show='headings')
    vsb = ttk.Scrollbar(RootFunction, orient="vertical", command=tree.yview)

    tree.bind('<Button-1>', "break")
   
    tree.column("#1", anchor=tk.CENTER, minwidth=0, width=50, stretch= FALSE)
    tree.heading("#1", text="STT")
    tree.column("#2", anchor=tk.CENTER, minwidth=0, width=450 ,stretch=FALSE)
    tree.heading("#2", text="Tên sách")
    tree.column("#3", anchor=tk.CENTER, minwidth=0, width=150, stretch=FALSE)
    tree.heading("#3", text="ID")
    tree.column("#4", anchor=tk.CENTER, minwidth=0, width=350, stretch=FALSE)
    tree.heading("#4", text="Tác giả")
    tree.column("#5", anchor=tk.CENTER, minwidth=0, width=300, stretch=FALSE)
    tree.heading("#5", text="Loại sách")
    tree.column("#6", anchor=tk.CENTER, minwidth=0, width=140, stretch=FALSE)
    tree.heading("#6", text="Năm sáng tác")
    tree.place(x = 20, y = 150, height = 520)
    vsb.place(x=20+50+450+150+350+300+140, y=150, height=520)
    
    
def __init__window(Client_windows):
    def Login(event):
        def LoginCheck():
            #check
            #LoginFail()
            LoginSuccessful()
            
            
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
            RootLoginS = Toplevel(Client_windows)
            RootLoginS.grab_set()

            RootLoginS.title(10*' '+"Đăng nhập")
            PlaceWindow(RootLoginS, 300, 180)

            FailLabel = Label(RootLoginS, text = "Đăng nhập thành công! \n Nhấn OK để tiếp tục")
            FailLabel.place(x= 90, y = 40)
            OkButton = Button(RootLoginS, text = "OK",command = lambda: [CloseWindow(Client_windows),Function()])
            OkButton.place(x = 85, y = 110, width = 130)
            
        
        LoginCheck()

    def Register(event):
        def checkRegistry():
            #check
            RegisterSuccessful()
            #RegisterFail()

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

    def End(event):
        CloseWindow(Client_windows)

    #init window
    Client_windows.title(80*" "+TITLE)
    PlaceWindow(Client_windows, 600, 400)
    Client_windows.resizable(0, 0)

    #label Library
    Label_Library = Text(Client_windows, bd = 0)
    Label_Library.place(x = 200, y = 60, width = 200, height = 20)
    Label_Library.insert('end',6*" "+"ONLINE LIBRARY")
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

    EndButton = Button(Client_windows, text = "Kết thúc")
    EndButton.bind("<Button-1>", End)
    EndButton.place(x = 200, y = 300, width = 200)    

def main():     
    Client_windows = Tk()
    __init__window(Client_windows)
    Client_windows.mainloop()

main()