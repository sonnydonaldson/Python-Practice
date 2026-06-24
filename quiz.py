"""
#varible to make sure they can't mess up and break the code
answer_vaild = False
score = 0 
# introduction to the quiz and getting there name 
INTRODUCTION = "This is a quiz about random stuff hope you like it and if it is a multpile choice answer in the upper case letters like A B C D. you will also be scored with you getting plues one with every question correct"
player_name = input("What is your name ").capitalize().strip()
print(f"hello {player_name}.")
print(f"{INTRODUCTION} \n")


# First question and getting their answer for it 

print(f"\n\nFirst question(this one is multiple choice)")
print("What is the fastest any man made craft has gone(so it has a person in side of it)\n A = 37,824 km/h \n B = 11.1km/s \n C = 383,947 Mph \n D = 3,692 mph")
question_answer = input().upper().strip()

# cheaking their answer is correct and printing the repily for if it is correct or incorrect

if question_answer in ("B", "11.1KM/S"):
    print("Correct that is the answer it was achieved by the crew of Apollo 10 \n")
    score +=1  
else:
    print("Incorrect the answer is 11.1km/s or  24,791mph or 39,897km/h this was done by the crew of apollo \n")



# second question and getting their answer for it
print("\n\nSecond question")
question_answer = input("What element has the highest melting point ").upper().strip()


# cheaking their answer is correct and printing the repily for if it is correct or incorrect

if question_answer in ("TUNGSTEN"): 
    print("Correct it has a melting point of 3,422 celises \n")
    score +=1  
else:
    print("Incorrect the element is Tungsten with a melting point of 3422 celises\n")


# third question and getting their answer for it

print("\n\nThird question(this one is multiple choice)")
print("Who created the theory of relativity\n A = Isaac Newton \n B = Galileo Galilei \n C = Albert Einstein \n D = Nikola Tesla")
question_answer = input().upper().strip()


# cheaking their answer is correct and printing the repily for if it is correct or incorrect

if question_answer in ("C", "ALBERT EINSTEIN" ):
    print("Correct it Was Albert Einstein")
    score +=1  
else:
    print("Incorrect the answer is C, Albert Einstein")
    

# fourth question and getting their answer for it 

print("\n\nfourth question(this one is multiple choice)")
print("How big was Tsar Bomba originally going to be(in megatons)\n A = 25 magatons B = 58 magatons C = 90 magatons D = 100 magatons E = 50 magatons")
question_answer = input().upper().strip()

# cheaking their answer is correct and printing the repily for if it is correct or incorrect


if question_answer in ("D", "100 MAGATONS", "100"):
    print("Correct the reason it was smaller was because of concerns over massive radioactive fallout and the high risk of not allowing the bomber crew enough time to escape the explosion.")
    score +=1  
else:
    print("Incorrect the answer is 100 magaton the reason it was smaller was because there was concerns over massive radioactive fallout and the high risk of not allowing the bomber crew enough time to escape the explosion.")


# fifth question and getting their answer for it 

print("\n\nFifth question(true or false )")
question_answer = input("eletrons are the smallest subatomic particle ").upper().strip()

#cheaking their answer is correct and printing the repily for if it is correct or incorrect

if question_answer in ("FALSE", "QUARKAS "):
    print("correct the smallest subatomic particle is Quarks")
    score +=1  
else:
    print("Incorrect the smallest subatomic particle is Quarks")

#sixth question and getting their answer for it 

print("\n\nSixth Question")
question_answer = input("What does sound travel faster in air or water ").upper().strip()


#cheaking their answer is correct and printing the repily for if it is correct or incorrect

if question_answer in ("WATER"):
    print("Correct sound travels faster in water")
    score +=1  
else:
    print("Incorrect sound travels faster in water")

print(f"your final score was {score}")
"""
KEY_QUESTION = "KEY_QUESTIONS"
KEY_ANSWER = "KEY_ANSWER"
KEY_CORRECT_RESPONS = "KEY_CORRECT_RESPONS"
KEY_INCORRECT_RESPONS = "KEY_INCORRECT_RESPONS"
KEY_POSSABLE_ANSWERS = "KEY_POSSABLE_ANSWERS"

quiz_questions = [
    {KEY_QUESTION: "What is the fastest any man made craft has gone(so it has a person in side of it)", KEY_POSSABLE_ANSWERS:["37,824 km/h","11.1km/s","383,947 Mph", "3,692 mph" ],KEY_ANSWER: ""}
    ]



def intro():
    name = input("what is your name")
    print(f"hello {name} this is a quiz about random things have fun")
    return name

class question():
    def __init__(self,question, question_possable_answers,correct_answer, correct_respons, incorrect_respons):
        self.question = question
        self.question_possable_answers = question_possable_answers
        self.correct_answer = correct_answer
        self.correct_respons = correct_respons
        self.incorrect_respons = incorrect_respons

questions = [
    question("What is the fastest any man made craft has gone(so it has a person in side of it)", ["37,824 km/h","11.1km/s","383,947 Mph","3,692 mph"],)
question1 = question()
while True:
    print(f"{question1.question}")
    for i , j in enumerate(question1.question_possable_answers):
        print(f"{i + 1} {j}")
        user_answer = input()
    try:
        user_answer = int(user_answer)
        break
    except:
        print("invaild answer try again")
        continue
if user_answer == question1.correct_answer:
    print(f"{question1.correct_respons}")
else:
    print(f"{question1.incorrect_respons}")







