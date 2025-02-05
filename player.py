"""
Module: game_setup.py

Description:
	- Handles player setup(number of players, names),
	- Displays game rules,
	- (Optionally) manges a simple play flow calling level functions.
"""

from levels import beginner_level, intermediate_level, advanced_level
from timer import player_time_counter, add_score, print_scores


def setup_players():
	"""Sets up the game by initializing players.
	Returns: a list of player names.
	"""

	print("Welcome to the Wiki Word Chain Game!\n")

	# Input number of players
	while True:
		try:
			num_players = int(input("Enter the number of players: "))
			if not (1 <= num_players <= 5):
				raise ValueError("The number of players must be between 1 and 5.")
			break
		except ValueError as e:
			print(f"Invalid input: {e}")

	# Input player names
	players = []
	for i in range(num_players):
		while True:
			try:
				name = input(f"Enter the name of player no. {i + 1}: ")
				if not name.strip():  # Check for empty or whitespace-only names
					raise ValueError("The provided name is empty and cannot be added.")
				players.append(name)
				break
			except ValueError as e:
				print(f"Invalid input: {e}")

	print("\nPlayers successfully registered!")
	print(f"Players names: {players}")
	return players


def display_game_rules():
	"""Displays the rules of the game.
	Returns: Str: The rules text (also printed to console).
	"""
	rules = (
		"\n==============================\n"
		"           Game Rules:\n"
		"==============================\n"
		"1. The game begins with a randomly generated word.\n"
		"2. Form a continuous chain of words where each word starts with the last letter of the previous word.\n"
		"3. Words used must correspond to valid Wikipedia article titles.\n"
		"4. Levels of increasing difficulty: Beginner, Intermediate, Advanced.\n"
		"   - Beginner: Any Wikipedia article title.\n"
		"   - Intermediate: Forbidden Letters Challenge.\n"
		"   - Advanced: No repetition of starting letters within the word chain.\n"
		"5. Players must score at least 3 out of 5 to advance to the next level.\n"
		"6. Time limits: 10 seconds for Beginner and 15 seconds for Intermediate and Advanced.\n"
		"============================\n"
	)
	print(rules)
	return rules


def play_turn(player, level_name):
	"""
	Handles a single player's turn for a given level:
	  - Starts the timer for the given level_name (beginner, intermediate, advanced).
	  - Calls the appropriate level function (which runs 5 rounds internally).
	  - (Optional) Measures the player's time or simply enforces a blocking wait.
	  - Adds scoring logic.

	Args:
		player (str): The player's name.
		level_name (str): One of "beginner", "intermediate", or "advanced".
	"""
	# Print whose turn it is and for which level
	print(f"\n[{level_name.capitalize()} Level] It's {player}'s turn.")

	# 1. Start the timer
	#    If you're using the 'blocking wait' style, this just prints start time,
	#    loops for the given time (10 or 5 seconds), then prints "Time passed!".
	player_time_counter(level_name)

	# 2. Call the correct level function
	if level_name == 'beginner':
		beginner_level(player)
		# Example scoring: +2 for simply playing
		add_score(player, 2)
	elif level_name == 'intermediate':
		intermediate_level()
		# Example scoring: +2
		add_score(player, 2)
	elif level_name == 'advanced':
		advanced_level()
		# Example scoring: +3
		add_score(player, 3)
	else:
		print("Error: Unknown level specified.")


def main():
	"""Start the game setup and run the game."""
	players = setup_players()  # Store the returned list of players
	display_game_rules()
	print("\nLet's start the game!\n")
	input("Press enter to start the game...")
	play_turn(players, level_name)
	print("\nSetup complete - proceed to next step of the game workflow!")


# play_turn(players)


if __name__ == "__main__":
	main()






