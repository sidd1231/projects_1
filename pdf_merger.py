import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_combiner(Pdf_list):
    merger=PyPDF2.PdfFileMerger()
    for pdf in Pdf_list:
        print(pdf)
        merger.append(pdf)
        merger.write('super.pdf')


pdf_combiner(inputs)