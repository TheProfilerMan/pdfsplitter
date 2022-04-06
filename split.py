import os
from pikepdf import Pdf

# a dictionary mapping PDF file to original PDF's page range
file2pages = {
    0: [0, 2071], # 1st split PDF file will contain the pages from start to one before end
    1: [2072, 4142], # 2nd split PDF file will contain the pages from start to one before end
    2: [4143, 6215], # 3rd split PDF file will contain the pages from start to one before end
}

# the target PDF document to split
filename = "orcs.pdf"

# load the PDF file
pdf = Pdf.open(filename)

# make the new splitted PDF files
new_pdf_files = [ Pdf.new() for i in file2pages ]

# the current pdf file index
new_pdf_index = 0

# iterate over all of the pages
for n, page in enumerate(pdf.pages):
    if n in list(range(*file2pages[new_pdf_index])):
        # add the `n` page to the `new_pdf_index` file
        new_pdf_files[new_pdf_index].pages.append(page)
        print(f"[*] Assigning Page {n} to the file {new_pdf_index}")
    else:
        # create a new fue namme by adding the pdf index
        name, ext = os.path.splitext(filename)
        output_filename = f"{name}-{new_pdf_index}.pdf"
        # save the output
        new_pdf_files[new_pdf_index].save(output_filename)
        print(f"[+] File: {output_filename} saved.")
        # next file
        new_pdf_index += 1
        # add the `n` page to the `new_pdf_index` file
        new_pdf_files[new_pdf_index].pages.append(page)
        print(f"[*] Assigning Page {n} to the file {new_pdf_index}")

# save the last file
name, ext = os.path.splitext(filename)
output_filename = f"{name}-{new_pdf_index}.pdf"
new_pdf_files[new_pdf_index].save(output_filename)
print(f"[+] File: {output_filename} saved.")
