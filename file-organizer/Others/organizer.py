import os
import shutil

# Extensions grouped by category
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z", ".tar"],
}

def organize_folder(path):
    if not os.path.exists(path):
        print("Invalid folder path.")
        return
    
    files = os.listdir(path)
    print(f"\nOrganizing files in: {path}")

    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isdir(file_path):
            continue  # Skip folders

        file_ext = os.path.splitext(file)[1].lower()
        moved = False

        # Categorize file
        for folder, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                target_folder = os.path.join(path, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, file))
                print(f"Moved: {file} → {folder}/")
                moved = True
                break

        # If no matching category
        if not moved:
            other_folder = os.path.join(path, "Others")
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(other_folder, file))
            print(f"Moved: {file} → Others/")

    print("\nOrganization Complete!")


print("------ FILE ORGANIZER ------")
folder = input("Enter the path of the folder to organize: ")

organize_folder(folder)
