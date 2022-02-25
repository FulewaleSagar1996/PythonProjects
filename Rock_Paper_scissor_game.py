# #Rules for Game
# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.
import random
user_choice = int(input("what do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.\n"))
if user_choice>2:
    print("you type wrong number.You loose")
else:
    computer_choice = random.randint(0,2)

    print(computer_choice)
    if user_choice==1 and computer_choice==0:
     print("You win")
    elif user_choice==2 and computer_choice==1:
     print("You win")
    elif user_choice==0 and computer_choice==2:
     print("You win")
    else:
     print("you loose")
