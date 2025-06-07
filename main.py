import random

'''
1 for snake
-1 for water
0 for gun
'''

while True:
    computer = random.choice([-1, 0, 1])
    youstr = input("Enter your choice (s for snake, w for water, g for gun): ")
    youDict = {"s": 1, "w": -1, "g": 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

    you = youDict.get(youstr)
    if you is None:
        print("Invalid choice! Please enter s, w, or g.")
        continue

    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a draw")
    else:
        if computer == -1 and you == 1:
            print("You win!")
        elif computer == -1 and you == 0:
            print("You lose!")
        elif computer == 1 and you == -1:
            print("You lose!")
        elif computer == 1 and you == 0:
            print("You win!")
        elif computer == 0 and you == -1:
            print("You win!")
        elif computer == 0 and you == 1:
            print("You lose!")
        else:
            print("Something went wrong!")

    cont = input("Do you want to continue? (y/n): ").lower()
    if cont != 'y':
        print("Thanks for playing!")
        break
