import sys
import subprocess

try:
    import mammoth
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "mammoth"])
    import mammoth

with open("E7_Shot_Prompts.md.docx", "rb") as docx_file:
    result = mammoth.convert_to_markdown(docx_file)
    with open("E7_Shot_Prompts.md", "w", encoding="utf-8") as md_file:
        md_file.write(result.value)
print("Successfully converted to E7_Shot_Prompts.md")
