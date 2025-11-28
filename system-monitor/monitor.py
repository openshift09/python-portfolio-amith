import psutil
import datetime
import time

print("------ SYSTEM MONITOR ------")

def get_uptime():
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time
    return str(uptime).split('.')[0]  # Remove microseconds

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    processes = len(psutil.pids())
    uptime = get_uptime()

    print("\nSYSTEM STATUS:")
    print(f"CPU Usage: {cpu}%")
    print(f"RAM Usage: {ram}%")
    print(f"Disk Usage: {disk}%")
    print(f"Running Processes: {processes}")
    print(f"System Uptime: {uptime}")

    time.sleep(2)   # Refresh every 2 seconds
