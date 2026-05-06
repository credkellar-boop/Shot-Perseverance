import sqlite3

class SessionLogger:
    def __init__(self, db_path="data/session_data.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS events 
            (timestamp REAL, action_type TEXT, perfection_score REAL, video_path TEXT)''')
        self.conn.commit()

    def log_event(self, action_type, score, path):
        self.cursor.execute("INSERT INTO events VALUES (datetime('now'), ?, ?, ?)", 
                           (action_type, score, path))
        self.conn.commit()
