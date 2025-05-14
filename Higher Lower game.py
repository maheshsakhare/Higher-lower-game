#Display Art

from art import logo,vs
from game_data import data
import random



def format_data(account):
    """Take the account data and return the printable format."""
    account_name = account["name"]
    account_desr  = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and followers count and return if they got it right."""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
    

print(logo)

score = 0
#Make the game repeatable.
game_should_continue = True
account_b = random.choice(data)

#Making account at position B become the necxt account at postion A.

while game_should_continue:
    #Generate a random account from the game data.

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")


    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B' : ").lower()

    #Clear the screen
    print("\n"*20)
    print(logo)
    
    #Check if user is correct.
    #Get follower count of each account
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]

    is_correct  = check_answer(guess, a_follower_account,b_follower_account)


    #Give user feedback on their guess.
    #Score keeping

    if is_correct:
        score += 1
        print(f"You're right!, current_score :{score}")
    else:
        print(f"sorry, that's wrong!, Final score: {score}")
        game_should_continue = False

        


