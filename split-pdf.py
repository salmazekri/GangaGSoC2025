from PyPDF2 import PdfReader, PdfWriter
import sys
import os

def split_pdf(input_file):
    # Get the directory of the input file
    output_dir = os.path.dirname(os.path.abspath(input_file))
    base_name = os.path.splitext(os.path.basename(input_file))[0]

    try:
        with open(input_file, "rb") as file:
            inputpdf = PdfReader(file)
            
            for i in range(len(inputpdf.pages)):
                output = PdfWriter()
                output.add_page(inputpdf.pages[i])
                
                # Create output path in same directory as input file
                output_path = os.path.join(output_dir, f"{base_name}_page_{i+1}.pdf")
                with open(output_path, "wb") as outputStream:
                    output.write(outputStream)
                print(f"Created: {output_path}")
            
            return output_dir

    except Exception as e:
        print(f"Error processing PDF: {str(e)}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python split-pdf.py <input_pdf_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found")
        sys.exit(1)
    
    output_dir = split_pdf(input_file)
    if output_dir:
        print(f"PDF splitting completed! Files saved in: {output_dir}")
    else:
        print("PDF splitting failed!")
        sys.exit(1)