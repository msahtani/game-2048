from game_logic import Game2048

class GameLoader:

    grid = None

    @classmethod
    def get_grid(cls):
        return cls.grid

    def load_game(cls):
       cls.grid = [Game2048()]