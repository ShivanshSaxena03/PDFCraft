# PDFCraft
📄 A collection of Python scripts for PDF rotation, merging, splitting, and text overlay. Handy tools for PDF manipulation tasks.

PDF MERGER:


A lightweight Python script that merges multiple PDF files into a single PDF using `PyPDF2`.

## 🚀 Features

- Merge any number of PDF files
- Order of merging follows the command-line input
- Outputs a single file: `Final.pdf`

## 🧰 Requirements

- Python 3
- `PyPDF2`

Install PyPDF2:

```bash
pip install PyPDF2

python merge.py file1.pdf file2.pdf file3.pdf

 PDF Page Rotator 🔄

A simple Python script to rotate the **first page** of a PDF file by 90 degrees and save the result to a new file.

## 📌 Features

- Rotates the **first page** of a PDF (clockwise)
- Outputs the rotated page as a new PDF (`tilt.pdf`)
- Uses `PyPDF2` for PDF manipulation

## 🔧 Requirements

- Python 3
- `PyPDF2`

Install using pip:

```bash
pip install PyPDF2

🚀 How to Use
Place your input file named hello_world.pdf in the same directory.

Run the script:

bash
Copy
Edit
python rotate_first_page.py

⚠️ Notes
Only the first page is rotated.

You can modify the script to rotate all pages or a specific range.

