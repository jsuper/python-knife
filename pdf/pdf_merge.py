# coding:utf-8
# 合并多个pdf文件为一个
from PyPDF2 import PdfFileReader as reader,PdfFileWriter as writer
import os

def main():
    base_path = "需要合并的pdf文件目录路径"
    pdf_part = []
    total_pages = 0
    for f in os.listdir(base_path):
        print(f)
        pdf = reader(base_path+"/"+f)
        pdf_part.append(pdf)
        total_pages = total_pages+pdf.getNumPages()

    merged_pdf = writer()
    page_idx = 0 
    for pdf in pdf_part:
        for idx in range(pdf.getNumPages()):
            merged_pdf.insertPage(pdf.getPage(idx),page_idx)
            page_idx+=1

    with open(base_path+"/merged.pdf",'wb') as pdf_file:
        merged_pdf.write(pdf_file)

if __name__ == "__main__":
    main()