def administer_quiz(questions):
    correct_answers = 0
    incorrect_answers = 0
    wrong_answers = []

    for question_data in questions:
        question = question_data["question"]
        correct_answer = question_data["answer"]

        user_answer = input(f"{question}: ").strip()

        if user_answer.lower() == correct_answer.lower():
            correct_answers += 1
        else:
            incorrect_answers += 1
            wrong_answers.append({"question": question, "user_answer": user_answer, "correct_answer": correct_answer})

    return correct_answers, incorrect_answers, wrong_answers


def inform_user_performance(correct_answers, incorrect_answers, wrong_answers):
    print("\n***** Quiz Results *****")
    print(f"Correct Answers: {correct_answers}")
    print(f"Incorrect Answers: {incorrect_answers}")

    if incorrect_answers > 0:
        print("\n***** Incorrectly Answered Questions *****")
        for idx, wrong_answer in enumerate(wrong_answers, 1):
            print(f"{idx}. Question: {wrong_answer['question']}")
            print(f"   Your Answer: {wrong_answer['user_answer']}")
            print(f"   Correct Answer: {wrong_answer['correct_answer']}\n")

    if incorrect_answers > 3:
        print("You had more than 3 wrong answers. Please play again to improve your score.")


if __name__ == "__main__":
    data = [
        {
            "question": "What is Baby Yoda's real name?",
            "answer": "Grogu"
        },
        {
            "question": "Where did Obi-Wan take Luke after his birth?",
            "answer": "Tatooine"
        },
        {
            "question": "What year did the first Star Wars movie come out?",
            "answer": "1977"
        },
        {
            "question": "Who built C-3PO?",
            "answer": "Anakin Skywalker"
        },
        {
            "question": "Anakin Skywalker grew up to be who?",
            "answer": "Darth Vader"
        },
        {
            "question": "What species is Chewbacca?",
            "answer": "Wookiee"
        }
    ]

    # Administer the quiz and get results
    correct_count, incorrect_count, wrong_answers_list = administer_quiz(data)

    # Inform the user about their performance
    inform_user_performance(correct_count, incorrect_count, wrong_answers_list)
