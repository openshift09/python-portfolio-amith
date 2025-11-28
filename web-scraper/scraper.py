import requests
from bs4 import BeautifulSoup

print("------ PYTHON WEB SCRAPER ------")

URL = "https://news.ycombinator.com"

try:
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("a", class_="storylink")

    print("\nTOP HEADLINES:\n")
    for i, headline in enumerate(headlines[:10], start=1):
        print(f"{i}. {headline.text}")
        print("   Link:", headline["href"])
        print()

except Exception as e:
    print("Error scraping website:", e)
