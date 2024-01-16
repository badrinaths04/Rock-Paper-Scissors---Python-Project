import random

def play():
    user = input("Whats your choice ?\n'r' for rock 'p' for paper and 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == computer:
        return "Tie"
    
    elif is_win(user,computer):
        return "$ You Won $"
    
    else:
        return "! You Lost !"
    
def is_win(player,opponent):
         # r > s, s > p, p > r
        if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
             return True
        
print(play())



