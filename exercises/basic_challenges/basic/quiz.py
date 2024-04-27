def quiz():
    questions = {
        "Who is the president of the United States?": "Joe Biden",
        "What is the capital of France?": "Paris",
        "What is the largest mammal in the world?": "Blue whale"
    }

    score = 0

    for question, answer in questions.items():
        user_answer = input(question + " ").strip().lower()
        if user_answer == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The correct answer is:", answer)

    print("You scored {}/{}.".format(score, len(questions)))


quiz()
