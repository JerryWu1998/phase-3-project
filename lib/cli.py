```
import random

class User:
    def __init__(self, username):
        self.username = username
        self.owned_games = []

    def own_game(self, game):
        self.owned_games.append(game)

    def leave_review(self, game, score, comment=""):
        review = Review(game, self, score, comment)
        game.add_review(review)


class Game:
    def __init__(self, title):
        self.title = title
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)


class Review:
    def __init__(self, game, user, score, comment=""):
        self.game = game
        self.user = user
        self.score = score
        self.comment = comment


# Generate a list of users
users = [User("Alice"), User("Bob"), User("Charlie")]

# Popular game titles
game_titles = [
    "The Legend of Zelda: Breath of the Wild",
    "Super Mario Odyssey",
    "Red Dead Redemption 2",
    "The Witcher 3: Wild Hunt",
    "Final Fantasy VII Remake",
    "God of War",
    "Minecraft",
    "Fortnite",
    "Among Us",
    "Animal Crossing: New Horizons"
]

# Generate a list of games
games = [Game(title) for title in game_titles]

# Assign random games to users
for user in users:
    num_owned_games = random.randint(1, len(games))
    owned_games = random.sample(games, num_owned_games)
    for game in owned_games:
        user.own_game(game)

# Leave reviews for games
for user in users:
    for game in user.owned_games:
        score = random.randint(1, 10)
        comment = "Awesome game!"
        user.leave_review(game, score, comment)
```
