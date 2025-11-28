import datetime

print("------ PYTHON CHATBOT ------")
print("Type 'exit' anytime to quit.\n")

def bot_reply(user):
    user = user.lower()

    if "hello" in user or "hi" in user:
        return "Hello! How can I help you today?"

    elif "your name" in user:
        return "I'm PyBot, your friendly Python chatbot!"

    elif "time" in user:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {now}"

    elif "date" in user:
        today = datetime.date.today().strftime("%B %d, %Y")
        return f"Today's date is {today}"

    elif "how are you" in user:
        return "I'm doing great! Thanks for asking."

    elif "bye" in user:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I didn't understand that. Try asking something else."

# Chat loop
while True:
    msg = input("You: ")

    if msg.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = bot_reply(msg)
    print("Bot:", response)
