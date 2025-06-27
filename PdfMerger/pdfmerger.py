import PyPDF2
import sys

userinput = sys.argv[1:]

def pdfmerger(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('Final.pdf')
pdfmerger(userinput)