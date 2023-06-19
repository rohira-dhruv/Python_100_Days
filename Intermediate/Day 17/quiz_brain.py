class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.questions_list = question_bank
        self.score = 0

    def next_question(self):
        """displays the question on the screen and checks the user's answer."""
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """returns whether there are more questions left in the question_list."""
        return self.question_number < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        """checks if user_answer is equal to the correct_answer or not and increments score accordingly."""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"The current score is: {self.score}/{self.question_number}\n")
