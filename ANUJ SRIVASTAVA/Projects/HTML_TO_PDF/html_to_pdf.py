

#import pdfkit libraray
import pdfkit

#initialize the input and output file name
pdfkit.from_file('inputfile_name.html', 'output_file.pdf')

#If you want to downlaod from web url:

#import pdfkit
#pdfkit.from_url('https://url/','output_filename.pdf')
