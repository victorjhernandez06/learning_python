from PyPDF2 import PdfWriter, PdfReader
import getpass

pdf_writer = PdfWriter()
pdf_reader = PdfReader("Document.pdf")

for page_num in range(len(pdf_reader.pages)):
    pdf_writer.add_page(pdf_reader.pages[page_num])

password=getpass.getpass(prompt="Enter your Password: ")
print(password)
pdf_writer.encrypt(password)

with open("document-protected.pdf", "wb") as file:
    pdf_writer.write(file)

"""
Debes crear un entorno virtual al principio
## --> python -m virtualen venv
luego instalas el 
## --> pip install PyPDF2, 
con ello puedes importar PdfWriter, PdfReader



"""