# import sys and os just to be able to clear the screen between questions.
# sys to check the operating system and os to call the proper clear screen function
import sys
import os

# Import the test_questions in which we have the text of the questions and the answers
import test_questions


# This function will just clear the screen between each question
def clear_screen():
    print(sys.platform)
    if sys.platform == "win32":
        os.system("cls")
    else:
        # we assume Mac since we do not support linux yet
        os.system("clear")


# Count the correct number of answers
correct = 0
for i in range(10):
    clear_screen()
    print("What will the below code print?\nPlease choose the correct answer (type a,b,c or d)")
    print(test_questions.questions[i])
    answer = input("What is your answer? ")
    if answer == test_questions.answers[i]:
        correct += 1

print("your final score is: {}/{}".format(correct, len(test_questions.questions)))
