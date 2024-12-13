class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def add_question(self, question, options, correct_option):
        self.questions.append({
            "question": question,
            "options": options,
            "correct_option": correct_option
        })

    def start(self):
        print("Welcome to the Quiz!\n")
        for idx, question in enumerate(self.questions, 1):
            print(f"Question {idx}: {question['question']}")
            for i, option in enumerate(question['options'], 1):
                print(f"  {i}. {option}")
            
            while True:
                try:
                    answer = int(input("Your answer (choose the number): "))
                    if 1 <= answer <= len(question['options']):
                        break
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Please enter a number.")

            if question['options'][answer - 1] == question['correct_option']:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was: {question['correct_option']}\n")

        print(f"Quiz finished! Your score: {self.score}/{len(self.questions)}")

# Example usage
quiz = Quiz()

# Add questions to the quiz
quiz.add_question(
    "What is the best machine learning language?",
    ["Java Programming Language", "Python Programming Language", "C++ Programming Language ", "Scala Programming Language"],
    "Python Programming Language"
)

quiz.add_question(
    "What does VBA mean?",
    ["Visual Basic for Applications", "Visual By Arithmetic", "Visual Basic Answers", "Visual By Algorithms"],
    "Visual Basic for Applications"
)

quiz.add_question(
    "Which programming language is this quiz written in?",
    ["Python", "Java", "C++", "Ruby"],
    "Python"
)
quiz.add_question(
    "What is a variable in Python?",
    ["A reserved word", "A data type", "A location in memory to store data", "A function"],
    "A location in memory to store data"
)
quiz.add_question(
    "How do you declare a variable in Python?",
    ["x = 4", "var x", "x = variable", "declare x"],
    "x = 4"
)

# Start the quiz
quiz.start()

print("\nProject Developed by:-------Shamila Naz, Saliha and Ruqayya--------")
