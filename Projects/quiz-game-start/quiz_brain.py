class QuizBrain:

    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list

    def has_still_questions(self):
        if self.question_number < 12:
            return True

    def nextQuestion(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}  (True/False): ")