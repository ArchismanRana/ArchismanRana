import tkinter
from tkinter import *
from tkinter import messagebox, Toplevel
from PIL import ImageTk, Image
from tkinter import filedialog
from docx2pdf import convert
import pathlib
from pdf2docx import Converter

root = Tk()
root.title("PDF converter and merging PDF's")
# Always save icons photo in the file where this script will be saved
p = PhotoImage(file='D:\\Cavendish logo\\5.png')
root.iconphoto(False, p)
root.geometry('920x656')  # Order is WidthXHeight
root.minsize(600, 256)  # Order is Width,Height
root.configure(bg='white')

img = PhotoImage(file='D:\\Cavendish logo\\Bg1.png')
label = Label(root, image=img)
label.pack(fill='both', pady='12')
label.place(x=-4, y=-5, relwidth=1, relheight=1)

Text_1 = Label(text="Welcome to PDF converter and Merging PDF", fg="dark blue", bg="white",
               font=("comicsansms", 20, "bold"), borderwidth=7, relief=RIDGE)
# relief includes SUNKEN, RAISED, GROOVE, RIDGE
Text_1.pack(fill='x', pady='14')  # This .pack() is a rule in Python to show the stuffs

image1 = Image.open('D:\\Cavendish logo\\Word to PDF.png')
# Resize the Image
image_1 = image1.resize((166, 100), Image.ANTIALIAS)
# Convert the image to PhotoImage
img1 = ImageTk.PhotoImage(image_1)
image2 = Image.open('D:\\Cavendish logo\\PDF to word.png')
# Resize the Image
image_2 = image2.resize((166, 100), Image.ANTIALIAS)
# Convert the image to PhotoImage
img2 = ImageTk.PhotoImage(image_2)
image3 = Image.open('D:\\Cavendish logo\\close.png')
# Resize the Image
image_3 = image3.resize((120, 60), Image.ANTIALIAS)
# Convert the image to PhotoImage
img3 = ImageTk.PhotoImage(image_3)
image4 = Image.open('D:\\Cavendish logo\\Excel to pdf.png')
# Resize the Image
image_4 = image4.resize((166, 100), Image.ANTIALIAS)
# Convert the image to PhotoImage
img4 = ImageTk.PhotoImage(image_4)
image5 = Image.open('D:\\Cavendish logo\\PDF to excel.png')
# Resize the Image
image_5 = image5.resize((166, 100), Image.ANTIALIAS)
# Convert the image to PhotoImage
img5 = ImageTk.PhotoImage(image_5)
image6 = Image.open('D:\\Cavendish logo\\Merge PDF.png')
# Resize the Image
image_6 = image6.resize((206, 206), Image.ANTIALIAS)
# Convert the image to PhotoImage
img6 = ImageTk.PhotoImage(image_6)


def w_to_p():
    New_Win = Toplevel(root)  # TopLevel object which will be treated as a new window
    New_Win.title("Word to pdf")
    New_Win.geometry('800x400')  # Order is WidthXHeight
    New_Win.minsize(800, 400)
    New_Win.maxsize(1000, 600)
    New_Win.configure(bg='#c2c3ed')

    heading = Label(New_Win, text="Convert Doc to PDF", bg='#c2c3ed', fg='black', font='Verdana 30 bold')
    heading.place(x=70, y=60)

    Doc = Label(New_Win, text="Enter File path:", bg='#c2c3ed', fg='black', font='Verdana 20 bold')
    Doc.place(x=70, y=150)
    StringVar()
    En = Entry(New_Win, font=40, width=60)
    En.place(x=70, y=198)

    def open_file():
        file = filedialog.askopenfile(mode='r')
        En.insert(tkinter.END, file)
        if pathlib.Path(file).suffix == '.docx':
            convert(file)
            messagebox.showinfo("Information", "File converted Successfully!!")
        else:
            messagebox.showerror("Error", "Enter a file with extension .docx")

    Doc_entry = Button(New_Win, text="Browse File and Convert", bg="white", fg='green', relief=RIDGE,
                       font='Verdana 15 bold',
                       width=20,
                       height=1, command=open_file)
    Doc_entry.place(x=70, y=245)


def p_to_w():
    New_Win = Toplevel(root)  # TopLevel object which will be treated as a new window
    New_Win.title("Pdf to Word")
    New_Win.geometry('800x400')  # Order is WidthXHeight
    New_Win.minsize(800, 400)
    New_Win.maxsize(1000, 600)
    New_Win.configure(bg='#c2c3ed')

    heading = Label(New_Win, text="Convert PDF to Doc", bg='#c2c3ed', fg='black', font='Verdana 30 bold')
    heading.place(x=70, y=60)

    Doc = Label(New_Win, text="Enter File path:", bg='#c2c3ed', fg='black', font='Verdana 20 bold')
    Doc.place(x=70, y=140)
    StringVar()
    En1 = Entry(New_Win, font=40, width=60)
    En1.place(x=70, y=185)
    Rename = Label(New_Win, text="Rename File:", bg='#c2c3ed', fg='black', font='Verdana 20 bold')
    Rename.place(x=70, y=280)
    StringVar()

    # En2 = Entry(New_Win, font=40, width=40)
    # En2.place(x=70, y=320)

    def open_file():
        global file
        file = filedialog.askopenfile(mode='r')
        En1.insert(tkinter.END, file)

    Doc_entry = Button(New_Win, text="Browse File", bg="white", fg='green', relief=RIDGE,
                       font='Verdana 15 bold',
                       width=12,
                       height=1, command=open_file)
    Doc_entry.place(x=70, y=220)

    def converty():
        open_file()
        pdf = file
        # reanam = En2
        cv = Converter(pdf)
        # cv.convert(reanam)
        cv.close()

    convey = Button(New_Win, text="Convert", bg="white", fg='green', relief=RIDGE,
                    font='Verdana 15 bold',
                    width=12,
                    height=1, command=converty)
    convey.place(x=550, y=280)


def merging():
    import PyPDF2

    New_Win = Toplevel(root)  # TopLevel object which will be treated as a new window
    New_Win.title("Merging 2 pdf's")
    New_Win.geometry('800x470')  # Order is WidthXHeight
    New_Win.minsize(800, 400)
    New_Win.maxsize(1000, 600)
    New_Win.configure(bg='#c2c3ed')

    heading = Label(New_Win, text="Add two pdf's into a single pdf", bg='#c2c3ed', fg='black', font='Verdana 30 bold')
    heading.place(x=70, y=60)

    Doc_1 = Label(New_Win, text="Enter first File path:", bg='#c2c3ed', fg='black', font='Verdana 20 bold')
    Doc_1.place(x=70, y=140)
    En1 = Entry(New_Win, font=40, width=60)
    En1.place(x=70, y=185)

    Doc_2 = Label(New_Win, text="Enter second File path:", bg='#c2c3ed', fg='black', font='Verdana 20 bold')
    Doc_2.place(x=70, y=290)
    En2 = Entry(New_Win, font=40, width=60)
    En2.place(x=70, y=335)

    def open_1file():
        global file1
        file1 = filedialog.askopenfile()
        with open(file1, "r", encoding="utf-8") as f:
            string = f.read()
        En1.insert(tkinter.END, string)

    def open_2file():
        global file2
        file2 = filedialog.askopenfile(mode='r')
        En2.insert(tkinter.END, file2)

    Doc_1entry = Button(New_Win, text="Browse File", bg="white", fg='green', relief=RIDGE,
                        font='Verdana 15 bold',
                        width=12,
                        height=1, command=open_1file)
    Doc_1entry.place(x=70, y=220)
    Doc_2entry = Button(New_Win, text="Browse File", bg="white", fg='green', relief=RIDGE,
                        font='Verdana 15 bold',
                        width=12,
                        height=1, command=open_2file)
    Doc_2entry.place(x=70, y=370)
    open_1file()
    open_2file()
    # Open the files that have to be merged one by one
    pdf1File = open(file1, 'rb')
    pdf2File = open(file2, 'rb')

    # Read the files that you have opened
    pdf1Reader = PyPDF2.PdfFileReader(pdf1File)
    pdf2Reader = PyPDF2.PdfFileReader(pdf2File)

    # Create a new PdfFileWriter object which represents a blank PDF document
    pdfWriter = PyPDF2.PdfFileWriter()

    # Loop through all the pagenumbers for the first document
    for pageNum in range(pdf1Reader.numPages):
        pageObj = pdf1Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    # Loop through all the pagenumbers for the second document
    for pageNum in range(pdf2Reader.numPages):
        pageObj = pdf2Reader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    # Now that you have copied all the pages in both the documents, write them into the a new document
    pdfOutputFile = open('MergedFiles.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)

    # Close all the files - Created as well as opened
    pdfOutputFile.close()
    pdf1File.close()
    pdf2File.close()


def close():
    x = messagebox.askquestion("askquestion", "Are you sure?")
    if x == 'yes':
        root.destroy()
    else:
        var = None


# Creating a button with more than one command using lambda
b1 = Button(bg="white", image=img1, command=w_to_p, borderwidth=5, relief=RIDGE)
b1.place(x=100, y=105)
b2 = Button(bg="white", image=img2, command=p_to_w, borderwidth=5, relief=RIDGE)
b2.place(x=100, y=250)
b3 = Button(bg="white", image=img4, borderwidth=5, relief=RIDGE)
b3.place(x=650, y=105)
b4 = Button(bg="white", image=img5, borderwidth=5, relief=RIDGE)
b4.place(x=650, y=250)
b5 = Button(bg="white", image=img6, command=merging, borderwidth=5, relief=RIDGE)
b5.place(x=100, y=400)
close = Button(bg="white", image=img3, command=close, borderwidth=5, relief=RIDGE)
close.place(x=670, y=450)

root.mainloop()
