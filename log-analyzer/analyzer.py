import re

print("------ PYTHON LOG ANALYZER ------")

log_path = input("Enter path of log file: ")

try:
    with open(log_path, "r") as file:
        logs = file.readlines()

    error_count = 0
    warning_count = 0
    info_count = 0

    print("\n--- MATCHED LOGS ---\n")

    for line in logs:
        if "ERROR" in line:
            print("ERROR:", line.strip())
            error_count += 1
        elif "WARNING" in line:
            print("WARNING:", line.strip())
            warning_count += 1
        elif "INFO" in line:
            print("INFO:", line.strip())
            info_count += 1

    print("\n--- SUMMARY ---")
    print(f"Total ERROR lines: {error_count}")
    print(f"Total WARNING lines: {warning_count}")
    print(f"Total INFO lines: {info_count}")

except FileNotFoundError:
    print("Log file not found. Check the path and try again.")
