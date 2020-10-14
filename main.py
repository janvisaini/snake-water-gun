import random 

def user_input():

    inp=input("enter\n s - snake\n w -water \n g - gun\n\n") 

    return(inp) 

choice_list=["s","g","w"]

def bot_choice():
    choice=random.choice(choice_list)

    return(choice)


def BOTWIN(user,bot):
	global bot_win
	print(f"YOU : {user} \nBOT : {bot}\n               BOT wins\n\n")
	bot_win+=1
def USERWIN(user,bot):
	global user_win
	print(f"YOU : {user} \nBOT : {bot}\n               YOU wins\n\n")
	user_win+=1	
	
user_win=0

bot_win=0

tie=0

def result(user, bot):
	if user == "s" and bot=="g":
		BOTWIN(user,bot)       
	
	elif user == "g" and bot=="w":
		BOTWIN(user,bot) 

	elif user == "w" and bot=="s":
		BOTWIN(user,bot) 

	elif user == "g" and bot=="s":
	          USERWIN(user,bot)
	
	elif user == "w" and bot=="g":
		USERWIN(user,bot)

	elif user == "s" and bot=="w":
		USERWIN(user,bot)
	
	elif user == bot:
	    print(f"YOU : {user}\nBOT :{bot}\n             match tie\n\n")
	    global tie
	    tie+=1

n=0

while n<10:

    user=user_input()
    while user_input not in choice_list:
        user=user_input()

    res=result(user,bot_choice())

    n=n+1

print(f"""user win: {user_win} times\n
Bot wins: {bot_win} times\n
Tie : {tie} times """)
