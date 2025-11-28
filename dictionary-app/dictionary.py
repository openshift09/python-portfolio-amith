import requests

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

print("------ PYTHON DICTIONARY APP ------")

def get_meaning(word):
    try:
        response = requests.get(API_URL + word)
        data = response.json()

        if isinstance(data, dict) and data.get("title") == "No Definitions Found":
            print("❌ No meaning found for this word.")
            return

        meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
        example = data[0]["meanings"][0]["definitions"][0].get("example", "No example available.")
        part_of_speech = data[0]["meanings"][0]["partOfSpeech"]

        print("\n📘 WORD:", word)
        print("🔹 Part of Speech:", part_of_speech)
        print("📖 Meaning:", meaning)
        print("✏ Example:", example)
        print()
    except Exception as e:
        print("Something went wrong:", str(e))


while True:
    word = input("Enter a word (or 'exit' to quit): ").strip()

    if word.lower() == "exit":
        print("Goodbye!")
        break

    get_meaning(word)
