import random

randomnum = random.randint(1,200)
# print(randomnum)
Guessnumber = None
guesses = 0

while (Guessnumber != randomnum): 
    Guessnumber = int(input("Guess the Number : "))
    guesses += 1
    if Guessnumber == randomnum:
        print("You Guessed it right!")
    else:
        if Guessnumber>randomnum :
            print("You Guessed it wrong! Enter the smaller number")
        else:
            print("You Guessed it wrong! Enter the larger number")

print(f"You Guessed the number in {guesses} guesses")
with open("hiscore.txt","r") as f:
    hiscore = int(f.read())
if guesses<hiscore : 
    print("You have just broken the High score!")
    with open ("hiscore.txt","w") as f:
        f.write(guesses)

    
    


