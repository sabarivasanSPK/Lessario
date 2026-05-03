import re
import os

def clean_markdown(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Remove Escaped Characters
    content = content.replace(r'\-', '-')
    content = content.replace(r'\(', '(')
    content = content.replace(r'\)', ')')
    content = content.replace(r'\.', '.')
    content = content.replace(r'\!', '!')
    content = content.replace(r'\#', '#')

    # 2. Convert __Bold__ to **Bold** (Standard Markdown)
    content = content.replace('__', '**')

    # 3. Remove HTML anchors in headers
    content = re.sub(r'<a id=".*?"></a>', '', content)

    # 4. Clean up the "Shot #" structure
    # This regex looks for patterns like:
    # **Shot #**
    # 
    # **Characters**
    # 
    # 1
    # 
    # It converts them into a more readable heading: ### Shot 1
    
    # Placeholder for more complex restructuring if needed
    # For now, let's just fix the basic formatting
    
    # Fix the weird "Shot #" headers to be inline or cleaner
    content = content.replace('**Shot #**', '### Shot')
    
    # Write the cleaned content back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Successfully cleaned: {file_path}")

if __name__ == "__main__":
    target_file = r"c:\Users\acer\Documents\Github\Lessario\0shotss copy\01_Script_Department\02_Processed_Markdowns\E7_Shot_Prompts.md"
    clean_markdown(target_file)
