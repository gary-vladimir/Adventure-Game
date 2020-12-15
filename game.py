from time import sleep
import random

def print_by_time(text):
    print(text)
    sleep(2)

def intro():
    print_by_time("You find yourself standing in an open field, filled with grass and yellow wildflowers.")  
    print_by_time(f"Rumor has it that a {enemy} is somewhere around here, and has been terrifying the nearby village.")
    print_by_time("In front of you is a house.")
    print_by_time("To your right is a dark cave.")
    print_by_time("In your hand you hold your trusty (but not very effective) dagger\n")

def house_choice():
    while True:
        election = input("Would you like to (1) fight or (2) run away?")
        if election == '1':
            return 1
        if election == '2':
            print_by_time("You run back into the field. Luckily, you don't seem to have been followed.\n")
            return 2

def choice():
    print("What would you like to do?")
    while True:
        election = input("(Please enter 1 or 2).\n")
        if election == '1':
            return 1
        if election == '2':
            return 2

def field():
    print_by_time("Enter 1 to knock on the door of the house")
    print_by_time("Enter 2 to peer into the cave.")


def fight(magical_sword):
    if magical_sword == False:
        print_by_time("You do your best...")
        print_by_time(f"but your dagger is no match for the {enemy}.")
        print_by_time("You have been defeated!\n")
        return "defeated"
    if magical_sword == True:
        print_by_time(f"As the {enemy} moves to attack, you unsheath your new sword.")
        print_by_time("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
        print_by_time(f"But the {enemy} takes one look at your shiny new toy and runs away!")
        print_by_time(f"You have rid the town of the {enemy}. You are victorious!\n")
        return "victory"

def house(magical_sword):
    print_by_time("You approach the door of the house.")
    print_by_time(f"You are about to knock when the door opens and out steps a {enemy}.")
    print_by_time(f"Eep! This is the {enemy} house!")
    print_by_time("The pirate attacks you!")
    if magical_sword == False:
        print_by_time("You feel a bit under-prepared for this, what with only having a tiny dagger.")


def dark_cave(sword):
    magical_sword = sword
    if magical_sword == False:
        print_by_time("You peer cautiously into the cave.")
        print_by_time("It turns out to be only a very small cave.")
        print_by_time("Your eye catches a glint of metal behind a rock.")
        print_by_time("You have found the magical Sword of Ogoroth!")
        print_by_time("You discard your silly old dagger and take the sword with you.")
        print_by_time("You walk back out to the field.\n")
        magical_sword = True
    elif magical_sword == True:
        print_by_time("You peer cautiously into the cave.")
        print_by_time("You've been here before, and gotten all the good stuff.")
        print_by_time("It's just an empty cave now.") 
        print_by_time("You walk back out to the field.\n")
    return magical_sword

def game():
    magical_sword = False
    end = False
    while end == False:
        field()
        first_choice = choice()
        if first_choice == 1:
            house(magical_sword)
            second_choice = house_choice()
            if second_choice == 1:
                fight(magical_sword)
                end = True
        elif first_choice == 2:
            magical_sword = dark_cave(magical_sword)

lst_off_enemy = ["pirate","evil ninja","troll"]
enemy = random.choice(lst_off_enemy)
intro()
game()