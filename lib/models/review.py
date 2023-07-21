
class Review:
    all_reviews = []
    id_counter = 1

    def __init__(self, user, game, rating, comment=None):
        if not isinstance(rating, int) or not 1 <= rating <= 10:
            raise ValueError("Rating must be an integer between 1 and 10")
        if comment and not isinstance(comment, str):
            raise ValueError("Comment must be a string")
        self.id = Review.id_counter
        Review.id_counter += 1
        self.user = user
        self.game = game
        self.rating = rating
        self.comment = comment
        Review.all_reviews.append(self)

    @classmethod
    def list_all(cls):
        for review in cls.all_reviews:
            print(f"User: {review.user.gamertag}, Game: {review.game.title}, Rating: {review.rating}, Comment: {review.comment}")
                
    @classmethod
    def find_by_id(cls, id):
        for review in cls.all_reviews:
            if review.id == id:
                return review
        return None

    def update_rating(self, new_rating):
        if not isinstance(new_rating, int) or not 1 <= new_rating <= 10:
            raise ValueError("Rating must be an integer between 1 and 10")
        self.rating = new_rating

    def update_comment(self, new_comment):
        if not isinstance(new_comment, str):
            raise ValueError("Comment must be a string")
        self.comment = new_comment

    def delete(self):
        Review.all_reviews.remove(self)

reviews = [
    {
        'user_gamertag': 'JohnDoe',
        'game_id': 1,
        'rating': 8,
        'comment': 'Great game!',
    },
    {
        'user_gamertag': 'JaneSmith',
        'game_id': 1,
        'rating': 9,
        'comment': 'Amazing game!',
    },
    {
        'user_gamertag': 'AlexM',
        'game_id': 2,
        'rating': 7,
        'comment': 'Fun but challenging',
    },
    {
        'user_gamertag': 'SarahJ',
        'game_id': 2,
        'rating': 10,
        'comment': 'Classic game!',
    },
    {
        'user_gamertag': 'DavidW',
        'game_id': 3,
        'rating': 6,
        'comment': 'Interesting storyline',
    },
    {
        'user_gamertag': 'EmilyR',
        'game_id': 3,
        'rating': 9,
        'comment': 'Great graphics!',
    },
    {
        'user_gamertag': 'MikeH',
        'game_id': 4,
        'rating': 8,
        'comment': 'Addictive gameplay',
    },
    {
        'user_gamertag': 'LisaK',
        'game_id': 4,
        'rating': 7,
        'comment': 'Needs more content updates',
    },
    {
        'user_gamertag': 'ChrisG',
        'game_id': 5,
        'rating': 9,
        'comment': 'Best multiplayer experience',
    },
    {
        'user_gamertag': 'JessicaL',
        'game_id': 5,
        'rating': 10,
        'comment': 'Hours of fun!',
    }
]

# Create instances of Review for each review data in the reviews list
for review_data in reviews:
    from models.user import User
    from models.game import Game
    user_gamertag = review_data['user_gamertag']
    game_id = review_data['game_id']
    rating = review_data['rating']
    comment = review_data['comment']
    user = User.find_by_gamertag(user_gamertag)
    game = Game.find_by_id(game_id)
    
    if user and game:
        review_instance = Review(user, game, rating, comment)
    else:
        print(f"User or game not found for review data: {review_data}")


# Review.list_all()