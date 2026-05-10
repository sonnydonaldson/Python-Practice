# 3 Question Quiz - Debug all the errors, including any semantic errors.


# intro to the quizz
print("Hello!")
print("This is a quick 3 part quiz. A question will be asked, and then you answer it")

# printing the first question and getting their answer
print("First question:")
first_answer = input("How many millimetres in a centimetre?")


 # cheaking their answer is correct and printing the repily for if it is correct or incorrect 
if first_answer in ("10") :
  
  
    print("Correct the answer is 10") 
if first_answer != ("10") : 
    print("Incorrect the answer is 10")


 # printing the second question and getting there answer
print("Next Question:")
second_answer = input("What is the capital of New Zealand?")

# cheaking their answer is correct and printing the repily for if it is correct or incorrect 

if second_answer in ("wellington", "Wellington"):
     print("Correct the answer is Wellington")

elif second_answer != ("wellington", "Wellington") : 
    print("Incorrect the answer is Wellington")
     

# printing the third question and getting there answer
print("Final Question!")
third_answer = input("What is 3 x 6 ")


# cheaking their answer is correct and printing the repily for if it is correct or incorrect 
if third_answer in ("18") :
    print("Correct the answer is 18")

if third_answer != ("18") : 
    print("Incorrect the answer is 18")


