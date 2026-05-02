import os
import shutil

def organize_master_project():
    base_path = os.getcwd()
    print(f"Organizing Master Folder: {base_path}")

    # 1. Define the new structure
    structure = {
        "01_Scripts_and_Prompts": "Script document",
        "02_Character_Assets": "Animals Sheets",
        "99_Archive": ["not used", "New folder", "download-4", "untitled folder"]
    }

    # 2. Handle Scripts Folder
    if os.path.exists("Script document"):
        if not os.path.exists("01_Scripts_and_Prompts"):
            os.rename("Script document", "01_Scripts_and_Prompts")
            print("Renamed: Script document -> 01_Scripts_and_Prompts")
        else:
            print("Folder 01_Scripts_and_Prompts already exists.")

    # 3. Handle Character Assets Folder
    if os.path.exists("Animals Sheets"):
        if not os.path.exists("02_Character_Assets"):
            os.rename("Animals Sheets", "02_Character_Assets")
            print("Renamed: Animals Sheets -> 02_Character_Assets")
        else:
            print("Folder 02_Character_Assets already exists.")

    # 4. Handle Archive
    if not os.path.exists("99_Archive"):
        os.makedirs("99_Archive")
    
    for junk in structure["99_Archive"]:
        if os.path.exists(junk):
            shutil.move(junk, os.path.join("99_Archive", junk))
            print(f"Archived: {junk}")

    # 5. Create a Project Map
    map_content = """# Singu - The Raja Project Map

## 📁 [01_Scripts_and_Prompts](./01_Scripts_and_Prompts)
Contains all your scripts, Word docs, PDFs, and Markdown files. Use the `Fix_Episode7.bat` here to generate your prompts.

## 📁 [02_Character_Assets](./02_Character_Assets)
Reference sheets and poses for every character in the series.

## 📁 [epi7](./epi7)
Your active Shotcut project files and completed shots for Scene 1.

## 📁 [99_Archive](./99_Archive)
Old files and unused folders kept for safety.

---
*Note: If Shotcut asks for 'Missing Files', simply point it to the new '02_Character_Assets' folder!*
"""
    with open("PROJECT_MAP.md", "w", encoding="utf-8") as f:
        f.write(map_content)
    
    print("Created PROJECT_MAP.md")

if __name__ == "__main__":
    organize_master_project()
