from datetime import datetime
import time
import sys

# Keeps a map between players names and their score
players_score = {}


def player_time_counter(player_type='beginner'):
    """
    :param player_type: type of player: beginner, intermediate, advanced
    :return: a message when reach the time counter
    It waits for 5 seconds for advanced players and 10 seconds for others then if it passes the time returns a message
    """
    begin_time = datetime.now()
    print(f"Timer started at {begin_time.strftime('%H:%M:%S')} for a {player_type} player.")

    if player_type == 'advanced':
        delta = 5
    else:
        delta = 10

    # Return both the actual start_time and the time limit
    return begin_time, delta

    # player_time = 0
    # while player_time < delta:
    #     current_time = datetime.now()
    #     time_difference = current_time - begin_time
    #     player_time = time_difference.total_seconds()
    # print("Time passed!")


def initiate_players_scores(players):
    """
    :param players: a list of players name
    The function initializes the global 'players_score' dict with each player's name set to 0.
    """
    for player in players:
        players_score[player] = 0



def add_score(player, score=1):
    """
    :param player: player name
    :param score: optional> gained score, default is 1
    :raise Exception when player is not in the above dict
    Whenever player scores, we should call this fuction
    """
    if player not in players_score:
        raise Exception("Player not found")
    players_score[player] += score
    print('scoring----> ', players_score)


def print_scores():
    """
    :return: prints every player's score and finally prints the winner
    """
    winners = []
    max_score = 0
    print("Players Scoreboard:")
    for key, value in players_score.items():
        print(f"{key} scored: {value} points")
        if value > max_score:
            winners.clear()
            winners.append(key)
            max_score = value
        elif value == max_score:
            winners.append(key)
    print()
    if len(winners) > 1:
        print("The winners are:")
        for winner in winners:
            print(f"{winner}")
    else:
        print(f"The winner is:\n{winners[0]}")


def main():
    print("Not supported!")
    print("Testing timer.py ...")

    # Example usage
    sample_players = ["Alice", "Bob"]
    initiate_players_scores(sample_players)

    # Test the timer for advanced
    player_time_counter(player_type='advanced')

    # Test scoring
    add_score("Alice", 2)
    add_score("Bob", 3)
    print_scores()

    print("timer.py test complete!")


if __name__ == "__main__":
    main()

