import requests

API_URL = "https://tinyurl.com/api-create.php"

def shorten_url(long_url):
    try:
        response = requests.get(API_URL, params={"url": long_url})
        if response.status_code == 200:
            return response.text
        else:
            return "Error: Unable to shorten URL"
    except Exception as e:
        return f"Something went wrong: {str(e)}"

print("------ URL SHORTENER ------")

while True:
    url = input("Enter a URL to shorten (or 'exit' to quit): ")

    if url.lower() == "exit":
        print("Goodbye!")
        break

    short = shorten_url(url)
    print("Shortened URL:", short, "\n")
