# introduction to the quiz and getting there name 
INTRODUCTION = "This is a quiz about random stuff hope you like it"
player_name = input("What is your name ").capitalize()
print(f"hello {player_name}.")
print(f"{INTRODUCTION} \n")


# First question and getting their answer for it 
print(f"First question(this one is multiple choice)")
print("What is the fastest any man made craft has gone(so it has a person in side of it)\n A = 37,824 km/h \n B = 11.1km/s \n C = 383,947 Mph \n D = 3,692 mph")
first_question_answer = input()

# cheaking their answer is correct and printing the repily for if it is correct or incorrect

if first_question_answer in ("b", "B"):
    print("Correct that is the answer it was achieved by the crew of Apollo 10 \n")

if first_question_answer not in ("b", "B"):
    print("Incorrect the answer is 11.1km/s or  24,791mph or 39,897km/h this was done by the crew of apollo \n")



# second question and getting their answer for it
print("Second question")
second_question_answer = input("What element has the highest melting point")


# cheaking their answer is correct and printing the repily for if it is correct or incorrect

if second_question_answer in ("Tungsten", "tungsten"): 
    print("Correct it has a melting point of 3,422 celises \n")

if second_question_answer not in ("Tungsten", "tungsten"):
    print("Incorrect the element is Tungsten with a melting point of 3422 celises\n")


# third question and getting their answer for it

print("Third question(this one is multiple choice)")
print("Who created the theory of relativity\n A = Isaac Newton \n B = Galileo Galilei \n C = Albert Einstein \n D = Nikola Tesla")
third_question_answer = input()


# cheaking their answer is correct and printing the repily for if it is correct or incorrect

if third_question_answer in ("C", "c"):
    print("Correct it Was Albert Einstein")

if third_question_answer not in ("C", "c"):
    print("Incorrect the answer is C, Albert Einstein")
    

# fourth question and getting their answer for it 

print("fourth question(this one is multiple choice)")
print("How big was Tsar Bomba originally going to be(in megatons)\n A = 25 magatons B = 58 magatons C = 90 magatons D = 100 magaton E = 50 magatons")
fourth_question_answer = input()

# cheaking their answer is correct and printing the repily for if it is correct or incorrect


if fourth_question_answer in ("D", "d"):
    print("Correct the reason it was smaller was because of concerns over massive radioactive fallout and the high risk of not allowing the bomber crew enough time to escape the explosion.")

if fourth_question_answer not in ("D", "d"):
    print("Incorrect the answer is 100 magaton the reason it was smaller was because there was concerns over massive radioactive fallout and the high risk of not allowing the bomber crew enough time to escape the explosion.")


# fifth question and getting their answer for it 

print("Fifth question(true or false )")
fifth_question_answer = input("eletrons are the smallest subatomic particle")

#cheaking their answer is correct and printing the repily for if it is correct or incorrect

if fifth_question_answer in ("True", "true"):
    print("correct the smallest subatomic particle is Quarks")

if fifth_question_answer not in ("True", "true"):
    print("Incorrect the smallest subatomic particle is Quarks")


