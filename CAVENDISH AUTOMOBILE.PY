from tkinter import *
from tkinter import messagebox, Toplevel
from PIL import ImageTk, Image
import os
import csv

root = Tk()
root.title("H2 OP")
# Always save icons photo in the file where this script will be saved
p = PhotoImage(file='D:\\PyCharm\\New PyCharm\\My projects\\4.GIF')
root.iconphoto(False, p)
root.geometry('920x656')  # Order is WidthXHeight
root.minsize(600, 256)  # Order is Width,Height
root.configure(bg='white')

img = PhotoImage(file='D:\\Cavendish logo\\Bg1.png')
label = Label(root, image=img)
label.pack(fill='both', pady='12')
label.place(x=-4, y=-5, relwidth=1, relheight=1)

Text_1 = Label(text="-A vision to make EV and Hydrogen powered vehicles all over the world", fg="dark blue", bg="white",
               font=("comicsansms", 15, "bold"), borderwidth=7, relief=RIDGE)
# relief includes SUNKEN, RAISED, GROOVE, RIDGE
Text_1.pack(fill='x', pady='12')  # This .pack() is a rule in Python to show the stuffs

text = Label(text="Welcome\nto\n", font=("comicsansms", 23, "bold"), fg='black', bg='white', width=24, height=4,
             borderwidth=4, relief=GROOVE)
text.place(x=440, y=80)
u = Label(root, text="Cavendish-Future of Hydrogen", fg="red", font=("comicsansms", 23, "bold"), bg='white')
u.place(x=445, y=180)

my_img = (Image.open("D:\\Cavendish logo\\Main.png"))
resizing_img = my_img.resize([410, 550], Image.Resampling.LANCZOS)  # Resize image Width x Height
new_pic = ImageTk.PhotoImage(resizing_img)
my_label = Label(image=new_pic, borderwidth=7, relief=RAISED)
my_label.pack(anchor="nw")

image1 = Image.open('D:\\Cavendish logo\\login.png')
# Resize the Image
image_1 = image1.resize((100, 50), Image.Resampling.LANCZOS)
# Convert the image to PhotoImage
img1 = ImageTk.PhotoImage(image_1)
image2 = Image.open('D:\\Cavendish logo\\sign up.png')
# Resize the Image
image_2 = image2.resize((100, 50), Image.Resampling.LANCZOS)
# Convert the image to PhotoImage
img2 = ImageTk.PhotoImage(image_2)
image3 = Image.open('D:\\Cavendish logo\\close.png')
# Resize the Image
image_3 = image3.resize((100, 40), Image.Resampling.LANCZOS)
# Convert the image to PhotoImage
img3 = ImageTk.PhotoImage(image_3)


def sign_up():
    New_2Win = Toplevel(root)  # TopLevel object which will be treated as a new window
    New_2Win.title("Sign Up")
    New_2Win.geometry('550x656')  # Order is WidthXHeight
    New_2Win.minsize(550, 656)
    New_2Win.maxsize(550, 656)
    New_2Win.configure(bg='pink')

    heading = Label(New_2Win, text="Sign Up", bg='pink', fg='purple', font='Verdana 30 bold')
    heading.place(x=70, y=60)

    Full_na = Label(New_2Win, text="Full Name :", bg='pink', fg='black', font='Verdana 15 bold')
    Full_na.place(x=70, y=150)
    StringVar()
    Full_na_entry = Entry(New_2Win, width=40)
    Full_na_entry.place(x=225, y=159.5)

    Username = Label(New_2Win, text="Log In ID :", bg='pink', fg='black', font='Verdana 15 bold')
    Username.place(x=70, y=210)
    Username_entry = Entry(New_2Win, width=40)
    Username_entry.place(x=225, y=219.5)

    Password = Label(New_2Win, text="Password :", bg='pink', fg='black', font='Verdana 15 bold')
    Password.place(x=70, y=270)
    Password_entry = Entry(New_2Win, width=40)
    Password_entry.place(x=225, y=279.5)

    def clear():
        Username.delete(0, END)
        Password.delete(0, END)

    Password_confirm = Label(New_2Win, text="Confirm Your\nPassword :", bg='pink', fg='black', font='Verdana 15 bold')
    Password_confirm.place(x=70, y=330)
    Password_confirm = Entry(New_2Win, width=40)
    Password_confirm.place(x=225, y=362.5)
    Password_confirm.config(show="#")

    def user_info():
        User_info = Full_na_entry.get()
        user_ID = Username_entry.get()
        Password_info = Password_entry.get()
        if User_info == "" or user_ID == "" or Password_info == "":
            messagebox.showerror("Error", "Please fill all the details.")
        else:
            f = open("Public Details", "w", newline='')
            wo = csv.writer(f)
            wo.writerow(['Full Name', 'UserId', 'Password'])
            wo.writerow(User_info, user_ID, Password_info)
            f.close()
            messagebox.showinfo("Information", "Account created successfully!!")
            Full_na_entry.delete(0, END)
            Username_entry.delete(0, END)
            Password_entry.delete(0, END)

    Button(New_2Win, text='Sign Up', relief=RIDGE, font='Verdana 11 bold', width=6, height=2, command=user_info).place(
        x=165, y=520)
    btn = Button(New_2Win, text="Clear", font='Verdana 11 bold', width=6, height=2, command=clear, relief=RIDGE)
    btn.place(x=250, y=520)


def login_id():
    New_2Win = Toplevel(root)  # TopLevel object which will be treated as a new window
    New_2Win.title("Sign Up")
    New_2Win.geometry('550x656')  # Order is WidthXHeight
    New_2Win.minsize(550, 656)
    New_2Win.maxsize(550, 656)
    New_2Win.configure(bg='grey')

    heading = Label(New_2Win, text="Log In", bg='white', fg='red', font='Verdana 30 bold')
    heading.place(x=70, y=60)

    Full_na = Label(New_2Win, text="Full Name :", bg='pink', fg='black', font='Verdana 15 bold')
    Full_na.place(x=70, y=150)
    StringVar()
    Full_na_en = Entry(New_2Win, width=40)
    Full_na_en.place(x=225, y=159.5)

    Username = Label(New_2Win, text="Username:", bg='#FAF6FC', fg='black', font='Verdana 18 bold')
    Username.place(x=70, y=210)
    Username_en = Entry(New_2Win, width=40)
    Username_en.place(x=225, y=219.5)

    Password = Label(New_2Win, text="Password:", bg='#FAF6FC', fg='black', font='Verdana 18 bold')
    Password.place(x=70, y=270)
    Password_en = Entry(New_2Win, width=40)
    Password_en.place(x=225, y=279.5)
    Password.config(show='*')

    def login_verify():
        uname = Username_en.get()
        pword = Password_en.get()
        file_exists = os.path.exists('register.txt')

        print(file_exists)
        list_of_files = os.listdir('D:\\PyCharm\\New PyCharm\\My projects')
        if uname == list_of_files:
            file1 = open(uname, "r")
            content = file1.read().splitlines()
            if pword in content:
                messagebox.showinfo("Information", "Login is successful!!")
                New_3Win = Toplevel(root)  # TopLevel object which will be treated as a new window
                New_3Win.title("All about Cavendish")
                New_3Win.geometry('920x656')

            else:
                messagebox.showerror("Error", "Wrong Password Entered")
            file1.close()
            Username_en.delete(0, END)
            Password_en.delete(0, END)
        else:
            messagebox.showerror("Error", "Account not found!\nPlease enter correct details.")

    Button(New_Win, width=6, height=2, text='Log In', command=login_verify, font='Verdana 11 bold', relief=RIDGE) \
        .place(x=640, y=320)

    acc = Label(New_Win, text="Make a account here ->", fg='red', bg='#FAF6FC', font='Verdana 15 bold')
    acc.place(x=500, y=485)
    bton = Button(New_Win, width=10, height=2, text="Sign Up now", font='Verdana 11 bold', command=sign_up,
                  relief=RIDGE)
    bton.place(x=794, y=478)

    def clear():
        Username.delete(0, END)
        # Password.delete(0, END)

    btn = Button(New_Win, width=6, height=2, text="Clear", font='Verdana 11 bold', command=clear, relief=RIDGE)
    btn.place(x=740, y=320)

    """
    New_Win = Toplevel(root)  # TopLevel object which will be treated as a new window
    New_Win.title("Login")
    New_Win.geometry('1050x656')  # Order is WidthXHeight
    New_Win.minsize(1050, 656)
    New_Win.maxsize(1050, 656)
    New_Win.configure(bg="#C6E5FD")

    #my_im = (Image.open('D:\\Cavendish logo\\Bg4.png'))
    #resizing_im = my_im.resize([365, 590], Image.Resampling.LANCZOS)  # Resize image Width x Height
    #new_pi = ImageTk.PhotoImage(resizing_im)
    #my_labe = Label(New_Win, image=new_pi, borderwidth=7, relief=RAISED)
    #my_labe.place(x=45, y=30)

    h = Label(New_Win, width=75, bg='#FAF6FC', height=39, borderwidth=7, relief=RAISED)
    h.place(x=300, y=20)

    heading = Label(New_Win, text="Log In", fg='red', bg='#FAF6FC', font='Verdana 25 bold')
    heading.place(x=350, y=15)
    heading.pack()

    Username = Label(New_Win, text="Username:", bg='#FAF6FC', fg='black', font='Verdana 18 bold')
    Username.place(x=500, y=150)
    Username_en = Entry(New_Win, width=30)
    Username.place(x=650, y=159.5)
    Username.pack()

    #Password = Label(New_Win, text="Password:", bg='#FAF6FC', fg='black', font='Verdana 18 bold')
    #Password.place(x=500, y=220)
    #Password_en = Entry(New_Win, width=40)
    #Password.place(x=648, y=229.5)
    #Password.config(show='*')
    #Password.pack()
    Password_en = 123
    def login_verify():
        uname = Username_en.get()
        pword = 123#Password_en.get()
        list_of_files = os.listdir('D:\\PyCharm\\New PyCharm\\My projects')
        if uname == list_of_files:
            file1 = open(uname, "r")
            content = file1.read().splitlines()
            if pword in content:
                messagebox.showinfo("Information", "Login is successful!!")
                New_3Win = Toplevel(root)  # TopLevel object which will be treated as a new window
                New_3Win.title("All about Cavendish")
                New_3Win.geometry('920x656')

            else:
                messagebox.showerror("Error", "Wrong Password Entered")
            file1.close()
            Username_en.delete(0, END)
            #Password_en.delete(0, END)
        else:
            messagebox.showerror("Error", "Account not found!\nPlease enter correct details.")


    Button(New_Win, width=6, height=2, text='Log In', command=login_verify, font='Verdana 11 bold', relief=RIDGE) \
        .place(x=640, y=320)

    acc = Label(New_Win, text="Make a account here ->", fg='red', bg='#FAF6FC', font='Verdana 15 bold')
    acc.place(x=500, y=485)
    bton = Button(New_Win, width=10, height=2, text="Sign Up now", font='Verdana 11 bold', command=sign_up,
                  relief=RIDGE)
    bton.place(x=794, y=478)

    def clear():
        Username.delete(0, END)
        #Password.delete(0, END)

    btn = Button(New_Win, width=6, height=2, text="Clear", font='Verdana 11 bold', command=clear, relief=RIDGE)
    btn.place(x=740, y=320)

"""
def close():
    root.destroy()


# Creating a button with more than one command using lambda
b1 = Button(bg="white", image=img1, command=login_id, borderwidth=3, relief=RAISED)
b1.place(x=625, y=250)
b2 = Button(bg="white", image=img2, command=sign_up, borderwidth=3, relief=RAISED)
b2.place(x=625, y=320)
b3 = Button(bg="white", image=img3, command=close, borderwidth=3, relief=RAISED)
b3.place(x=625, y=390)

root.mainloop()
