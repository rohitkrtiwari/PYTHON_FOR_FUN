import random
choices=["snake","water","gun"]
print("\n\t\t********   SNAKE WATER GUN     ********")

user_score=0
comp_score=0
i=0

while i<=10:
    i=i+1
   
    print("\nChoose One from SNAKE WATER and GUN: ")
    user_choice=input('user: ').lower()
    comp_choice=random.choice(choices)

    if user_choice==comp_choice:
        print("computer: ",comp_choice)
        print("DRAW!")

    if user_choice == "snake" and comp_choice == "water":
        print("computer: ",comp_choice)
        user_score += 1
        print("You've got +1")
        print("your score: ",user_score)
        print("comp score: ",comp_score)

    if user_choice == "snake" and comp_choice == "gun":
        print("computer: ",comp_choice)
        comp_score += 1
        print("comp got +1")
        print("your score: ",user_score)
        print("comp score: ",comp_score)

    if user_choice == "water" and comp_choice == "snake":
        print("computer: ",comp_choice)
        comp_score += 1
        print("comp got +1")
        print("your score: ",user_score)
        print("comp score: ",comp_score)

    if user_choice == "water" and comp_choice == "gun":
        print("computer: ",comp_choice)
        user_score += 1
        print("You've got +1")
        print("your score: ",user_score)
        print("comp score: ",comp_score)

    if user_choice == "gun" and comp_choice == "water":
        print("computer: ",comp_choice)
        comp_score += 1
        print("comp got +1")
        print("your score: ",user_score)
        print("comp score: ",comp_score)

    if user_choice == "gun" and comp_choice == "snake":
        print("computer: ",comp_choice)
        user_score += 1
        print("You've got +1")
        print("your score: ",user_score)
        print("comp score: ",comp_score)

if user_score<comp_score:
    print("\nComp score: ",comp_score)
    print("Your score: ",user_score)
    print("Better Luck Newt Time !")

elif comp_score<user_score:
    print("\nComp score: ",comp_score)
    print("Your score: ",comp_score)
    print("Hurrah! You won !")