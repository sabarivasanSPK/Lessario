import pdfplumber
import os

def convert_with_pdfplumber(pdf_path, output_md):
    print(f"Opening {pdf_path} with pdfplumber...")
    try:
        with pdfplumber.open(pdf_path) as pdf:
            full_text = ""
            for i, page in enumerate(pdf.pages):
                print(f"Processing Page {i+1}...")
                
                # Extract text with layout preservation
                text = page.extract_text(layout=True)
                
                if text:
                    full_text += f"## Page {i+1}\n\n"
                    full_text += text + "\n\n---\n\n"
                
        with open(output_md, "w", encoding="utf-8") as f:
            f.write(full_text)
            
        print(f"Success! Structured Markdown saved to: {output_md}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    pdf_file = "Singu - The Raja_E7_The Unstoppable Force (1).pdf"
    output_file = "E7_Script_Advanced.md"
    
    if os.path.exists(pdf_file):
        convert_with_pdfplumber(pdf_file, output_file)
    else:
        print(f"Error: Could not find {pdf_file}")
