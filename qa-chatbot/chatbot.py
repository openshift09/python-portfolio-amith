import json

print("------ PYTHON Q&A CHATBOT ------")
print("Type 'exit' to quit.\n")

# Load knowledge base
with open("knowledge.json", "r") as file:
    knowledge = json.load(file)

def get_answer(user_input):
    user_input = user_input.lower()

    # Search for keywords from JSON
    for key in knowledge:
        if key in user_input:
            return knowledge[key]
    
    return "Sorry, I don't know the answer to that. Try another question."

while True:
    user = input("You: ")

    if user.lower() == "exit":
        print("Bot: Goodbye!")
        break

    reply = get_answer(user)
    print("Bot:", reply)
