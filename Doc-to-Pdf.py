from tkinter import Tk, filedialog, Button, Label
from docx2pdf import convert
from PIL import Image, ImageTk


def select_file():
    # Create a Tkinter root window
    root = Tk()
    root.withdraw()

    # Open a file dialog to select the DOC file
    file_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])

    if file_path:
        convert_to_pdf(file_path)


def convert_to_pdf(doc_file):
    # Update UI to show conversion in progress
    status_label.config(text="Converting...", fg="blue")
    root.update()

    try:
        # Convert the DOC file to PDF
        convert(doc_file)

        # Update UI to show conversion completion
        status_label.config(text="Conversion complete!", fg="green")
    except Exception as e:
        # Update UI to show conversion failure
        status_label.config(text="Conversion failed.", fg="red")
        print("Conversion error:", e)


def load_image(image_path):
    # Load and resize the image
    image = Image.open(image_path)
    image = Image.resize((150, 150), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)

    # Create a label to display the image
    img_label = Label(root, image=img)
    img_label.image = img
    img_label.pack()


# Create a Tkinter root window
root = Tk()
root.title("DOC to PDF Converter")

# Load and display an image
#load_image("D:\PyCharm\New PyCharm\My projects\coversion_icon.png")

# Create a label for the status
status_label = Label(root, text="Select a DOC file to convert", fg="black", font=("Arial", 12, "bold"))
status_label.pack(pady=10)

# Create a button to select the DOC file
select_button = Button(root, text="Select DOC file", command=select_file, font=("Arial", 12, "bold"), padx=20, pady=10)
select_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
