import random

'''
Project Introduction
In this project, we will create a simple game called rock paper scissors by creating objects. So be sure to revise objects and classes before you proceed.

Working of the game
If you don't know, here's how the game works:

This game is played between two players.
Each player can choose either rock or paper or scissors.
If both players choose the same thing, it's a draw.
However, if the players choose different things, one will win and the other will lose. The rule is:

rock - scissors: rock will win (rock crushes scissors)
rock - paper: paper will win (paper covers rock)
scissors - paper: scissors win (scissors cuts paper)
Project Description
Here's how our project works:

This game will be played between the computer and the user.
The computer will randomly pick either rock, paper or scissors. The user will not know what the computer's pick.
The user will be asked to choose either rock, paper or scissors.
We will compare the computer's pick and the user's pick and decide whether the user won or lost or drew.
Idea Emoji
Note: We have created this game in the Python Basics course using functions. Now we will create this game using an object-oriented programming approach.

'''

# Step 1: Create a Player Class
# Create a Player class with the following methods:


class Player:
    def get_player_info(self):
        self.name = input("Enter your name: ")
        self.choice = input("Enter your choice (rock/paper/scissors): ")

    def display_player_info(self):
        print("Player Name:", self.name)
        print("Player Choice:", self.choice)


# Step 2: Create a Computer Class
# Create a Computer class with the following methods:

class Computer:
    def get_computer_choice(self):
        choices = ["rock", "paper", "scissors"]
        self.choice = random.choice(choices)

    def get_player_choice(self):
        choices = ["rock", "paper", "scissors"]
        while True:
            user_choice = input(
                "Enter your choice (rock/paper/scissors): ").lower()
            if user_choice in choices:
                self.choice = user_choice
                break
            else:
                print("Invalid choice. Please try again.")
        return self.choice

    def display_computer_choice(self):
        print("Computer Choice:", self.choice)


# Step 3: Create a Game Class
# Create a Game class with the following methods:

class Game:
    def compare_choices(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "draw"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
                (player_choice == "paper" and computer_choice == "rock") or \
                (player_choice == "scissors" and computer_choice == "paper"):
            return "win"
        else:
            return "lose"

    def display_result(self, result):
        if result == "draw":
            print("It's a draw!")
        elif result == "win":
            print("Congratulations! You won!")
        else:
            print("Sorry! You lost!")


# Step 4: Create the Main Function
# Create a main function to run the game. In the main function, create objects of the Player, Computer and Game classes and call their methods to play the game.

def main():
    # create objects of Player, Computer and Game classes
    player = Player()
    computer = Computer()
    game = Game()

    # get player info
    player.get_player_info()

    # get computer choice
    computer.get_computer_choice()

    # display player and computer choices
    player.display_player_info()
    computer.display_computer_choice()

    # compare choices and display result
    result = game.compare_choices(player.choice, computer.choice)
    game.display_result(result)


# Step 8: Run the Game
# Run the game by calling the main function.
main()
