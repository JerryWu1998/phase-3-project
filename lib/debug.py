import ipdb

from db.games import games
from db.users import users
from db.reviews import reviews
from cli import *


if __name__ == "__main__":
    # Create Game instances
    game_instances = {game["id"]: Game(game["id"], game["title"]) for game in games}

    # Create User instances and assign games to users
    user_instances = {}
    for user in users:
        user_instance = User(user["gamertag"])
        user_instances[user["gamertag"]] = user_instance
        for game_id in user["owned_games"]:
            game_instance = game_instances.get(game_id)
            if game_instance:  # Ensure the game exists
                user_instance.own_game(game_instance)

    # Create Review instances
    review_instances = {}
    for review in reviews:
        user_instance = user_instances.get(review["user_gamertag"])
        game_instance = game_instances.get(review["game_id"])
        if user_instance and game_instance:  # Ensure the user and game exist
            review_instance = Review(user_instance, game_instance, review["rating"], review["comment"])
            game_instance.add_review(review_instance)
            review_instances[(review["user_gamertag"], review["game_id"])] = review_instance

    # Set a breakpoint here
    ipdb.set_trace()
