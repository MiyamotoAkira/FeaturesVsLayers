from data import models

class MemoryStore :
    def __init__ (self):
        self.users = {}

    def create(self, user):
        user_id = len(self.users)
        data_user = models.DataUser(user_id, user['username'], user['email'], user['password'])
        self.users[str(user_id)] = data_user
        return 'ok', data_user
    
    def read(self, user_id):
        if (user_id in self.users):
            return 'ok', self.users[user_id]
        else:
            return 'ok', None

    def months_to_pay(self, user_id):
        if (user_id in self.users):
            return 'ok', self.users[user_id].months
        else:
            return 'ok', None
        

    def read_by_email(self, email):
        for value in self.users.values():
            if (value.email == email):
                return 'ok', value

        return 'ok', None
            

    def bill_months(self, user_id, months):
        if (user_id in self.users):
            self.users[user_id].months += months
        return 'ok', months
            
    def pay_months(self, user_id, months):
        if (user_id in self.users):
            self.users[user_id].months = self.users[user_id].months - months
        return 'ok', months

            
store = MemoryStore()
