import mammoth
import re

def clean_markdown(text):
    # 1. Remove anchor tags like <a id="..."></a>
    text = re.sub(r'<a id="[^"]+"></a>', '', text)
    
    # 2. Fix escaped characters like \( and \) and \- and \.
    text = text.replace('\\(', '(').replace('\\)', ')')
    text = text.replace('\\-', '-').replace('\\.', '.')
    text = text.replace('\\_', '_')
    
    # 3. Clean up double underscores used for bold (sometimes mammoth over-escapes)
    # text = text.replace('__', '**')
    
    # 4. Remove excessive empty lines (more than 2)
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    return text

input_file = "E7_Shot_Prompts.md.docx"
output_file = "E7_Shot_Prompts_Pure.md"

with open(input_file, "rb") as docx_file:
    # Convert docx to raw markdown using mammoth
    result = mammoth.convert_to_markdown(docx_file)
    markdown_content = result.value
    
    # Apply cleaning filters
    pure_markdown = clean_markdown(markdown_content)
    
    with open(output_file, "w", encoding="utf-8") as md_file:
        md_file.write(pure_markdown)

print(f"Successfully generated pure markdown: {output_file}")
