import random
print("I am thinking about a number between 1 and 100")
print("You have five choices to guess the number")
computer_choice=random.randint(1,100)
for i in range(1,6):
    print(f"Attempt no:{i}")
    user_choice=int(input("Guess the number :"))

    if user_choice==computer_choice:
        print("Your guess is correct ,Congratulations , you have won the game")
        break


    elif user_choice<computer_choice:
        print(f"Try a higher number, you have {5-i} tries left")


    elif user_choice>computer_choice:
        print(f"Try a lower number , you have {5-i} tries left")


else:
    print("Sorry, you lost")
    print(f"Answer:{computer_choice}")
    print("Try Next time")