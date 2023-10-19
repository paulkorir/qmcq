import json
import random
from jsonschema import validate, ValidationError


def validate_data(data, schema):
    try:
        validate(instance=json.loads(data), schema=schema)
        return True
    except ValidationError as e:
        print(f"Validation error: {e.message}")
        return False


def quiz(data, shuffle=True):
    questions = json.loads(data)["questions"]
    if shuffle:
        random.shuffle(questions)  # Shuffle the order of the questions
    score = 0

    for q in questions:
        print(q["question"])

        shuffled_options = q["options"].copy()
        if shuffle:
            random.shuffle(shuffled_options)  # Shuffle the options

        options_with_letters = list(zip(['A', 'B', 'C', 'D'], shuffled_options))

        for letter, option in options_with_letters:
            print(f"{letter}. {option}")

        answer = input("Your answer (A-D): ").upper()

        correct_option_letter = next(letter for letter, option in options_with_letters if option == q["answer"])

        if answer == correct_option_letter:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q['answer']}\n")

    print(f"Your final score is: {score}/{len(questions)}")


def load_json_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()
