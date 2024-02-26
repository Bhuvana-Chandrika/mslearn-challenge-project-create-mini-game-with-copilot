import random
def rpc():
    valid_options = ['rock','paper','scissors']
    score=0
    
    while True:
        user_choice=input(" Enter your choice: rock, paper or scissors?")
        
        if user_choice in valid_options:
            opp_choice=random.choice(valid_options)

            if user_choice == opp_choice:
                print("It's a draw")
            elif (user_choice=='rock' and opp_choice=='scissors') or (user_choice=='scissors' and opp_choice=='paper') or (user_choice=='paper' and opp_choice=='rock'):
                print("Hurray! You won.")
                score+=1
            else:
                print("Oops! You lost.")
            
            play_again=input("Do you want to play again? (yes/no)").lower()
            if play_again!='yes':
                break

        else:
            print("Enter a valid choice")
    print("Your final score:",score)

rpc()
