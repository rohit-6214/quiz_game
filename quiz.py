# quiz game by python programming

ask1 = input("Hey, want to play quiz with me..?\n")
if ask1.lower() in ["yes", "yeah"]:
    print("Let's play the game :) ")
else:
    print("It's okay, you can exit the quiz..!!")
    quit()

score = 0
total_questions = 5

# Questions and answers 
questions = {
    "What does HTTP stand for?": "Hyper Text Transfer Protocol",
    "What does SMTP stand for?": "Simple Mail Transfer Protocol",
    "What does CPU stand for?": "Central Processing Unit",
    "What does OS stand for?": "Operating System",
    "What does CU stand for?": "Control Unit"
}

for question, correct_answer in questions.items():
    user_answer = input(question + "\n")
    
    # Check if the user's answer matches the correct answer
    if user_answer.lower().strip() == correct_answer.lower():
        print("Correct Answer!")
        score += 1
        print("Your score is", score)
    else:
        print("Nope... Incorrect Answer.")
        print(f"The correct answer is: {correct_answer}")

# Calculate percentage and show final results
if score == total_questions:
    percentage = (score / total_questions) * 100
    print(f"Congratulations! You've answered all questions correctly.")
    print(f"Your score: {score}/{total_questions}")
    print(f"Your percentage: {percentage}%")
else:
    print(f"Your final score: {score}/{total_questions}")
    print(f"Your percentage: {(score / total_questions) * 100:.2f}%")
