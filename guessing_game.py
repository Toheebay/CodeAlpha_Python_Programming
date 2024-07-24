import random
random_number = random.randint(1,20)
tries=7
while tries>0:
    number = int(input("Guess your choice of number between 1 to 20 ?"))
    if number > random_number:
      print("Too High")
    tries = tries - 1
    if number < random_number:
        print("Too low")
    tries = tries - 1
    if number == random_number:
        print("You Claim your winner!")
        print("Total Guesses", 7-tries)
        break
    if tries == 0:
        print(" Sorry you can come back again!")
    