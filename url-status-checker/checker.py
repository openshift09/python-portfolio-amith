import requests
import time

print("------ URL STATUS CHECKER ------")

def check_url(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=5)
        end = time.time()
        
        status = "UP" if response.status_code == 200 else "DOWN"
        
        return {
            "url": url,
            "status": status,
            "code": response.status_code,
            "time": round(end - start, 3)
        }
    except Exception as e:
        return {
            "url": url,
            "status": "DOWN",
            "code": "N/A",
            "time": "N/A"
        }

def main():
    with open("urls.txt", "r") as file:
        urls = [u.strip() for u in file.readlines()]

    print("\n--- CHECKING URLS ---\n")

    for url in urls:
        result = check_url(url)
        print(f"{result['url']} → {result['status']} (Code: {result['code']}, Time: {result['time']}s)")

main()
