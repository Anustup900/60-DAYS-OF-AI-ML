# -*- coding: utf-8 -*-
"""HTML to PDF.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nB1ew0Jra5OK30bL9QzNznxO-S7qxU8K
"""

#import pdfkit libraray
import pdfkit

#initialize the input and output file name
pdfkit.from_file('inputfile_name.html', 'output_file.pdf')

#If you want to downlaod from web url:

#import pdfkit
#pdfkit.from_url('https://url/','output_filename.pdf')