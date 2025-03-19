from PyPDF2 import PdfReader, PdfWriter
import sys
import os

def split_pdf(input_file):
    output_dir = "split_pages"
    os.makedirs(output_dir, exist_ok=True)

    with open(input_file, "rb") as file:
        inputpdf = PdfReader(file)
        
        for i in range(len(inputpdf.pages)):
            output = PdfWriter()
            output.add_page(inputpdf.pages[i])
            
            output_path = os.path.join(output_dir, f"page_{i+1}.pdf")
            with open(output_path, "wb") as outputStream:
                output.write(outputStream)
            print(f"Created: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python split-pdf.py <input_pdf_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found")
        sys.exit(1)
        
    split_pdf(input_file)
    print("PDF splitting completed!")