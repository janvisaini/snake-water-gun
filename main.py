import random 

def user_input():
	# take input from user and return it
    return input("enter\n s - snake\n w -water \n g - gun\n\n") 

# list of choices that can be make
choice_list=["s","g","w"]


def bot_choice():
	# return the bot's random choice
    return random.choice(choice_list)

def botwin(user,bot):
	# keep track of how many matches bot wins
	global bot_win
	print(f"YOU : {user} \nBOT : {bot}\n               BOT wins\n\n")
	bot_win+=1

def userwin(user,bot):
	# keep track of how many matches you wins
	global user_win
	print(f"YOU : {user} \nBOT : {bot}\n               YOU wins\n\n")
	user_win+=1	

# defining necssary variables
user_win=0
bot_win=0
tie=0

def result(user, bot):
	# rules implementaion for game
	if user == "s" and bot=="g":
		botwin(user,bot)       
	
	elif user == "g" and bot=="w":
		botwin(user,bot) 

	elif user == "w" and bot=="s":
		botwin(user,bot) 

	elif user == "g" and bot=="s":
	    userwin(user,bot)
	
	elif user == "w" and bot=="g":
		userwin(user,bot)

	elif user == "s" and bot=="w":
		userwin(user,bot)
	
	elif user == bot:
	    print(f"YOU : {user}\nBOT :{bot}\n             match tie\n\n")
	    global tie
	    tie+=1

for i in range(11):
    user=user_input()
    while user not in choice_list:
        print("invalid input")
        user=user_input()

    res=result(user,bot_choice())


# printing the summary of series
print(f"""user win: {user_win} times\n
Bot wins: {bot_win} times\n
Tie : {tie} times """)
