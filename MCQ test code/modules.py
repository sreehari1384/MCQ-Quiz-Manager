import json

class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option 

    def to_dict(self):
        return {
            'text': self.text,
            'options': self.options,
            'correct_option': self.correct_option
        }

    @staticmethod
    def from_dict(data):
        return Question(data['text'], data['options'], data['correct_option'])

class Quiz:
    def __init__(self, name, questions=None):
        self.name = name
        self.questions = questions if questions else []

    def add_question(self, question):
        self.questions.append(question)

    def to_dict(self):
        return {
            'name': self.name,
            'questions': [q.to_dict() for q in self.questions]
        }

    @staticmethod
    def from_dict(data):
        questions = [Question.from_dict(q) for q in data['questions']]
        return Quiz(data['name'], questions)

class QuizManager:
    def __init__(self, filename='quizzes.json'):
        self.filename = filename
        self.quizzes = self.load_quizzes()

    def load_quizzes(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Quiz.from_dict(q) for q in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_quizzes(self):
        with open(self.filename, 'w') as f:
            json.dump([q.to_dict() for q in self.quizzes], f, indent=2)

    def add_quiz(self, quiz):
        self.quizzes.append(quiz)
        self.save_quizzes()

    def get_quiz_names(self):
        return [q.name for q in self.quizzes]

    def get_quiz_by_name(self, name):
        for q in self.quizzes:
            if q.name == name:
                return q
        return None

    def update_quiz(self, quiz):
        for i, q in enumerate(self.quizzes):
            if q.name == quiz.name:
                self.quizzes[i] = quiz
                self.save_quizzes()
                return True
        return False
