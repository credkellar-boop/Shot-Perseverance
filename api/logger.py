import sqlite3
import os

class SessionLogger:
    def __init__(self, db_path="data/session_data.db"):
        # Create the data folder if it doesn't exist
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        self.conn = sqlite3.connect(db_path)
        self.curr = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Using TEXT for timestamp to avoid SQLite REAL conversion errors
        self.curr.execute('''CREATE TABLE IF NOT EXISTS events 
            (timestamp TEXT, action_type TEXT, score REAL, video_path TEXT)''')
        self.conn.commit()

    def log_event(self, action_type, score, path):
        self.curr.execute(
            "INSERT INTO events (timestamp, action_type, score, video_path) VALUES (datetime('now'), ?, ?, ?)", 
            (action_type, score, path)
        )
        self.conn.commit()
