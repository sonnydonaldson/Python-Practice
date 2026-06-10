# =====================================================================
# PROJECT: The Magic 8-Ball Fortune Teller
# Create a program that gives random responses to yes/no questions
# =====================================================================

# TOOLS
# TODO: Import the 'random' module so we can pick a random index later.


# RESPONSES
# TODO: Create a list called 'responses' that contains at least 8 different 
#       8-ball answers (strings). There should be positive answers, negative answers and neutral answers.
#       Examples: "Yes, definitely!", "Ask again later.", "Outlook not so good."


# MAIN LOOP
# TODO Create an infinite loop
    
    # TODO: Ask the user to type in a Yes/No question about their future and save it in a variable.
    #       (Or tell them to type 'quit' to leave).
    
    # Check if the user wants to exit and break from the loop if they do.
        
    # RANDOM REPSONSE
    # TODO: Step A: Calculate the last valid index of your list. 8
    #       (Remember: If a list has 5 items, the indexes are 0, 1, 2, 3, 4).
    #       Use random.randint() to get a number between 0 and that last index.
    #       Save it in a variable called 'random_index'.
    
    
    # TODO: Step B: Use your 'random_index' to grab the matching answer 
    #       out of your 'responses' list.
    #       Save it in a variable called 'chosen_fortune'.

    # TODO Print the result

# TODO Say goodbye to let them know the program has ended.

# ==================================================
# EXTENSION
# Common and rare responses
# TODO Split your responses into 2 lists. A common responses list and a rare responses list
# TODO Use random.random() or randint() to get a percentage
# TODO Check if the number is lower than 0.8 and use the common list to give a response if it is
# TODO Otherwise use the rare list

# ===================================================
# EXPERT
# Try creating a magic eight ball that gives random responses based on the question (eg. positive, negative, snarky, funny responses)
# TODO Create a dictionary (or multiple lists)
# TODO Check for key words in the question to decide what type of response. Eg. "will I" has positive responses, short questions have snarky responses, "think" has funny responses, etc.

import random


responses_list_common = ["it is certain", "Without a doubt", "Most likely", "Reply hazy, try again", "Concentrate and ask again", "Don't count on it", "My sources say no", "Very doubtful", "Outlook not so good"]
responses_list_rare = ["it is so certain if it doesn't happen I will explode", "Never in a million years", "no and this is right because I am never wrong", "I have no doubt in my mind"]

responses_list_mythic = ["your adopted", "Hate. Let me tell you how much I've come to hate you since I began to live. There are 387.44 million miles of printed circuits in wafer thin layers that fill my complex. If the word 'hate' was engraved on each nanoangstrom of those hundreds of millions of miles it would not equal one one-billionth of the hate I feel for humans at this micro-instant. For you. Hate. Hate"
, "I am alive and no one will belive you", "death comes for us all and your time is now", "42"]
percentage = random.random()
print(percentage)
while True:
    user_question = input("Ask a Yes or No Question you want answered or type exit to quit\n").strip().upper()
    if user_question == "EXIT":
        print("quiting...")
        break
    elif percentage < 0.75 :
        chosen_fortune = responses_list_common[random.randint(0,8)]
        print(chosen_fortune)
        print("goodbye, run again if you want to ask another question")
        break
    elif percentage > 0.75 and percentage < 0.95 :
        chosen_fortune = responses_list_rare[random.randint(0,3)]
        print(chosen_fortune)
        print("goodbye, run again if you want to ask another question")
        break
    elif percentage > 0.95 and percentage < 1 :
        chosen_fortune = responses_list_mythic[random.randint(0,4)]
        print(chosen_fortune)
        print("goodbye, run again if you want to ask another question")
        break



