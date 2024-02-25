import pdf_merge
import sys

if (len(sys.argv) < 3):
    print("Usage: merge-pdf front.pdf back.pdf [output.pdf]")
    exit()

front = sys.argv[1]
back = sys.argv[2]

output='pdf_out.pdf'

if (len(sys.argv) == 4):
    output = sys.argv[3]

def cli_main():
    pdf_merge.pdf_merge(front, back, output)
