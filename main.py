"""
main.py

Orchestrates the Wiki Word Chain Game by importing modules:
- player.py: setup_players, display_game_rules
- levels.py: beginner_level, intermediate_level, advanced_level
- timer.py: initiate_players_scores, add_score, print_scores
"""
import wikipedia
import random
from datetime import datetime
import time
import sys

from player import setup_players, display_game_rules, play_turn
from levels import beginner_level, intermediate_level, advanced_level
from timer import (initiate_players_scores, add_score, print_scores)


def main_game():
	"""
	Main game flow:
	1. Setup players and initialize scores.
	2. Display rules and wait for user input.
	3. Loop through each player for Beginner, then Intermediate, then Advanced.
	4. Print final scores.
	"""
	# 1. Setup Phase
	# Get player names
	players = setup_players()
	# Show the rules
	display_game_rules()
	# Initialize scores for all players
	initiate_players_scores(players)
	input("\nPress Enter to start the game...")



	# 2. Beginner Level for all players
	print("\n========== Beginner Level ==========")
	for player in players:
		play_turn(player, 'beginner')

	# 3. Intermediate Level
	print("\n========== Intermediate Level ==========")
	input("Press Enter to continue to the Intermediate Level...")
	for player in players:
		play_turn(player, 'intermediate')

	# 4. Advanced Level
	print("\n========== Advanced Level ==========")
	input("Press Enter to continue to the Advanced Level...")
	for player in players:
		play_turn(player, 'advanced')

	# 5. End of Game - Print Final Scores
	print("\n========== Game Over ==========")
	print_scores()
	print("\nThank you for playing the Wiki Word Chain Game!\n")


if __name__ == "__main__":
	main_game()
