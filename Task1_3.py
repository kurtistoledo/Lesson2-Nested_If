# 1. Nested Decisions: The Adventure Game
# Task 3: Default Path
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("Do you want to climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    torch_action = input("Do you want to light a torch or proceed in the dark? ")
    if torch_action == "light a torch":
        print("You light a torch and see ancient drawings on the cave walls.")
    elif torch_action == "proceed in the dark":
        print("You stumble in the darkness but find a hidden treasure!")
    else:
        pass
else:
    pass 