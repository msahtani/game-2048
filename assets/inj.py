import numpy as np
import sqlite3

lis = [
    [1024, 512, 256, 128],
    [8 ,16 ,32 ,64],
    [4, 2, 2, 0],
    [0,0,0,0]
]

arr = np.array(lis)
np.save('tmp', arr)

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

with open('tmp.npy') as f:
    cursor.execute("INSERT INTO game2048(state, score, largest_tile) VALUES (?, ?, ?)",
    (f.read(), 0, 1024))
    conn.commit()
