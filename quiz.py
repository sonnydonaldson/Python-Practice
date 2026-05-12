# introduction to the quiz and getting there name 
INTRODUCTION = "This is a quiz about random stuff hope you like it"
player_name = input("What is your name ").capitalize()
print("hello " + player_name)
print(INTRODUCTION)


# First question and getting their answer for it 
print("First question")
first_question_answer = input("what is the fastest any man made object has gone(please include km\s or mph or km/h )")


# cheaking their answer is correct and printing the repily for if it is correct or incorrect

if first_question_answer in ("11.1km/s", "24,791mph", "39,897km/h"):
    print("Correct that is the answer it was achieved by the crew of Apollo 10 ")

if first_question_answer not in ("11.1km/s", "24,791mph", "39,897km/h"):
    print("incorrect the answer is 11.1km/s or  24,791mph or 39,897km/h this was done by the crew of apollo ")



# second question and getting their answer for it
print("second question")
second_question_answer = input("What metal has the highest melting point")


# cheaking their answer is correct and printing the repily for if it is correct or incorrect

if second_question_answer in ("Tungsten", "tungsten"): 
    print("correct it has a melting point of 3,422 celises ")

if second_question_answer not in ("Tungsten", "tungsten"):
    print("incorrect the element is Tungsten with a melting point of 3422 celises")

    



