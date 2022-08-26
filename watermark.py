import PyPDF2
from PyPDF2 import PdfFileReader

import sys

from PyPDF2 import merger
from PyPDF2.pdf import PdfFileWriter

input = sys.argv[1]
water_mark_file=sys.argv[2]

def pdf_marker(Pdf_list):
    input_pdf=PdfFileReader(input)
    watermark=PdfFileReader(water_mark_file).pages[0]


    # merger=PyPDF2.PdfFileMerger()
    for page in input_pdf.pages:
      merger=merger.PdfFileMerger(page)
      merger.add(watermark).render()

      writer =PdfFileWriter()
      writer.write(input.split('.pdf')[0]+'_w.pdf',input_pdf)

pdf_marker(input)