import pypdf
import sys

pdflist = []

for name in sys.argv[1:]:
    pdflist.append(pypdf.PdfReader(name))


writer = pypdf.PdfWriter()
for pdf in pdflist:
    writer.append_pages_from_reader(pdf)

writer.write("out.pdf")
