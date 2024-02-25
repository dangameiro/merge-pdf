from PyPDF2 import PdfReader, PdfWriter
import sys

def pdf_merge (front, back, output='pdf_out.pdf'):
    front_pdf = PdfReader(front)
    back_pdf = PdfReader(back)
    output_pdf = PdfWriter()
    
    for i in range(len(front_pdf.pages)):
        output_pdf.add_page(front_pdf.pages[i])
        output_pdf.add_page(back_pdf.pages[-(i+1)])
    
    output_pdf.write(output)
    
if __name__ == '__main__':
    
    if (len(sys.argv) < 3):
        print("Usage: python pdf-merge.py front.pdf back.pdf [output.pdf]")
        
    front = sys.argv[1]
    back = sys.argv[2]
    
    if (len(sys.argv) == 4):
        output = sys.argv[3]
        pdf_merge(front, back, output)
    else:
        pdf_merge(front, back)
