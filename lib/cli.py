<<<<<<< HEAD


################ GAME CLASS ################
class Game:
    all_games = []

    def __init__(self, id, title):
        if any(game.id == id for game in Game.all_games):
            raise ValueError("Game ID must be unique")
        self._id = id
        self.title = title  # use the property setter
        self.reviews = []
        Game.all_games.append(self)

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str) or not new_title.strip():
            raise ValueError("Title must be a non-empty string")
        self._title = new_title

    def add_review(self, review):
        if not isinstance(review, Review):
            raise ValueError("Review must be an instance of the Review class")
        if review in self.reviews:
            raise ValueError("Duplicate review for this game")
        self.reviews.append(review)

    def calculate_average_rating(self):
        if not self.reviews:
            return 0.0
        total_ratings = sum(review.rating for review in self.reviews)
        return round(total_ratings / len(self.reviews), 2)

################ REVIEW CLASS ################
class Review:
    all_reviews = []

    def __init__(self, user, game, rating, comment=None):
        if not isinstance(rating, int) or not 1 <= rating <= 10:
            raise ValueError("Rating must be an integer between 1 and 10")
        if comment and not isinstance(comment, str):
            raise ValueError("Comment must be a string")
        self.user = user
        self.game = game
        self.rating = rating
        self.comment = comment
        Review.all_reviews.append(self)

    def update_rating(self, new_rating):
        if not isinstance(new_rating, int) or not 1 <= new_rating <= 10:
            raise ValueError("Rating must be an integer between 1 and 10")
        self.rating = new_rating

    def update_comment(self, new_comment):
        if not isinstance(new_comment, str):
            raise ValueError("Comment must be a string")
        self.comment = new_comment

################ USER CLASS ################
class User:
    all_users = []

    def __init__(self, gamertag):
        self.gamertag = gamertag  # use the property setter
        self.owned_games = []
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

    def display_owned_games(self):
        print(f"Owned games for {self.gamertag}:")
        for game in self.owned_games:
            print(game.title)
