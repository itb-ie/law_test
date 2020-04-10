# This is to "hide" the correct answers into a different file
# The questions are defined into the questios.txt file
# We parse this file and construct a list of questions, plus I define a matching list of correct answers

# These are the correct answers
answers = ["c", "d", "c", "b", "a", "d", "c", "c", "b", "b"]

# The questions are in a file that we open and read from
fp = open("questions.txt")
all_text = fp.read()

# We parse the file and get the list of questions
questions = all_text.split("\n\n\n")

# Once we are done, we close the file
fp.close()

