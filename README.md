# PDF Data Extraction Tool

This Python script extracts data from PDF files and stores it in an Excel spreadsheet. It is designed to process PDF documents and extract information such as document type, date, postcode, and correctness.

## Usage

1. **Installation**:
   - Make sure you have Python installed.
   - Install the required Python packages by running the following commands:

pip install pdfplumber
pip install openpyxl

2. **Configuration**:
- Set the `pdf_folder` variable to the directory containing the PDF files you want to process.
- Set the `excel_file` variable to the path where you want to save the output Excel file.

3. **Run the Script**:
- Execute the script by running `python your_script_name.py` in your terminal.
- The script will process all PDF files in the specified folder and extract relevant information.

4. **Output**:
- The extracted data will be saved in an Excel file (`output.xlsx`) with columns for document name, type, date, postcode, and type.
- If the script can't find specific information in a PDF file, it will label it as "ERROR" in the Excel file.

## Customization

- You can customize the document type detection logic by modifying the code section that checks for keywords in the PDF text.
- Adjust regular expressions or text patterns to match the format of the dates and postcodes you want to extract from your PDF files.

## Dependencies

- [pdfplumber](https://github.com/jsvine/pdfplumber): A PDF text extraction library.
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/): A library for working with Excel files in Python.

## Sample PDFs

Before running the script, it's a good idea to examine your PDF files with the `initial_pdf_reader` utility to understand the structure and text content of the PDFs you're processing.


Feel free to reach out if you have any questions or need assistance with this project.
