
from modules import QuizManager, Quiz, Question

def main_menu():
    manager = QuizManager()
    while True:
        print("1. Create Test")
        print("2. Existing Tests")
        print("3. Modify Test")
        print("4. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            create_test(manager)
        elif choice == '2':
            take_test(manager)
        elif choice == '3':
            modify_test(manager)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

def create_test(manager):
    name = input("Enter quiz name: ")
    quiz = Quiz(name)
    while True:
        text = input("Enter question (or 'done' to finish): ")
        if text.lower() == 'done':
            break
        options = []
        for i in range(4):
            opt = input(f"Enter option {i+1}: ")
            options.append(opt)
        correct = int(input("Enter correct option number (1-4): ")) - 1
        quiz.add_question(Question(text, options, correct))
    manager.add_quiz(quiz)
    print(f"Quiz '{name}' created!")

def take_test(manager):
    quizzes = manager.get_quiz_names()
    if not quizzes:
        print("No quizzes available.")
        return
    print("\nAvailable Quizzes:")
    for idx, name in enumerate(quizzes):
        print(f"{idx+1}. {name}")
    sel = int(input("Select quiz number: ")) - 1
    quiz = manager.get_quiz_by_name(quizzes[sel])
    score = 0
    for i, q in enumerate(quiz.questions):
        print(f"\nQ{i+1}: {q.text}")
        for j, opt in enumerate(q.options):
            print(f"  {j+1}. {opt}")
        ans = int(input("Your answer (1-4): ")) - 1
        if ans == q.correct_option:
            score += 1
    print(f"\nResult: {score}/{len(quiz.questions)} correct!")

def modify_test(manager):
    quizzes = manager.get_quiz_names()
    if not quizzes:
        print("No quizzes to modify.")
        return
    print("\nAvailable Quizzes:")
    for idx, name in enumerate(quizzes):
        print(f"{idx+1}. {name}")
    sel = int(input("Select quiz number to modify: ")) - 1
    quiz = manager.get_quiz_by_name(quizzes[sel])
    for i, q in enumerate(quiz.questions):
        print(f"\nQ{i+1}: {q.text}")
        for j, opt in enumerate(q.options):
            print(f"  {j+1}. {opt}")
        ch = input("Modify this question? (y/n): ")
        if ch.lower() == 'y':
            new_text = input("Enter new question text: ")
            new_options = []
            for k in range(4):
                new_opt = input(f"Enter new option {k+1}: ")
                new_options.append(new_opt)
            new_correct = int(input("Enter new correct option number (1-4): ")) - 1
            quiz.questions[i] = Question(new_text, new_options, new_correct)
    manager.update_quiz(quiz)
    print("Quiz updated!")

if __name__ == "__main__":
    main_menu()
