import random

def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']

def random_play():
    """ Vraci rock, paper nebo scissors se stejnou pravdepodobnosti """
    return random.choice(['rock', 'paper', 'scissors'])

def determine_game_result(human,computer):
    if human == computer:
        return "tie"
    # elif human == 'rock' and computer == 'paper':
    #     return "computer"
    # elif human == 'rock' and computer == 'scissors':
    #     return "human"
    # elif human == 'paper' and computer == 'scissors':
    #     return "computer"
    # elif human == 'paper' and computer == 'rock':
    #     return "human"
    # elif human == 'scissors' and computer == 'rock':
    #     return "computer"
    # elif human == 'scissors' and computer == 'paper':
    #     return "human"
    elif human+computer in "rockpaperscissorsrock":
        return "computer"
    else:
        return "human"

def main(input=input):
    human = None
    while not is_valid_play(human):
        human = input('rock, paper or scissors? ')
    computer = random_play()
    print(computer)
    print("The winner is: {}!".format(determine_game_result(human,computer)))

if __name__ == "__main__":
    main()
