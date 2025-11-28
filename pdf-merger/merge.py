import PyPDF2
import os

print("------ PDF MERGER ------")

def merge_pdfs(pdf_list, output_name):
    merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    merger.write(output_name)
    merger.close()
    print(f"\nPDFs merged successfully into: {output_name}")

# Ask user for folder path
folder_path = input("Enter folder path containing PDFs: ")

if not os.path.exists(folder_path):
    print("Invalid folder path.")
    exit()

pdf_files = [file for file in os.listdir(folder_path) if file.endswith(".pdf")]

if not pdf_files:
    print("No PDFs found in this folder.")
    exit()

print("\nPDF files found:")
for pdf in pdf_files:
    print(" -", pdf)

output = input("\nEnter output file name (e.g., merged.pdf): ")

merge_pdfs([os.path.join(folder_path, pdf) for pdf in pdf_files], output)
