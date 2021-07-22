import pdfkit 
# Save in the same folder
pdfkit.from_url('https://www.google.com/','html_to_pdf/sample.pdf')
# or 
# Save in the outer folder
# pdfkit.from_url('https://www.google.com/','sample.pdf') 


# If you want to add options

# import pdfkit
# options={
#    'page-size':'A4',#Letter
#     'margin-top':'0.75in',
#     'margin-right':'0.75in',
#     'margin-bottom':'0.75in',
#     'margin-left':'0.75in',
#     'encoding':"UTF-8",
#     'no-outline':None
# }    
# pdfkit.from_url('https://www.google.com/','out1.pdf', options=options)