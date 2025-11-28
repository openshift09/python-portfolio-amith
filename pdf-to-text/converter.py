import PyPDF2

print("------ PDF TO TEXT CONVERTER ------")

pdf_path = input("Enter the PDF file path: ")
output = input("Enter output text file name (e.g., output.txt): ")

try:
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page in reader.pages:
            text += page.extract_text() + "\n"

    with open(output, "w", encoding="utf-8") as out:
        out.write(text)

    print(f"\nText extracted and saved as {output}")

except FileNotFoundError:
    print("PDF file not found.")
except Exception as e:
    print("Error:", e)
