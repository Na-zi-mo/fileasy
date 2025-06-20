from PyPDF2 import PdfMerger # type: ignore

def merge(files):
    merger = PdfMerger() 
    for file in files:
        merger.append(file)
    merger.write("runs/result.pdf")
    merger.close()