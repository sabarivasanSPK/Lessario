import os
import shutil
import re

def studio_restructure():
    base_path = os.getcwd()
    print(f"🚀 Initializing Studio Restructure in: {base_path}")

    # 1. Define Department Folders
    departments = [
        "00_Production_Office",
        "01_Script_Department",
        "02_Art_Department",
        "03_Film_Studio",
        "04_Tech_Lab"
    ]

    for dept in departments:
        if not os.path.exists(dept):
            os.makedirs(dept)

    # 2. Sort Python & Batch Files (Tech Lab)
    for file in os.listdir(base_path):
        if file.endswith(".py") and file != "studio_restructure.py":
            shutil.move(file, os.path.join("04_Tech_Lab", file))
            print(f"Tech Lab: {file}")
        elif file.endswith(".bat"):
            shutil.move(file, os.path.join("04_Tech_Lab", file))
            print(f"Tech Lab: {file}")

    # 3. Handle Art Department (Move Character Assets)
    art_source = "02_Character_Assets" if os.path.exists("02_Character_Assets") else "Animals Sheets"
    if os.path.exists(art_source):
        # We move the contents of the folder into the new Art Dept
        shutil.move(art_source, os.path.join("02_Art_Department", "Characters"))
        print(f"Art Dept: Characters moved.")

    # 4. Handle Script Department (Smart Sorting)
    script_source = "01_Scripts_and_Prompts" if os.path.exists("01_Scripts_and_Prompts") else "Script document"
    if os.path.exists(script_source):
        for item in os.listdir(script_source):
            src_path = os.path.join(script_source, item)
            
            # Detect Episode Number (E1, E7, Episode 4, etc.)
            match = re.search(r"[eE]pisode[ _]?(\d+)|[eE](\d+)", item)
            if match:
                ep_num = match.group(1) or match.group(2)
                ep_folder = os.path.join("01_Script_Department", f"Episode_{int(ep_num):02d}")
                if not os.path.exists(ep_folder): os.makedirs(ep_folder)
                shutil.move(src_path, os.path.join(ep_folder, item))
                print(f"Script Dept: {item} -> {ep_folder}")
            else:
                shutil.move(src_path, os.path.join("01_Script_Department", item))

        # Remove old empty folder
        os.rmdir(script_source)

    # 5. Handle Film Studio (Episode 7 Project)
    if os.path.exists("epi7"):
        target = os.path.join("03_Film_Studio", "Episode_07")
        shutil.move("epi7", target)
        print("Film Studio: Episode 7 project moved.")
    
    if os.path.exists("epi7.mp4"):
        shutil.move("epi7.mp4", os.path.join("03_Film_Studio", "Episode_07", "epi7_render.mp4"))

    # 6. Final Dashboard
    with open("00_Production_Office/DASHBOARD.md", "w", encoding="utf-8") as f:
        f.write("# STUDIO DASHBOARD\n\n"
                "### 🎥 Active Project: Episode 07\n"
                "- Scripts: [01_Script_Department/Episode_07/]\n"
                "- Video: [03_Film_Studio/Episode_07/]\n\n"
                "### 🛠️ Developer Tools\n"
                "- All automation scripts are in [04_Tech_Lab/]\n")

    print("\n✅ Restructure Complete! Your studio is now organized by department.")

if __name__ == "__main__":
    studio_restructure()
