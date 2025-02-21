class Database:
    def __init__(self):
        # Using a dictionary to store users keyed by their id
        self.users = {}

    def new_user(self, id, name):
        return {
            "id": id,
            "name": name,
            "session": None,
        }

    async def add_user(self, id, name):
        # Add or update the user in memory
        self.users[id] = self.new_user(id, name)

    async def is_user_exist(self, id):
        # Check if the user exists in the dictionary
        return id in self.users

    async def total_users_count(self):
        # Return the total count of users stored in memory
        return len(self.users)

    async def get_all_users(self):
        # Return a list of all user dictionaries
        return list(self.users.values())

    async def delete_user(self, id):
        # Remove the user from the dictionary if they exist
        if id in self.users:
            del self.users[id]

    async def set_session(self, id, session):
        # Update the session field for the user
        if id in self.users:
            self.users[id]['session'] = session

    async def get_session(self, id):
        # Retrieve the session for the user if available
        user = self.users.get(id)
        return user.get("session") if user else None

# Instantiate the database object for in-memory use
db = Database()
