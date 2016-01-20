from random import randint

start = ("You are in a dark dungeon all alone, and you have to kill the dragon that you will see.")

print(start)
playerdead = False
playergold = 0
playersword = False
dragondead = False

encounter = "null"

while playerdead == False:

    x = randint(0,3)

    if x == 0:
        print("There is nothing here")
        encounter = "empty"

    elif x == 1:
        print("You have found some gold")
        encounter = "gold"

    elif x == 2:
        print("You have encountered a dragon")
        encounter = "dragon"

    elif x == 3:
            print("You have encountered a goblin")
            print("GOBLIN: Can I have some money?")
            encounter = "goblin"
    
    
    while encounter == "empty":
        inputstr = input(">> ")
        
        if(inputstr == "walk"):
            encounter = "null"

        elif(inputstr == "buy"):
            if playergold >= 4:
                playersword = True
                print("You now have a sword!")
                encounter = "null"

            else:
                print("You do not have enough money to buy a sword")
        else:
            print("There is no such command as",inputstr,".")
            
                

        

    while encounter == "gold":
        inputstr = input(">> ")

        if(inputstr == "pickup"):
            playergold = playergold + 1
            print("You now have ",playergold," gold ")
            encounter = "null"

        elif(inputstr == "walk"):
            encounter = "null"

        elif(inputstr == "buy"):
            if playergold >= 4:
                playersword = True
                print("You now have a sword!")
                encounter = "null"

            else:
                print("You do not have enough money to buy a sword")

        else:
            print("There is no such command as",inputstr,".")
            




                

    while encounter == "dragon":
        inputstr = input(">> ")
        
        if(inputstr == "buy"):
            if playergold >= 4:
                playersword = True
                print("You now have a sword!")
                encounter = "null"
            else:
                print("You do not have enough money to buy a sword")


        elif(inputstr == "fight"):
            if playersword == True:
                print("You Won")
                playerdead = True
                encounter = "null"

            else:
                print("You lose")
                playerdead = True
                encounter = "null"


        elif inputstr == "run":
            encounter = "null"

        else:
            print("There is no such command as",inputstr + ".")




    while encounter == "goblin":
        
        inputstr = input(">> ")
        
        
        if(inputstr == "walk"):
            encounter = "null"

        elif(inputstr == "give"):
            if playergold >= 1:
                playergold = playergold - 1
                print("You gave 1 gold to the goblin. You now have",playergold,"gold")
                x = randint(0,1)
                
                if x == 1:
                    playersword = True
                    print("The goblin gave you a sword")

                elif x == 0:
                    print("The goblin took your money")
                
                encounter = "null"

            else:
                print(" You do not have enough money to give to the Goblin.")
                
                
        else:
            print("There is no such command as",inputstr,".")
            


            
            
        

        
                
                

            

        


        

        
        
