with open("logs/sample.log","r") as file:
    lines =file.readlines()

info_count = 0
warning_count = 0
error_count = 0

for line in lines:
    if "ERROR" in line:
        error_count += 1
    elif "WARNING" in line:
        warning_count += 1
    elif "INFO" in line:
        info_count += 1

print("Log Analysis Summary")
print("---------------------")
print(f"INFO messages: {info_count}")
print(f"WARNING messages: {warning_count}")
print(f"ERROR messages: {error_count}")
