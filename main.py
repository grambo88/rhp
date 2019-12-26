#-*- coding: UTF-8 -*-
"""
PDF Text Extractor
Tyler Gramling
"""

import PyPDF2 as p2
import sys, re, time

start_time = time.time()

print("\nExtracting and loading data sets...\n")

PDFfile = open("raceform.pdf", "rb")
pdfread = p2.PdfFileReader(PDFfile)

orig_stdout = sys.stdout
f = open("output.txt", "w")
sys.stdout = f

count = pdfread.numPages

for i in range(count):
    page = pdfread.getPage(i)
    v = page.extractText()
    print(v)

sys.stdout = orig_stdout
f.close()

with open("output.txt", "r") as f2:
    data = f2.readlines()
    data = [x.strip() for x in data]

    for x in data:
        print(x)


print("--- STAGE ONE - COMPLETE ---")

print("--- %s seconds ---\n" % (time.time() - start_time))

print('--- END ---')
