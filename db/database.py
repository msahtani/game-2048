
import sqlite3
from datetime import datetime as dt
import numpy as np

from db.const import *

class DBConnection:

    def __init__(self):
        self.conn = None;
        try:
            self.conn = sqlite3.connect(DB_FILE)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(e)

    def exec(self, q, params = None):
        if params:
            self.cursor.execute(QUERY[q], params)
        else:
            self.cursor.execute(QUERY[q])

        
    def save(self, game):

        if game.id == 0:
            self.exec('save', (game.encoded, game.score, dt.now(), game.largest_tile))
        else:
            self.exec('update', (game.encoded, game.score, dt.now(), game.largest_tile, game.id))

        self.conn.commit()

    def load(self, id):
        assert id > 0

        self.exec('load', (id,))

        state, score = self.cursor.fetchone()

        with open('mat.npy', 'wb') as f:
            f.write(state)
        mat = np.load('mat.npy')
        import os
        os.remove('mat.npy')

        
        return mat, int(score), self.get_best_score()

    def get_last_id(self):
        self.exec('last_id')
        res, = self.cursor.fetchone()
        return int(res)

    def get_best_score(self):

        self.exec('best_score')
        try:
            best_score, = self.cursor.fetchone()
            return int(best_score)
        except:
            return 0

    def get_saved(self):
        self.exec('load_all')
        return self.cursor.fetchall()

    def delete(self, id):
        self.exec('delete', (id,))

    def close(self):
        self.cursor.close()
        self.conn.close()
    