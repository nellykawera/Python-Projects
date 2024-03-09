print("Welcome to my computer quiz!")

Playing= input("Do you want to play? ")

if Playing.lower() != "yes":
    quit()
print("Okay, let's play :) ")

score = 0

Answer = input("What does CPU stands for? ")
if Answer.lower() == "central processing unit":
    print("Correct!")
    score +=1

else:
    print("Incorrect!")

Answer = input("What does GPU stands for? ")

if Answer.lower() == "graphic processing unit":
    print("Correct!")
    score +=1

else:
    print("Incorrect!")

Answer = input("What does RAM stands for? ")

if Answer.lower() == "random access memory":
    print("Correct!")
    score +=1

else:
    print("Incorrect!")

Answer = input("What does PDU stands for? ")
if Answer.lower() == "power supply":
    print("Correct!")
    score +=1

else:
    print("Incorrect!")  
    
    
Answer = input(" What does ROM stands for? ")
if Answer.lower() == "read only memory":
    print("Correct!")
    score +=1

    
Answer = input(" What does ROM stands for? ")
if Answer.lower() == "read only memory":
    print("Correct!")
    score +=1
    

else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("you got: " + str(score*100/6) + "%")