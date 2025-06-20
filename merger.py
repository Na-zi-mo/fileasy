from PyPDF2 import PdfMerger # type: ignore

merger = PdfMerger()
merger.append("1.pdf")
merger.append("1.pdf")
merger.append("2.pdf")
merger.write("/runs/result.pdf")
merger.close()