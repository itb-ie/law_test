import sys
import os
import test_questions

def clear_screen():
    print(sys.platform)
    if sys.platform == "win32":
        os.system("cls")
    else:
        # we assume Mac since we do not support linux yet
        os.system("clear")


correct = 0
for i in range(10):
    clear_screen()
    print(test_questions.questions[i])
    answer = input("What is your answer? ")
    if answer == test_questions.answers[i]:
        correct += 1

print("your final score is: {}/10".format(correct))
