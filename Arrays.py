# Arrays
import array
import random
game_won = bool(0)
Array = array.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Number = 0
random_number = random.choice(Array)
while game_won == bool(0):
    try:
        while Number not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
            Number = int(input("Choose a number between 1 and 10:   "))
            if Number not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
                print("Funny guy, but I need a number between 1 and 10 only")
        random.choice(Array)
        print("The number I'm thinking of is...")
        if Number != random_number:
            print("Not that one, try again!")
            Number = 0
        elif Number == random_number:
            game_won = bool(1)
    except ValueError:
        print("Funny guy, but I needed a numeric value")
print(random_number, "\nYou guessed right, well done!")
