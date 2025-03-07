import motor.motor_asyncio
from config import DB_NAME, DB_URI

class Database:
    
    def __init__(self, uri, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.db = self._client[database_name]
        self.col = self.db.users

    def new_user(self, id, name):
        return dict(
            id = id,
            name = name,
            session = None,
        )
    
    async def add_user(self, id, name):
        user = self.new_user(id, name)
        await self.col.insert_one(user)
    
    async def is_user_exist(self, id):
        user = await self.col.find_one({'id':int(id)})
        return bool(user)
    
    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count

    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        await self.col.delete_many({'id': int(user_id)})

    async def set_session(self, id, session):
        await self.col.update_one({'id': int(id)}, {'$set': {'session': session}})

    async def get_session(self, id):
        user = await self.col.find_one({'id': int(id)})
        return user.get('session')

db = Database(DB_URI, DB_NAME)

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

