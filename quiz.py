

#the start of the quiz and it gets the persons name 
def intro():
    name = input("What is your name ").capitalize().strip()
    print(f"Hello {name} this is a quiz about random things have fun")
    print("PS you need to answer in numbers")
    return name
#creating an object to make the code a lot smaller with the questions
def questions():
    class question():
        def __init__(self,question, question_possable_answers,correct_answer, correct_respons, incorrect_respons):
            self.question = question
            self.question_possable_answers = question_possable_answers
            self.correct_answer = correct_answer
            self.correct_respons = correct_respons
            self.incorrect_respons = incorrect_respons
# list of questions and all the stuff relating to it 
    questionList = [
        question("What is the fastest any man made craft has gone(so it has a person in side of it)", ["37,824 km/h","11.1km/s","383,947 Mph","3,692 Mph"],2,"Correct that is the answer it was achieved by the crew of Apollo 10","Incorrect the answer is 11.1km/s or  24,791mph or 39,897km/h this was done by the crew of apollo"),
        question("What element has the highest melting point", ["Tungsten","Lithium","Iron","Oganesson"],1,"Correct it has a melting point of 3,422 celises","Incorrect the element is Tungsten with a melting point of 3422 celises"),
        question("Who created the theory of relativity",["Isaac Newton","Galileo Galilei","Albert Einstein","Nikola Tesla"], 3,"Correct it Was Albert Einstein","Incorrect the answer is 3, Albert Einstein"),
        question("How big was Tsar Bomba originally going to be(in megatons)",["25 magatons","58 magatons","90 magatons","100 magatons","50 magatons"],4,"Correct the reason it was smaller was because of concerns over massive radioactive fallout and the high risk of not allowing the bomber crew enough time to escape the explosion.","Incorrect the answer is 100 magaton the reason it was smaller was because there was concerns over massive radioactive fallout and the high risk of not allowing the bomber crew enough time to escape the explosion."),
        question("True or False question\n eletrons are the smallest subatomic particle", ["True", "False"],2,"Correct the smallest subatomic particle is Quarks","Incorrect the smallest subatomic particle is Quarks"),
        question("What does sound travel faster in ",["Air","Water"],2,"Correct sound travels faster in water","Incorrect sound travels faster in water")

    ]
#the code to print out the question and check if it is correct
    score = 0
    for i in questionList:
        while True:
            print(f"{i.question}")
            for j , k in enumerate(i.question_possable_answers):
                print(f"{j + 1}.{k}")
            user_answer = input().strip()
            try:
                user_answer = int(user_answer)
                break
            except:
                print("invaild answer try again")
                continue
        if user_answer == i.correct_answer:
            print(f"{i.correct_respons}")
            score += 1
        else:
            print(f"{i.incorrect_respons}")
    return score

#the scoring system 
def finalscore(score,name):
    if score == 6:
        print(f"Your final score was {score} good job {name} you got a perfect score")
    elif score > 3 and score < 6:
        print(f"Your final score is {score} you did a good {name}")
    elif score <= 3 and score > 0:
        print(f"Your final score was {score} you did allright {name}")
    elif score == 0:
        print(f"Your final score was {score} you failed {name}")
    else:
        print(f"good job {name} you broke the scoring system ")
#the main def that holds all the code 
def main():
    while True:
        name = intro()
        score = questions()
        finalscore(score, name)
        startagain = input("do you want to start again Y/N").strip().upper()
        if startagain == 'Y':
            continue
        else:
            print("shuting down...")
            break
#calling the main code
main()