#Import randomness for enemy
import random
#True statement for while loop
run = True
#Random computer action option
choices = ['Sword', 'Shield', 'Spell']

#Interactions
# What happens if user chooses Sword
def action_sword(user, comp, comp_action):
    if comp_action == 'Sword':
        comp.hp -= 3
        user.hp -= 3
        print("You trade sword strike for axe swing with the orc.")
        print(f"Knight: {user.hp}HP  Orc: {comp.hp}HP")
    elif comp_action == 'Shield':
        print("Your sword bounces off of the orc's large rectangular shield.")
        print(f"Knight: {user.hp}HP  Orc: {comp.hp}HP")
    elif comp_action == 'Spell':
        comp.hp -= 3
        print("Your sword thrust stops a massive spell from the orc.")
        print(f"Knight: {user.hp}HP  Orc: {comp.hp}HP")
    else:
        print("error oh no")

# What happens if user chooses Shield
def action_shield(user, comp, comp_action):
    if comp_action == 'Sword':
        print("You raise shield just in time to block your foe's axe.")
        print(f"Knight: {user.hp}HP  Orc: {comp.hp}HP")
    elif comp_action == 'Shield':
        print("You and your foe wait for the other to make the first move...")
        print(f"Knight: {user.hp}HP  Orc: {comp.hp}HP")
    elif comp_action == 'Spell':
        user.hp -= 4
        print("Your shield cannot block the orc's spiritual strike.")
        print(f"Knight: {user.hp}HP  Orc: {comp.hp}HP")
    else:
        print("error oh no")

# What happens if user chooses Spell
def action_spell(user, comp, comp_action):
    if comp_action == 'Sword':
        user.hp -= 3
        print("Your spell in interuppted by a solid swing of the orc's axe.")
        print(f"Knight: {user.hp}HP  Orc: {comp.hp}HP")
    elif comp_action == 'Shield':
        comp.hp -= 4
        print("Your fireball pierces right through your opponents defenses.")
        print(f"Knight: {user.hp}HP  Orc: {comp.hp}HP")
    elif comp_action == 'Spell':
        user.hp -= 4
        comp.hp -= 4
        print("You and your opponent each unleash a devastating magical attack.")
        print(f"Knight: {user.hp}HP  Orc: {comp.hp}HP")
    else:
        print("error oh no")

# Stats for enemy
class comp:
    def __init__(self, name):
        self.hp = 10
        self.name = "Orc"
    # Computer is given choices
    def choose_action(self):
        self.comp_action = random.choice(choices)

# Stats for user
class user:
    def __init__(self, name):
        self.hp = 10
        self.name = "Knight"
    # Player is given action choices
    def choose_action(self):
        while True:
            user_choice = input(f"Choose your action ({'|'.join(choices)}): ").capitalize()
            if user_choice in choices:
                return user_choice
            else:
                print("Invalid input. Try again.")


# Main game
def main():
    user_character = user('Knight')
    computer_character = comp('Orc')

    # Main loop for game
    while user_character.hp > 0 and computer_character.hp > 0:
        # Computer chooses action
        computer_character.choose_action()

        # User chooses action
        user_choice = user_character.choose_action()

        # Execute actions based on choices
        if user_choice == 'Sword':
            action_sword(user_character, computer_character, computer_character.comp_action)
        elif user_choice == 'Shield':
            action_shield(user_character, computer_character, computer_character.comp_action)
        elif user_choice == 'Spell':
            action_spell(user_character, computer_character, computer_character.comp_action)

        # Checks health for win condition
        if user_character.hp <= 0 and computer_character.hp <= 0:
            print("You and the orc collapse at the same time. Draw...")
        elif user_character.hp <= 0:
            print("The orc laughs as you slowly loose conciousness. You Lose.")
            break
        elif computer_character.hp <= 0:
            print("With a perfectly timed strike the orc finally falls. Victory!")
            break
        
#run the game
if __name__ == "__main__":
    main()
