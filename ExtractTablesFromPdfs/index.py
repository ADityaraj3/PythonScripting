from PyPDF2 import PdfReader
import os


print(os.getcwd())
current_directory = os.getcwd()

# Use a relative path to 'foo.pdf'
pdf_file_path = os.path.join(current_directory, 'PythonScripting','ExtractTablesFromPdfs', 'foo.pdf')

try:
    # Create a PdfReader object to read the PDF file
    pdf_reader = PdfReader(pdf_file_path)

    # Access PDF properties and methods using pdf_reader
    num_pages = len(pdf_reader.pages)
    print(f"Number of pages in the PDF: {num_pages}")

    # You can also access individual pages like this:
    # first_page = pdf_reader.pages[0]
    
except FileNotFoundError:
    print(f"File '{pdf_file_path}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

