from PyPDF2 import PdfMerger

merger = PdfMerger()
merger.append("lettre_de_motivationV2.pdf")
merger.append("Adda_Nazim_TCF.pdf")
merger.append("FMX_Nazim_Adda_contrat.pdf")
merger.write("lettre_explicative_Nazim_Adda.pdf")
merger.close()