import os
from PIL import Image
from PyPDF2 import PdfFileMerger
import re
def combine_pdf(destination, file_names, pdf_name):
    # not really working so have to save saparate pdfs and resort to PyPDF lib
    # im1.save("myPDF", "PDF", save_all=True, append_images=img_list)
    pdf_names = []
    for name in file_names:
        im = Image.open(name)
        pdf_name = name[:-4] + ".pdf"
        im.save(pdf_name)
        pdf_names.append(pdf_name) # remove .png suffix
    # use PyPDF2 to merge all pages
    merger = PdfFileMerger()
    for pdf in pdf_names:
        merger.append(pdf)
    os.chdir(destination)
    merger.write(pdf_name)
    merger.close()
