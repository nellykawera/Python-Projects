import random


top_of_range= input("Type any number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <=0 :
        print("Please enter number greater than zero next time")
        quit()
else:
    print("Please enter a number next time")        
    quit()
random_number = random.randrange(0,top_of_range)
print(random_number)

while True :
    user_guess = input("make a guess: ")
    if  user_guess.isdigit():
        user_guess = int( user_guess)
    else:
        print("Please enter a number next time")
        continue
    if user_guess == random_number:
        print("you got it!")
        break
    else:
        print("you got it wrong!")