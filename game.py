import random
number = random.randint(1, 100)
guess = 3
while guess != number:
    guess = int(input("Suggest a number ?"))
    if (guess < number):
        print("Guess Higher!")
        
    elif(guess > number):
        print("Guess Lower!")
    else:
        print("You won!")