from models.game import *
from models.review import Review

class User:
    all_users = []

    def __init__(self, gamertag):
        self.gamertag = gamertag  
        self.owned_games = []
        self.reviews = []
        User.all_users.append(self)

    @property
    def gamertag(self):
        return self._gamertag

    @gamertag.setter
    def gamertag(self, new_gamertag):
        if not isinstance(new_gamertag, str) or not 5 <= len(new_gamertag) <= 20:
            raise ValueError("Gamertag must be a string between 5 and 20 characters")
        if any(user.gamertag == new_gamertag for user in User.all_users):
            raise ValueError("Gamertag must be unique")
        self._gamertag = new_gamertag

    @classmethod
    def find_by_gamertag(cls, gamertag):
        for user in cls.all_users:
            if user.gamertag == gamertag:
                return user
        return None

    def own_game(self, game):
        if not isinstance(game, Game):
            raise ValueError("Game must be an instance of the Game class")
        if game in self.owned_games:
            raise ValueError("User already owns this game")
        self.owned_games.append(game)

    def remove_game(self, game):
        if not isinstance(game, Game):
            raise ValueError("Game must be an instance of the Game class")
        if game not in self.owned_games:
            raise ValueError("User does not own this game")
        self.owned_games.remove(game)

    def add_review(self, game, rating, comment=None):
        if not isinstance(game, Game):
            raise ValueError("Game must be an instance of the Game class")
        review = Review(self, game, rating, comment)
        self.reviews.append(review)

    def delete_review(self, review_id):
        review = Review.find_by_id(review_id)
        if review is None or review not in self.reviews:
            raise ValueError("Review not found for this user")
        self.reviews.remove(review)

    def list_reviews(self):
        for review in self.reviews:
            print(f"Game: {review.game.title}, Rating: {review.rating}, Comment: {review.comment}")

    def delete(self):
        User.all_users.remove(self)

    @classmethod
    def list_all(cls):
        for user in cls.all_users:
            print(user.gamertag)


users = [
    {
        'gamertag': 'JohnDoe',
        'owned_games': [1],  # IDs of owned games
    },
    {
        'gamertag': 'JaneSmith',
        'owned_games': [1],
    },
    {
        'gamertag': 'AlexM',
        'owned_games': [2],
    },
    {
        'gamertag': 'SarahJ',
        'owned_games': [2],
    },
    {
        'gamertag': 'DavidW',
        'owned_games': [3],
    },
    {
        'gamertag': 'EmilyR',
        'owned_games': [3],
    },
    {
        'gamertag': 'MikeH',
        'owned_games': [4],
    },
    {
        'gamertag': 'LisaK',
        'owned_games': [4],
    },
    {
        'gamertag': 'ChrisG',
        'owned_games': [5],
    },
    {
        'gamertag': 'JessicaL',
        'owned_games': [5],
    }
]


# Create Game instances for owned games of each user
for user_data in users:
    User(user_data['gamertag'])
    gamertag = user_data['gamertag']
    owned_game_ids = user_data['owned_games']

    for game_id in owned_game_ids:
        existing_game = next((game for game in Game.all_games if game.id == game_id), None)
        if existing_game:
            # If a Game instance with the same ID already exists, skip creating a new one.
            continue

        # Assuming we have a global list `games` defined with all game data.
        game_data = next((game for game in games if game['id'] == game_id), None)
        if game_data:
            Game(game_id, game_data['title'])
