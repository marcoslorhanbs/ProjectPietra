import sqlite3

conn = sqlite3.connect('Data/PiMemories.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Memories(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    phrase TEXT NOT NULL,
    keyword TEXT
);
""")

