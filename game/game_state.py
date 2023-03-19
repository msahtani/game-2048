from .game_logic import Game2048

class GameState:

    grid = None

    @classmethod
    def get(cls):
        return cls.grid

    @classmethod
    def undo(cls):
        if len(cls.grid) > 1:
            cls.grid.pop()
        else:
            print("no more step to undo")

    @classmethod
    def load(cls, id=0, k=1):
        cls.grid = [
            tuple(
                [Game2048(id) for _ in range(k)]
            )
        ]

