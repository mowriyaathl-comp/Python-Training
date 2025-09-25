import random
print("Welcome to Random number game!!")
secret_number=random.randint(1,5)
for guess in range(1,4):
    guess=int(input("Enter the guess value: "))
    if guess==secret_number:
        print("you are won the game!")
    elif guess>secret_number:
        print("you num is high ")
    elif guess<secret_number:
        print("you num is low ")
    else:
        print("you lose the game")
        
        
    