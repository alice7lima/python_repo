import PyPDF2

import os

merger = PyPDF2.PdfMerger()

caminho = '/home/alice/automacoes_python/automacao_pdf/files'

lista_arquivos = os.listdir(caminho)

lista_arquivos.sort()
print(lista_arquivos)

for arquivo in lista_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"{caminho}/{arquivo}")

merger.write(f"{caminho}/pdf_merged.pdf")
