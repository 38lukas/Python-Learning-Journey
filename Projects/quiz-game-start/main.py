from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


if __name__ == "__main__":

    # setting up question bank
    question_bank = []

    for question in question_data:
        new_question = Question(question["text"], question["answer"])
        question_bank.append(new_question)

    # main logic
    quiz = QuizBrain(question_bank)

    while quiz.has_still_questions():
        quiz.nextQuestion()


