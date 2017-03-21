# TEXT BASED GAME LAND OF FARAH
import time
import os

# Text Structure and Color
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print("This is a text-based game called Land of Farah.\nControl is handled though text in the input window,"
      "\nand the goal of the game is to reach the treasure.\n")

Phrases_Decision_Positive = ["Y", "y", "Yes", "yes", "Ye", "ye"]
Phrases_Decision_Negative = ["N", "n", "No", "no", "Nah", "nah", "Na", "Na"]

time.sleep(2)
# Naming Process [Choosing the name of the character]

Named = 0; Answer = 0
while (Named == 0) or (Answer == 0):
    Answer = 0; Named = 0
    Char_Name = input("What is your name:  ")
    if not(Char_Name.isalpha()):
        print("You can only have letters in your name.")
    else:
        Char_Name_Change = input("Are you sure? [Y/N]:  ")
        while Answer == 0:
            for x in Phrases_Decision_Positive:
                if x in Char_Name_Change:
                    Answer = 1
                    Named = 1
            if Answer == 0:
                for x in Phrases_Decision_Negative:
                    if x in Char_Name_Change:
                        Answer = 1
                if Answer == 0:
                    print("I couldn't understand what you said. "
                          "\nAre you sure you want to keep the name ", Char_Name, "?", sep='')
                    Char_Name_Change = input("[Y/N]:  ")


os.system('cls')
Char_Name = Char_Name.capitalize()
print(color.GREEN + "------------------------------------------\n\nHello ", Char_Name, ", Welcome to Farah!", sep='')

# Introduction to game
time.sleep(2)
print("You will control your characters movement through a map by choosing either to go "
      "\nforward, left, right or backwards. You will also be given a description "
      "\nof your surroundings as you move about, as well as notices about interesting "
      "\nor relevant objects you encounter."
      "\n\nWhen the description ends with a star '*', the game waits for you to finish reading."
      "\nWhen you have done so, press [ENTER] to proceed. Have Fun!*" + color.END)
input()
os.system('cls')

# Starting the main game
time.sleep(2)
print(color.GREEN + "You feel groggy...")
time.sleep(3)
print("...*")
input()
time.sleep(3)
print("A large man wearing leather and a sodden hat suddenly bolts into the room and slams the door shut." + color.END)
print(Char_Name, "!!",sep='')
time.sleep(1)
print("WAKE UP!")
time.sleep(2)
print("You have to get to work. \nIts already noon and you are sleeping!!*")
input()
print(color.GREEN + "You slowly crawl yourself out of bed and onto a nearby chair. \nYour head feels like bursting, "
                    "but you look to your surroundings.")
print("Your clothes lay strewn in a heap on the floor. Not washed for over two weeks")