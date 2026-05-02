import sys
import subprocess

# 1. Try to install PyMuPDF (fitz) if not present
try:
    import fitz
except ImportError:
    print("Installing PyMuPDF...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pymupdf"])
    import fitz

def convert_pdf_to_md(pdf_path, md_path):
    print(f"Opening {pdf_path}...")
    doc = fitz.open(pdf_path)
    full_text = ""
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        full_text += f"## Page {page_num + 1}\n\n"
        full_text += text + "\n\n---\n\n"
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(full_text)
    
    print(f"Success! Created {md_path}")

if __name__ == "__main__":
    pdf_file = "Singu - The Raja_E7_The Unstoppable Force (1).pdf"
    output_md = "E7_Script_From_PDF.md"
    convert_pdf_to_md(pdf_file, output_md)
