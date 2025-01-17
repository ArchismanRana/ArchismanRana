from tkinter import *
import customtkinter as ctk
from tkinter import messagebox
import Multiple_Hand_Gesture_Control as Hand_Gesture
from tkinter import filedialog
import Object_Measurement as OM

root = ctk.CTk()
root.title("Object Measurer")
ctk.set_appearance_mode("System")
root.configure(fg_color="#7b2929")

root.geometry('570x550')  # Order is WidthXHeight
root.minsize(450, 550)  # Order is Width,Height
root.maxsize(743, 550)
root.configure(bg='brown')

# Animation
my_y = -70

file_path_var = StringVar()


# Animation Functions
def down():
    global my_y
    if my_y <= 10:
        my_y += 10
        Text_1.place(x=0, y=my_y)
        root.after(40, down)


Frame1 = ctk.CTkFrame(root, corner_radius=10)
Frame1.pack(padx=20, pady=20, fill="both", expand=True)
Frame2 = ctk.CTkFrame(master=Frame1, corner_radius=10, width=200, height=100, fg_color="white")
Frame2.pack(padx=10, pady=10, fill="both", expand=True)
Text_1 = ctk.CTkLabel(Frame2, text="Virtual Object Measuring Project", text_color="dark blue",
                      fg_color="#eeeeee", font=("Microsoft New Tai Lue", 30, "bold"),
                      corner_radius=8, padx=15, pady=15)
Text_1.place(x=0, y=my_y)
root.after(400, down)


def Hand_Cap():
    Hand_Gesture.start_webcam_measurement()


def measure_by_photo_upload():
    New_Win = ctk.CTkToplevel(root)  # TopLevel object which will be treated as a new window
    New_Win.title("Word to pdf")
    New_Win.geometry('800x350')  # Order is WidthXHeight
    New_Win.minsize(800, 400)
    New_Win.maxsize(1000, 600)
    New_Win.configure(fg_color='#b2baef')

    heading = ctk.CTkLabel(New_Win, text="Measure Dimensions Virtually",
                           text_color="dark blue", fg_color="white",
                           font=("Berlin Sans FB", 30))
    heading.pack(fill='x', pady='14')

    Description = ctk.CTkLabel(New_Win,
                               text="Upload the image of the object while keeping \nit on a white paper of dimension L:340mm and W:240mm",
                               text_color="dark blue",
                               font=("Berlin Sans FB", 30))
    Description.pack(padx='10', pady='14')

    def open_file():
        file = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")])
        if file:
            file_path_var.set(file)

    En = ctk.CTkEntry(New_Win, height=25, width=600, font=("helvetica", 20),
                      corner_radius=20, fg_color="white",
                      text_color="green", textvariable=file_path_var)
    En.place(x=100, y=170)

    browse_button = ctk.CTkButton(New_Win, text="Upload Image", fg_color="white", text_color='green',
                                  font=('Verdana', 25, 'bold'), width=12, height=12,
                                  hover_color="#f9cb9c", border_width=2, border_color="grey", command=open_file)
    browse_button.place(x=130, y=230)

    def measure_image():
        OM.photo_measurement(file_path_var.get())

    Measure_button = ctk.CTkButton(New_Win, text="Measure It", fg_color="white", text_color='red',
                                   font=('Verdana', 25, 'bold'), width=12, height=12,
                                   hover_color="#f9cb9c", border_width=2, border_color="grey",
                                   command=measure_image)
    Measure_button.place(x=130, y=300)


b1 = ctk.CTkButton(Frame2, text="Measure by photo upload", text_color="Black",
                   font=("Arial Rounded MT Bold", 32, "bold"), fg_color="#FCE0C0", corner_radius=10,
                   command=measure_by_photo_upload,
                   border_width=5, border_spacing=10, border_color="brown", hover_color="#f9cb9c")
b1.place(x=32, y=140)

b2 = ctk.CTkButton(Frame2, text="Measure by webcam", text_color="Black",
                   font=("Arial Rounded MT Bold", 32, "bold"), fg_color="#FCE0C0", corner_radius=10,
                   command=Hand_Cap,
                   border_width=5, border_spacing=10, border_color="brown", hover_color="#f9cb9c")
b2.place(x=60, y=220)


def close():
    x = messagebox.askquestion("askquestion", "Are you sure?")
    if x == 'yes':
        root.destroy()
    else:
        return None


close = ctk.CTkButton(Frame2, fg_color="#FCE0C0", text="Close", text_color="Black",
                      font=("Arial Rounded MT Bold", 20, "bold"), command=close,
                      border_width=5, border_spacing=10, border_color="black", hover_color="light grey")
close.place(x=170, y=340)
# Initialize animation when the program starts


root.mainloop()
