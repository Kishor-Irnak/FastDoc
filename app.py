import os
from tkinter import Tk, filedialog, Button, Label
from PIL import Image
from fpdf import FPDF

class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to PDF Converter")
        self.root.geometry("400x200")

        self.label_input = Label(root, text="Select Input Folder", width=40)
        self.label_input.pack(pady=10)

        self.button_input = Button(root, text="Browse Input Folder", command=self.select_input_folder)
        self.button_input.pack()

        self.label_output = Label(root, text="Select Output Folder", width=40)
        self.label_output.pack(pady=10)

        self.button_output = Button(root, text="Browse Output Folder", command=self.select_output_folder)
        self.button_output.pack()

        self.convert_button = Button(root, text="Convert Images to PDFs", command=self.convert_images_to_pdfs)
        self.convert_button.pack(pady=20)

        self.input_folder = ""
        self.output_folder = ""

    def select_input_folder(self):
        self.input_folder = filedialog.askdirectory(title="Select Input Folder")
        if self.input_folder:
            self.label_input.config(text=f"Input Folder: {self.input_folder}")

    def select_output_folder(self):
        self.output_folder = filedialog.askdirectory(title="Select Output Folder")
        if self.output_folder:
            self.label_output.config(text=f"Output Folder: {self.output_folder}")

    def convert_images_to_pdfs(self):
        if not self.input_folder or not self.output_folder:
            print("Both input and output folders must be selected!")
            return

        # Loop through all images in the input folder
        for image_filename in os.listdir(self.input_folder):
            image_path = os.path.join(self.input_folder, image_filename)
            if image_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                image = Image.open(image_path)
                image = image.convert("RGB")

                # Define PDF file name
                pdf_filename = os.path.splitext(image_filename)[0] + ".pdf"
                pdf_path = os.path.join(self.output_folder, pdf_filename)

                # Save the image as a PDF
                image.save(pdf_path, "PDF", resolution=100.0)
                print(f"Converted {image_filename} to {pdf_filename}")

        print("Conversion complete!")

# Create the main window (root)
root = Tk()
# Create the converter object
app = ImageToPDFConverter(root)
# Run the Tkinter event loop
root.mainloop()
