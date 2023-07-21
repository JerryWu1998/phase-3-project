from models.user import User
from models.game import Game
from models.review import Review

def create_user(gamertag):
    User(gamertag)

def update_user(old_gamertag, new_gamertag):
    user = next(user for user in User.all_users if user.gamertag == old_gamertag)
    user.gamertag = new_gamertag

def delete_user(gamertag):
    user = next(user for user in User.all_users if user.gamertag == gamertag)
    user.delete()

def create_game(id, title):
    Game(id, title)

def update_game(id, new_title):
    game = next(game for game in Game.all_games if game.id == id)
    game.title = new_title

def delete_game(id):
    game = next(game for game in Game.all_games if game.id == id)
    game.delete()

def create_review(user_gamertag, game_id, rating, comment=None):
    user = next(user for user in User.all_users if user.gamertag == user_gamertag)
    game = next(game for game in Game.all_games if game.id == int(game_id))
    Review(user, game, int(rating), comment)

def update_review(user_gamertag, game_id, new_rating, new_comment):
    review = next(review for review in Review.all_reviews if review.user.gamertag == user_gamertag and review.game.id == int(game_id))
    review.update_rating(int(new_rating))
    review.update_comment(new_comment)

def delete_review(user_gamertag, game_id):
    review = next(review for review in Review.all_reviews if review.user.gamertag == user_gamertag and review.game.id == int(game_id))
    review.delete()

def list_all_users():
    for user in User.all_users:
        print(user.gamertag)

def list_all_games():
    Game.list_all()

def list_all_reviews():
    for review in Review.all_reviews:
        print(f"{review.user.gamertag} reviewed {review.game.title} - Rating: {review.rating}, Comment: {review.comment}")

COMMANDS = {
    'create_user': create_user,
    'update_user': update_user,
    'delete_user': delete_user,
    'list_all_users': list_all_users,
    'create_game': create_game,
    'update_game': update_game,
    'delete_game': delete_game,
    'list_all_games': list_all_games,
    'create_review': create_review,
    'update_review': update_review,
    'delete_review': delete_review,
    'list_all_reviews': list_all_reviews,
}

def run_cli():
    while True:
        print("\nPlease enter a command:")
        print("create_user - Create a new user")
        print("update_user - Update an existing user's gamertag")
        print("delete_user - Delete a user")
        print("list_all_users - View all users")
        print("create_game - Create a new game")
        print("update_game - Update an existing game's title")
        print("delete_game - Delete a game")
        print("list_all_games - View all games")
        print("create_review - Create a new review")
        print("update_review - Update an existing review's rating and comment")
        print("delete_review - Delete a review")
        print("list_all_reviews - View all reviews")
        print("quit - Quit the program")
        
        command = input("> ").strip().lower()

        if command == "quit":
            break

        try:
            if command in COMMANDS:
                if "list" in command:
                    COMMANDS[command]()
                else:
                    params = input("Please enter the parameters separated by comma: ")
                    params = [p.strip() for p in params.split(",")]
                    COMMANDS[command](*params)
            else:
                print(f"Invalid command: {command}")
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

if __name__ == "__main__":
    run_cli()
