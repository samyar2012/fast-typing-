

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user's choice
def make_choice(choice):
    computer_choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(computer_choices)

    result = determine_winner(choice, computer_choice)

    result_label.config(text=f"Computer chose {computer_choice}\n{result}")

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Create a frame for layout
frame = ttk.Frame(window, padding=20)
frame.grid(row=0, column=0)

# Customize the background color to create a luxurious look
window.configure(bg="#FFD700")  # Golden background
frame.configure(style="TFrame")

# Create buttons for Rock, Paper, and Scissors
rock_button = ttk.Button(frame, text="Rock", command=lambda: make_choice("Rock"))
paper_button = ttk.Button(frame, text="Paper", command=lambda: make_choice("Paper"))
scissors_button = ttk.Button(frame, text="Scissors", command=lambda: make_choice("Scissors"))

rock_button.grid(row=0, column=0, padx=10, pady=5)
paper_button.grid(row=0, column=1, padx=10, pady=5)
scissors_button.grid(row=0, column=2, padx=10, pady=5)

# Create a label for displaying the result
result_label = ttk.Label(frame, text="", font=("Arial", 14))
result_label.grid(row=1, columnspan=3, pady=20)

# Start the main event loop
window.mainloop()
