from tkinter import *
#from tkinter import messagebox, Toplevel
from PIL import ImageTk, Image
#import os
#import csv

root = Tk()
root.title("By Archisman")
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

Text_1 = Label(text="Maintain your personal information here.", fg="dark blue", bg="white",
               font=("comicsansms", 15, "bold"), borderwidth=7, relief=RIDGE)
# relief includes SUNKEN, RAISED, GROOVE, RIDGE
Text_1.pack(fill='x', pady='12')  # This .pack() is a rule in Python to show the stuffs

text = Label(text="Welcome\nto\n", font=("comicsansms", 23, "bold"), fg='black', bg='white', width=24, height=4,
             borderwidth=4, relief=GROOVE)
text.place(x=440, y=80)
u = Label(root, text="Secure Everything", fg="red", font=("comicsansms", 23, "bold"), bg='white')
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

root.mainloop()