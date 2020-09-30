import random 



def user_input():

    inp=input("enter\n s - snake\n w -water \n g - gun\n") 

    return(inp)

   

  

def bot_choice():

    choice_list=["s","g","w"]

    choice=random.choice(choice_list)

    return(choice)



user_win=0

bot_win=0

tie=0

  

def result(user, bot):

    

    global user_win

    global bot_win

    global tie

    

    if user == "s" and bot=="g":        

        print(f"You chose {user} and bot chose {bot}\n bot wins")

        bot_win+=1

    elif user == "g" and bot=="w":         

         print(f"You chose {user} and bot chose {bot}\n bot wins")

         bot_win+=1 

    elif user == "w" and bot=="s":

         print(f"You chose {user} and bot chose {bot}\n bot wins")

         bot_win+=1 

    elif user == "g" and bot=="s":

         print(f"You chose {user} and bot chose {bot}\n you wins")

         user_win+=1 

    elif user == "w" and bot=="g":

        print(f"You chose {user} and bot chose {bot}\n you wins")

        user_win+=1 

    elif user == "s" and bot=="w":

        print(f"You chose {user} and bot chose {bot}\n you wins")

        user_win+=1

    elif user == bot:

        print(f"You chose {user} and bot chose {bot}\n match tie")

        tie+=1

    return(f"\n\n\nyou win: {user_win} times\n bot_win: {bot_win} times\ntie: {tie}times \n\n\n")

n=0

while n<10:

    user=user_input() 

    res=result(user,bot_choice())

    n=n+1

    

print(res)
