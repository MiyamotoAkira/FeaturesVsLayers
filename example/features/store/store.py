from models import models

class MemoryStore :
    def __init__ (self):
        self.users = {}

    def get_users(self):
        return self.users

    def get_user(self, user_id):
        return self.users[user_id]

    def create_user(self, user_id, user):
        self.users[user_id] = user

            
memory_store = MemoryStore()
