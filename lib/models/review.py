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

    @classmethod
    def list_all(cls):
        for review in cls.all_reviews:
            print(f"User: {review.user.gamertag}, Game: {review.game.title}, Rating: {review.rating}, Comment: {review.comment}")
