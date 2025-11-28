print("------ PYTHON QUIZ APP ------")

questions = [
    {
        "question": "Which language is used for Data Science?",
        "options": ["1. Java", "2. Python", "3. C++", "4. HTML"],
        "answer": "2"
    },
    {
        "question": "What is the capital of India?",
        "options": ["1. Mumbai", "2. Kolkata", "3. New Delhi", "4. Chennai"],
        "answer": "3"
    },
    {
        "question": "Which company developed Python?",
        "options": ["1. Microsoft", "2. Apple", "3. Google", "4. None of these"],
        "answer": "4"
    },
    {
        "question": "HTML stands for?",
        "options": ["1. Hyper Text Markup Language", "2. HighText Machine Language", "3. Hyper Text Markdown Language", "4. None"],
        "answer": "1"
    }
]

score = 0

for q in questions:
    print("\n" + q["question"])
    for opt in q["options"]:
        print(opt)

    user_ans = input("Enter your option (1-4): ")

    if user_ans == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong answer.")

print("\n------ QUIZ COMPLETED ------")
print(f"Your Score: {score}/{len(questions)}")
