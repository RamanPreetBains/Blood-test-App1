from tkinter import *
import mysql.connector

def onClickSignUp():
    def onClick():
        print("!!")

        class report:
            def __init__(self,Pid, Name, Phone, Age, Gender, Address, Username, Password):
                self.Pid = Pid
                self.Name = Name
                self.Phone = Phone
                self.Age = Age
                self.Gender = Gender
                self.Address = Address
                self.Username = Username
                self.Password = Password

        class DBHelper:
            def savereportInDb(self, cRef):
                sql = "insert into report values(null, '{}', '{}', {}, '{}','{}','{}','{}')".format(cRef.Pid,cRef.Name,
                                                                                                    cRef.Phone,
                                                                                                    cRef.Age,
                                                                                                    cRef.Gender,
                                                                                                    cRef.Address,
                                                                                                    cRef.Username,
                                                                                                    cRef.Password)
                con = mysql.connector.connect(user='root', password="", host="127.0.0.1", database="patientdatabase")
                cursor = con.cursor()
                cursor.execute(sql)
                con.commit()
                print(">>Patient data saved")

        Pid = entryPid.get()
        Name = entryName.get()
        Phone = entryPhone.get()
        Age = entryAge.get()
        Gender = entryGender.get()
        Address = entryAddress.get()
        Username = entryUsername.get()
        Password = entryPassword.get()


        cRef = report(Pid, Name, Phone, Age, Gender, Address, Username, Password)

        dbhelper = DBHelper()
        dbhelper.savereportInDb(cRef)

    WindowSup = Tk()
    lblTitle = Label(WindowSup, text="Add Patient Details Below:")

    lblPid = Label(WindowSup, text="Enter Pid:")
    entryPid = Entry(WindowSup)

    lblName = Label(WindowSup, text="Enter Patient Name:")
    entryName = Entry(WindowSup)

    lblPhone = Label(WindowSup, text="Enter Patient Phone:")
    entryPhone = Entry(WindowSup)

    lblAge = Label(WindowSup, text="Enter Patient Age:")
    entryAge = Entry(WindowSup)

    lblGender = Label(WindowSup, text="Enter Gender:")
    entryGender = Entry(WindowSup)

    lblAddress = Label(WindowSup, text="Enter Patient Address:")
    entryAddress = Entry(WindowSup)

    lblUsername = Label(WindowSup, text="Enter Username:")
    entryUsername = Entry(WindowSup)

    lblPassword = Label(WindowSup, text="Enter Password:")
    entryPassword = Entry(WindowSup)

    btnAddRecord = Button(WindowSup, text="Add Record", command=onClick )

    lblTitle.grid(row=0)
    lblPid.grid(row=1)
    lblName.grid(row=2)
    lblPhone.grid(row=3)
    lblAge.grid(row=4)
    lblGender.grid(row=5)
    lblAddress.grid(row=6)
    lblUsername.grid(row=7)
    lblPassword.grid(row=8)
    btnAddRecord.grid(row=9, column=1)

    entryPid.grid(row=1, column=1)
    entryName.grid(row=2, column=1)
    entryPhone.grid(row=3, column=1)
    entryAge.grid(row=4, column=1)
    entryGender.grid(row=5, column=1)
    entryAddress.grid(row=6, column=1)
    entryUsername.grid(row=7, column=1)
    entryPassword.grid(row=8, column=1)



def Login():
   LoginNext = Tk()

   def fetchreportFromDB(self):
       sql = "select * from report"
       con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="patientdatabase")
       cursor = con.cursor()
       cursor.execute(sql)


def onClickLogin():
    root1 = Tk()
    root1.geometry("400x250")
    root1.title("Login")
    menu = Menu(root1)
    root1.config(menu=menu)
    lblUsername = Label(root1, text="Username")
    lblUsername.pack()
    entryUsername = Entry(root1)
    entryUsername.pack()
    lblPassword = Label(root1, text="Password")
    lblPassword.pack()
    entryPassword = Entry(root1)
    entryPassword.pack()
    btnLogin1 = Button(root1, text="Login", width=15, command=Login)

    btnLogin1.pack()
    

window = Tk()
window.title("Online Laboratory")
window.geometry("400x250")
window.configure(background= 'light yellow')


lblTitle = Label(window, text="Welcome")
lblTitle.pack()

btnSignUp = Button(window, text="Sign Up", width=15,  command=onClickSignUp)
btnSignUp.pack()
btnLogin = Button(window, text="Login ", width=15,  command=onClickLogin)
btnLogin.pack()


window.mainloop()
