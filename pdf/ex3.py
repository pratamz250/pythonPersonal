#Merge de pdfs
from pypdf import PdfMerger

merger = PdfMerger()

merger.append("a.pdf")
merger.append("b.pdf")
merger.append("c.pdf")

with open("merged.pdf", "wb") as f:
        merger.write(f)
