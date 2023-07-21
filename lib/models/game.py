class Game:
    all_games = []

    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.reviews = []

        Game.all_games.append(self)

    def update_title(self, new_title):
        self.title = new_title

    def delete(self):
        Game.all_games.remove(self)

    @staticmethod
    def list_all():
        for game in games:
            print(f"ID: {game['id']}, Title: {game['title']}")


games = [{
        'id': 1,
        'title': 'Super Mario',
    },
    {
        'id': 2,
        'title': 'Minecraft',
    },
    {
        'id': 3,
        'title': 'The Legend of Zelda',
    },
    {
        'id': 4,
        'title': 'Grand Theft Auto V',
    },
    {
        'id': 5,
        'title': 'Fortnite',
    },
    {
        'id': 6,
        'title': 'Overwatch',
    },
    {
        'id': 7,
        'title': 'Call of Duty: Modern Warfare',
    },
    {
        'id': 8,
        'title': 'Assassin\'s Creed Valhalla',
    },
    {
        'id': 9,
        'title': 'FIFA 22',
    },
    {
        'id': 10,
        'title': 'The Witcher 3: Wild Hunt',
    },
    {
        'id': 11,
        'title': 'Among Us',
    },
    {
        'id': 12,
        'title': 'Animal Crossing: New Horizons',
    },
    {
        'id': 13,
        'title': 'Red Dead Redemption 2',
    },
    {
        'id': 14,
        'title': 'League of Legends',
    },
    {
        'id': 15,
        'title': 'Cyberpunk 2077',
    },
    {
        'id': 16,
        'title': 'World of Warcraft',
    },
    {
        'id': 17,
        'title': 'Rocket League',
    },
    {
        'id': 18,
        'title': 'Fortnite',
    },
    {
        'id': 19,
        'title': 'PlayerUnknown\'s Battlegrounds',
    },
    {
        'id': 20,
        'title': 'Mortal Kombat 11',
    }
]