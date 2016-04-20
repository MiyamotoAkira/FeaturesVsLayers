from models import models
from store import store

def check_business_user_creation(data):
    _, user = read_by_email(data['email'])
    if (user == None):
        return  create(data)
    else:
        return 'fail', 'There is already an user with that email'

    
def read_by_email(email):
    users = store.memory_store.get_users()
    for value in users.values():
        if (value.email == email):
            return 'ok', value

    return 'ok', None


def create(user):
    users = store.memory_store.get_users()
    user_id = len(users)
    data_user = models.DataUser(user_id, user['username'], user['email'], user['password'])
    store.memory_store.create_user(str(user_id), data_user)
    return 'ok', data_user


def validate_user_creation(data):
    if (len(data['username']) == 0):
        return 'fail', 'Username cannot be empty'
    elif (len(data['email']) == 0):
        return 'fail', 'Email cannot be empty'

    elif (len(data['password']) == 0):
        return 'fail', 'Password cannot be empty'
    else:
        return check_business_user_creation(data)
