import random

question_dict = {}


def create(question, answer):

        question_dict[question] = answer
        print("Has been added")

def take():
    score = 0
    questions_list = list(question_dict.keys())
    random.shuffle(questions_list)
    for x in questions_list:
        userAnswer = input(x+":").lower()
        if userAnswer == question_dict[x]:
            score += 1
            print("Correct")
        else:
            print("Incorrect")
    print("Score:", score,"/",len(questions_list))

while True:
    take_create = input("Would you like to TAKE or CREATE a test(enter anything else to quit): ").lower()
    if take_create == "take":
        take()
        print("Thanks for taking the quiz")
    if take_create == "create":
        numberOfQues = int(input("How many questions do you want to add: "))
        for x in range(numberOfQues):
            question = input("Enter the question: ")
            answer = input("Enter the answer to the question: ").lower()
            create(question, answer)
    else:
        quit()



