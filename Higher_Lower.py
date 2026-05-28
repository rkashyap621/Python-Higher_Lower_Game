import Higher_Lower_ASCII_Art as art
import Higher_Lower_Game_Manager as game

print(art.logo)
current_score = 0
person1,person2=game.init_game()
print("Current Score: ",current_score)
print(f"Compare A: {person1["name"]}, a {person1["description"]}, from {person1['country']} ")
print(art.vs)
print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}")

guess=input("Who has more followers on Instagram 'A' or 'B'?: ")
current_score, should_continue= game.compare_guess(guess, person1, person2, current_score)

while should_continue:
    print("\n"*20)
    print(art.logo)
    print("Current Score: ", current_score)
    person1,person2=game.continue_game(person2)
    print("\n")
    print(f"Compare A: {person1["name"]}, a {person1["description"]}, from {person1['country']} ")
    print(art.vs)
    print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}")
    print("\n")
    guess = input("Who has more followers on Instagram 'A' or 'B'?: ")
    current_score, should_continue = game.compare_guess(guess, person1, person2, current_score)

print("Game Over!")
print(f"Final Score: {current_score}")
