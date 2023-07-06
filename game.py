import random 
print("")
Intro = input("             Welcome To The Game!!!!Press Enter To Start")
print("")
print('''     Rules That You Should Know Before Starting the Game := 

               1) Rock wins against scissors.
               2) Scissors win against paper.
               3) Paper wins against rock.    
                 ''')

user_wins = 0

Computer_wins = 0 

match=0

choices = ["rock","paper","scissor","q","quit"]

Tie = 0 
Rounds = int(input(("No. of Rounds You Would Like To Play := ")))
i=1
while i<=Rounds :


    print("Computer picked one option from choices , Now its Your Turn!")

    user = input("Enter Your Choice : rock / paper / scissor OR Q/quit(Quits the game) := ").lower()


    random_pick = random.randrange(0,2) 

    Computer_Picks = choices[random_pick]

    print("Computer Picked : ",Computer_Picks)

    

    if user not in choices :

        print("Error,Please select a valid choice!")

    # 0 = rock ,  1 = paper  , 2 = scissor 

    elif user == "rock" and Computer_Picks=="paper" :
        print("Paper covers rock! You lose.Computer Won")
        Computer_wins+=1

    elif user == "rock" and Computer_Picks=="scissor" :
        print("Rock smashes scissors! You win!")
        user_wins+=1

    elif user == "scissor" and Computer_Picks=="paper":
        print("Scissors cuts paper! You win!")
        user_wins+=1

    elif user == "scissor" and Computer_Picks=="rock":
        print("Rock smashes scissors! You lose.Computer Won")
        Computer_wins+=1

    elif user == "paper" and Computer_Picks=="rock" :
        print("Paper covers rock! You win!")
        user_wins+=1

    elif user == "paper" and Computer_Picks=="scissor" :
        print("Scissors cuts paper! You lose.Computer Won")
        Computer_wins+=1
    
    elif user==Computer_Picks :
        print("Both players selected",user,"It's a Tie!!")
        Tie += 1

    else :
        if user == "q" or user == "quit" :
            print("Thanks For Playing!")
            break

    match = match+1
    i+=1


print("--------------------RESULT------------------------")
print()
print("You Selected ",Rounds,"Rounds")
print("Total No. of Matches You Played : ",match)
print("Computer Won ",Computer_wins,"Match")
print("You Won ",user_wins,"Match")
print("Total No. of Tie : ",Tie)
print()

if Computer_wins>user_wins :
    diff = Computer_wins-user_wins
    print("Computer Won/Lead by ",diff,"Matches")

elif user_wins>Computer_wins :
    diff = user_wins-Computer_wins
    print("You Won/Lead by ",diff,"Matches")

else :
    print("It's a Tie!")

print("--------------------")

