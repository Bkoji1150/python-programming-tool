
import json
import sys

FILEPATH = "files/questions.json"


def read_file(FILEPATH):
    with open(FILEPATH) as file:
        content = file.read()
    return content


def read_json(JSONFILE):
    score = 0
    number = []
    questions = json.loads(JSONFILE)
    try:
        for question in questions:
            print(question['question_text'])
            for index, alternative in enumerate(question["alternatives"], 1):
                print(f"{index}.: {alternative}")
            number.append(index)
            user_choice = int(input("Enter Your answer: "))

            question["user_choice"] = user_choice
            if question["user_choice"] == question["correct_answer"]:
                score += 1
                result = f"Good job!, {question['correct_answer']} is the Correct Answer!"
            else:
                result = f"You are Wrong Answer!, {question['correct_answer']} is the right answer"
            print(result)
    except ValueError:
        print("Only numbers are allowed!")

    return score


data = read_file(FILEPATH)
score = read_json(data)


print(score,"/",len(json.loads(data)))
