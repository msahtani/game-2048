from game_logic import Game2048

grid = None

def get_grid():
    global grid
    return grid

def load_game(id=0): #
    global grid
    if id == 0: # 
        grid = Game2048()

    return grid