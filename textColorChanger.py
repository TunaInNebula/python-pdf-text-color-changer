import fitz
from fpdf import FPDF
import tkinter as tk
from tkinter import filedialog
import time
from tkinter import ttk
from tkinter import HORIZONTAL


# interface
root = tk.Tk()
root.size()
input_label = tk.Label(text="bir dosya giriniz")
input_label.pack()


filename = filedialog.askopenfilename()
print('Selected:', filename)


def UploadAction(event=None):
    print('Selected:', filename)
    '''
    Progressbar = ttk.Progressbar()
    pb1 = Progressbar(root, orient=HORIZONTAL, length=100, mode='indeterminate')
    pb1.pack(expand=True)
    '''


button = tk.Button(root, text='Open', command=UploadAction)
button.pack()

root.mainloop()

# color change
def pdf_to_colored_text(input_pdf, output_pdf, color='#FF0000'):
    pdf_document = fitz.open(input_pdf)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_text_color(int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16))

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text")

        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 10, text.encode('latin-1', 'replace').decode('latin-1'))

    pdf.output(output_pdf)

def color_changer():
    input_pdf = filename
    output_pdf = "ikincideneme.pdf"
    pdf_to_colored_text(input_pdf, output_pdf)
    print(f"Metin rengi değiştirilmiş PDF dosyası {output_pdf} olarak kaydedildi.")

