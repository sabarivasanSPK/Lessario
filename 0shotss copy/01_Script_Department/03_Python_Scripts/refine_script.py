import re

def refine_markdown(input_path, output_path):
    print(f"Refining {input_path}...")
    
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    refined_lines = []
    
    for line in lines:
        # 1. Clean up whitespace
        clean_line = line.strip()
        
        # 2. Skip empty lines and Page markers
        if not clean_line or clean_line.startswith("## Page") or clean_line == "---":
            continue
            
        # 3. Detect Scene Headings
        if re.match(r"^SCENE \d+", clean_line, re.IGNORECASE):
            refined_lines.append(f"\n## {clean_line}\n")
            continue
            
        # 4. Detect Character Names (All caps, more than 2 chars)
        if clean_line.isupper() and len(clean_line) > 2 and not clean_line.startswith("SCENE"):
            refined_lines.append(f"\n**{clean_line}**")
            continue
            
        # 5. Normal Text (Action or Dialogue)
        refined_lines.append(clean_line)

    # Write the refined output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(refined_lines))
        
    print(f"Done! Clean script saved to: {output_path}")

if __name__ == "__main__":
    input_file = "E7_Script_Advanced.md"
    output_file = "E7_Script_Final_Clean.md"
    refine_markdown(input_file, output_file)
