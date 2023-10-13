import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

# Function to play the game
def play_game():
    user_choice = user_choice_var.get()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer's choice: {computer_choice}\n{result}")

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create and place UI elements
user_choice_var = tk.StringVar()
user_choice_var.set("rock")  # Default choice

instruction_label = tk.Label(root, text="Choose rock, paper, or scissors:")
instruction_label.pack()

choice_frame = tk.Frame(root)
rock_button = tk.Radiobutton(choice_frame, text="Rock", variable=user_choice_var, value="rock")
paper_button = tk.Radiobutton(choice_frame, text="Paper", variable=user_choice_var, value="paper")
scissors_button = tk.Radiobutton(choice_frame, text="Scissors", variable=user_choice_var, value="scissors")
rock_button.pack(side="left")
paper_button.pack(side="left")
scissors_button.pack(side="left")
choice_frame.pack()

play_button = tk.Button(root, text="Play", command=play_game)
play_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()
