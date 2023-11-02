print("Welcome to my computer quiz")

playing=input("Do you want to play? ")

if playing.lower()!= "yes":
    quit()
    
print("Okay! Let's start :)")
score=0

question=input("Inside which HTML element do we put the JavaScript? ")
if question.lower()=="Float":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
    
question=input("Which company developed JavaScript? ")
if question.lower()=="Netscape":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
    
question=input("Javascript is an _______ language? ")
if question.lower()=="Object-Oriented":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
    
question=input("The" + "function" + "and"  " var" + "are known as? ")
if question.lower()=="Declaration statements":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
    
question=input(" How can a datatype be declared to be a constant type? ")
if question.lower()=="const":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
    
question=input("What keyword is used to check whether a given property is valid or not? ")
if question.lower()=="in":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
    
question=input("Which operator is used to combine two or more strings in JavaScript? ? ")
if question.lower()=="+":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
    
question=input("What is the index of the first element in an array? ")
if question.lower()=="0":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
    
question=input("What method do you use to join all elements of an array into a single string? ")
if question.lower()=="join()":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
    
question=input("How do you find the index of a specific element in an array? ")
if question.lower()=="indexOf()":
    print('Correct!')
    score+=1
else:
    print('Incorrect!')
    
print("You got " + str(score) + " questions correct! ")
print("You got " + str((score/10)*100) + "%.")