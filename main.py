from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for QA in question_data:
    question = Question(QA["text"], QA["answer"])
    question_bank.append(question)

quiz = QuizBrain(q_list=question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz!")
print(f"Your final score was: {quiz.score}/{len(quiz.question_list)}")
