import pdfplumber


#path to .pdf file

pdf_file = r""

with pdfplumber.open(pdf_file) as pdf:
    
    first_page = pdf.pages[0]  #Only using first page in my instance
    text = first_page.extract_text() 
    print(text)

    #prints all pdf text to be initally analysed