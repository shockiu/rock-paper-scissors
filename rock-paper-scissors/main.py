import  random

def rock_papper_scissors():
     
    user_option = input("Choose rocket (r), scissors (s) or paper (p)").lower()
    ramdon_choice = random.choice(['r', 'p', 's'])
    if user_option == ramdon_choice:
        print("It\'s a tie")
        return
    
    if win_user(user_option, ramdon_choice):
        print("You win!")
        return

    print("You lose!")




def win_user(user_choice, ramdon_choice):
    if (user_choice == "r" and ramdon_choice == "s") or (user_choice == "s" and ramdon_choice == "p") or (user_choice == "p" and ramdon_choice == "r"):
        return True
    
rock_papper_scissors()