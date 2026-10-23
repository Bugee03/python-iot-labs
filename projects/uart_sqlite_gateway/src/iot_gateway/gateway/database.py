import sqlite3
from datetime import datetime


class Database:

    def __init__(self,db_name = "sensor_data.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()


    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS measurements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            temperature REAL,
            current REAL,
            vibration REAL
        )
        """)
        self.conn.commit()


    def insert(self, data: dict):
        cursor = self.conn.cursor()
        cursor.execute("""
                INSERT INTO measurements (timestamp, temperature, current, vibration)
                VALUES (?, ?, ?, ?)
                """, (
            datetime.utcnow().isoformat(),
            data["temperature"],
            data["current"],
            data["vibration"]
        ))
        self.conn.commit()