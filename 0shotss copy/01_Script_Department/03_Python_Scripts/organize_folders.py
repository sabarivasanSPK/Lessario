import os
import shutil

def organize_folder():
    base_path = os.getcwd()
    
    # Define target folders
    folders = {
        "01_Source_Documents": [".pdf", ".docx"],
        "02_Processed_Markdowns": [".md"],
        "03_Python_Scripts": [".py"],
        "04_Automation": [".bat"]
    }
    
    # Create folders if they don't exist
    for folder in folders:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")

    # List all files
    files = [f for f in os.listdir(base_path) if os.path.isfile(f)]
    
    for file in files:
        # Don't move the organization script itself!
        if file == "organize_folders.py":
            continue
            
        moved = False
        for folder, extensions in folders.items():
            if any(file.lower().endswith(ext) for ext in extensions):
                src = os.path.join(base_path, file)
                dst = os.path.join(base_path, folder, file)
                
                # Check for existing file to avoid errors
                if not os.path.exists(dst):
                    shutil.move(src, dst)
                    print(f"Moved: {file} -> {folder}")
                    moved = True
                    break
                else:
                    print(f"Skipped (already exists): {file}")
                    moved = True
                    break
        
        if not moved:
            print(f"Leaving in root: {file}")

if __name__ == "__main__":
    organize_folder()
