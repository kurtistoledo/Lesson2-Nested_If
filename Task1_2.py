# 1. Nested Decisions: The Adventure Game
# Task 2: Setting the Scene
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Do you want to climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    torch_action = input("Do you want to light a torch or proceed in the dark? ")
    if torch_action == "light a torch":
        print("The torch will give you light.")
    elif torch_action == "proceed in the dark":
        print("Good luck finding the treasure in the darkness!")

