import os
import time

folder_path = "watch_folder"

previous_files = set(os.listdir(folder_path))

print("Monitoring started ....(Press CTRL + C to stop)")

while True:
      time.sleep(2)

      current_files = set(os.listdir(folder_path))

      created_files = current_files -previous_files
      deleted_files = previous_files - current_files

      for file in created_files:
          print(f"[CREATED] {file}")

      for file in deleted_files:
          print(f"[DELETED] {file}")

      previous_files = current_files

