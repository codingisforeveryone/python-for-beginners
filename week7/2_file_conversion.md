# Convert Word files to pdf and merge the files

## 📦 Step 1: Install Required Libraries
```
pip install docx2pdf 
pip install PyPDF2
```

## 🧑‍💻 Step 2: Program to Convert Text Files to PDF

Create a files convert_and_merge.py
```
import os
from docx2pdf import convert
from PyPDF2 import PdfMerger

# ===== SETTINGS =====
INPUT_FOLDER = r"C:\dev\python-for-beginners\week7\test_files"
OUTPUT_PDF = r"C:\dev\python-for-beginners\week7\test_files\final_merged.pdf"
TEMP_PDF_FOLDER = r"C:\dev\python-for-beginners\week7\test_files\tmp"

# ====================

os.makedirs(TEMP_PDF_FOLDER, exist_ok=True)

pdf_files = []

# Step 1: Convert Word files to PDF
for filename in os.listdir(INPUT_FOLDER):
    file_path = os.path.join(INPUT_FOLDER, filename)

    # Convert .docx to PDF
    if filename.lower().endswith(".docx"):
        pdf_name = filename.replace(".docx", ".pdf")
        pdf_path = os.path.join(TEMP_PDF_FOLDER, pdf_name)

        print(f"Converting: {filename}")
        convert(file_path, pdf_path)
        pdf_files.append(pdf_path)

    # Keep existing PDFs
    elif filename.lower().endswith(".pdf"):
        pdf_files.append(file_path)

# Step 2: Merge PDFs
merger = PdfMerger()

for pdf in sorted(pdf_files):
    print(f"Adding: {pdf}")
    merger.append(pdf)

merger.write(OUTPUT_PDF)
merger.close()

print("\n✅ Done!")
print(f"Merged PDF saved as:\n{OUTPUT_PDF}")
```
