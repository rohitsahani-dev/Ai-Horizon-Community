import random

random_num = random.randint(1, 100)


while True:
     try:
        guss = int(input("Guess a number from 1 to 100: ")) 
        if guss == random_num:
            print("Congratulations! You guessed correctly.")
            print(f"You gussed correctly the number was {guss} ")
            break
        elif guss < random_num:
            print("Too low")
        elif guss > random_num:
            print("Too high")
     except:
        print("Incorrect input enter number between(1 to 100)")


