import random

def generate_story():
    # Lists of characters, places, and actions
    characters = ["A tiny robot 🤖", "A flying kitten 🐱🚀", "A genius turtle 🐢"]
    places = ["on the moon 🌙", "in a chocolate forest 🍫🌳", "at the bottom of the sea 🌊"]
    actions = ["started dancing 💃", "began singing opera 🎶", "found a hidden treasure 💎"]

    # Randomly selecting one element from each list
    char = random.choice(characters)
    place = random.choice(places)
    action = random.choice(actions)

    # Combining them into a story
    story = f"One day, {char} went {place} and suddenly {action}!"
    
    print("-" * 30)
    print("Your Unique Story:")
    print(story)
    print("-" * 30)

# Run the program
if __name__ == "__main__":
    generate_story()
