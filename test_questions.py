# just define simple test questions (the question + possible answers)
# the questions are defined as a list in which we keep adding text.
# This program does not assume anything regarding the number of questions

answers = ["c", "d", "c", "b", "a", "d", "c", "c", "b", "b"]

# The questions are in a list
fp = open("questions.txt")
all_text = fp.read()


# define the questions list
questions = all_text.split("\n\n\n")

