import re
import os

def convert_full_script_to_tables(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into header and scenes
    parts = re.split(r'(## SCENE \d+.*)', content)
    
    final_output = [parts[0]] # Header info
    
    for i in range(1, len(parts), 2):
        scene_header = parts[i].strip()
        scene_content = parts[i+1]
        
        # Extract shots from scene_content
        # Shots look like:
        # 9
        # Muttagose
        # Image Prompt
        # Video Prompt
        # Dialogue (Optional)
        # —
        
        shots = []
        # Split by number at the start of a line
        shot_raws = re.split(r'\n(\d+)\n', scene_content)
        
        for j in range(1, len(shot_raws), 2):
            shot_num = shot_raws[j].strip()
            shot_data = shot_raws[j+1].strip()
            
            # Split shot_data into blocks by double newlines or single newlines
            # Then filter out the '—' separators
            blocks = [b.strip() for b in shot_data.split('\n') if b.strip() and b.strip() != '—' and b.strip() != '***']
            
            # The structure is usually:
            # 0: Characters (or —)
            # 1: Image Prompt
            # 2: Video Prompt
            # 3: Dialogue (Optional)
            
            char = "—"
            img = "—"
            vid = "—"
            dia = "—"
            
            if len(blocks) > 0:
                # Check if first block is characters or image prompt
                # Usually characters are short or match a list
                # If the block is very long, it might be the image prompt
                if len(blocks[0]) < 100:
                    char = blocks[0]
                    if len(blocks) > 1: img = blocks[1]
                    if len(blocks) > 2: vid = blocks[2]
                    if len(blocks) > 3: dia = blocks[3]
                else:
                    img = blocks[0]
                    if len(blocks) > 1: vid = blocks[1]
                    if len(blocks) > 2: dia = blocks[2]
            
            shots.append(f"| {shot_num} | {char} | {img} | {vid} | {dia} |")

        # Create Table
        table_md = f"\n{scene_header}\n\n| # | Characters | Image Prompt | Video Prompt | Dialogue |\n|---|---|---|---|---|\n"
        table_md += "\n".join(shots)
        table_md += "\n"
        
        final_output.append(table_md)

    # Add the Summary section if it exists
    summary_part = re.search(r'## Summary.*', content, re.DOTALL)
    if summary_part:
        final_output.append("\n" + summary_part.group(0))

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write("".join(final_output))

if __name__ == "__main__":
    path = r"c:\Users\acer\Documents\Github\Lessario\0shotss copy\01_Script_Department\02_Processed_Markdowns\E7_Shot_Prompts.md"
    convert_full_script_to_tables(path)
