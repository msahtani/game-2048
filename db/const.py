DB_FILE = 'assets/db.sqlite3'

QUERY = {
    'save' : "INSERT INTO game2048 ('state', 'score', 'saved_at', 'largest_tile') VALUES(?, ?, ?, ?)",
    'update' : "UPDATE game2048 SET state=?, score=?, saved_at=?, largest_tile=? WHERE id=?",
    'load' : "SELECT state, score FROM game2048 WHERE id=?",
    'last_id' : "SELECT id from game2048 ORDER BY id DESC",
    'best_score' : "SELECT score from game2048 ORDER BY score DESC",
    'load_all' : "SELECT id, score, largest_tile, saved_at FROM game2048 ORDER BY largest_tile DESC",
    'delete' : "DELETE FROM game2048 WHERE id = ?",
}