### WHAT ANIMAL ARE YOU QUIZ ###

# FIRST, create a basic Flowchart using the FLowchart Shapes to plan the flow of your 'what animal are you' quiz. 
# __________________________

# Write a 'what animal are you' quiz. 
# You can base this on the picture from last lesson, but make it simpler - 
# 3 questions and 4 animals.


# Ask your user a question about themselves, giving them 2 options

# Check if they picked the first option

    # Ask the next question

    # Check if they picked the first option

        # Tell them they're animal 1

    # Otherwise

        # Tell them they're animal 2

# Otherwise

    # Ask the next question

    # Check if they picked the first option

        # Tell them they're animal 3

    # Otherwise

        # Tell them they're animal 4 

# __________________________

# EXTENSION
# Extend the quiz so there are 8 possible animals
# Create a Flowchart using the FLowchart Shapes to 

# __________________________

# EXTENSION 2
# Create a 'Which ??? are you?' Quiz
# This time allow all questions to have 4 possible answers (a,b,c and d) 
# and tally how many times they choose each
# Determine what they are at the end using the letter with the highest tally.
# Eg. If they picked mostly As, maybe they are Pikachu.
#making sure the varibles dont break 
second_question_answer = None
answerValid = False
print("this is an amimal test to see what animal you are")

#getting the first answer 
while answerValid == False:
    first_question_answer = input("first question\n Do you prefer to be with people or be alone ").upper().replace(" ", "")

    if first_question_answer in ["ALONE", "PEOPLE"]:
        answerValid = True

#responding to the first answera and giving you what animal you are for the first answer 
answerValid = False
if first_question_answer == "PEOPLE":
    while answerValid == False:
        second_question_answer = input("second question\nAre you are a leader ").upper().replace(" ","")

        if second_question_answer == "YES":
            print("You are a Lion")
            answerValid = True
        elif second_question_answer == "NO":
            print("You are a fish")
            answerValid = True

#responding to the first answera and giving you what animal you are for the second answer 

if first_question_answer == "ALONE":
    while answerValid == False:
        second_question_answer = input("second question\nAre you a night person or a day person ").upper().replace(" ","")

        if second_question_answer =="NIGHT":
            print("You are an Owl")
            answerValid = True
        elif second_question_answer == "DAY":
            print("You are an female cheetah")
            answerValid = True


      