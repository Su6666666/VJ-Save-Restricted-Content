import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def is_subscribed(user_id):
    cursor.execute("SELECT * FROM subscribers WHERE user_id = ?", (user_id,))
    return cursor.fetchone() is not None

def subscribe(user_id):
    cursor.execute("INSERT INTO subscribers (user_id) VALUES (?)", (user_id,))
    conn.commit()

def unsubscribe(user_id):
    cursor.execute("DELETE FROM subscribers WHERE user_id = ?", (user_id,))
    conn.commit()

def is_premium(user_id):
    cursor.execute("SELECT * FROM premium_members WHERE user_id = ?", (user_id,))
    return cursor.fetchone() is not None



import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS files (
        id INTEGER PRIMARY KEY,
        file_id TEXT,
        file_name TEXT,
        file_size INTEGER
    );
""")

conn.commit()
