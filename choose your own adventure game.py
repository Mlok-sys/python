name = input("type your nsme: ")
print("welcome",name,"to this adventure!")

answer=input("You are in a dirt road, it has come to an end ank you can go left or right, which way you would like to go? ").lower()

if answer == "right":
    answer = input("You come to a river, you can walk around it or you can swim across? type walk to walk or swim to swim across: ")
    if  answer == "swim":
        print("you swam across and eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose. ")

elif answer == "left":
        answer = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
        if answer == "cross":
            answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
            if answer.lower() == "yes":
                print("you talk to the stranger and they give you gold. You won.")
            elif answer == "no":
                print("you ignore the stranger and they are offended and you lost.")
            else:
                print("This is invalid option.")
        else:
            print("This is invalid option.")
        if answer == "back":
            print("You go back and lose. ")
print("thanks for playing mr" ,name)

