import random
import game_data as data

def select():
    """This function returns a randon personality data as a python dictionary from database"""
    return random.choice(data.data)


def init_game():
    """This function initiates the game and returns two random personality data as python dictionaries"""
    a= select()
    b= select()
    return a,b


def continue_game(b):
    a= b
    b= select()
    return a,b


def compare_guess(choice, p1, p2, score):
    if choice == "A":
        compare_result = p1["follower_count"] > p2["follower_count"]
    else:
        compare_result = p1["follower_count"] < p2["follower_count"]
    if compare_result:
        print("Correct!")
        score+= 1
        play_continue = True
        return score, play_continue
    else:
        print("Incorrect!")
        play_continue = False
        return score, play_continue
