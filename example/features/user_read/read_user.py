from models import models
from store import store


def validate_user_request(data):
    try:
        int(data)
    except:
        return 'fail', 'An invalid user id has been passed'

    return read(data)

def read(user_id):
    user= store.memory_store.get_user(user_id)
    
    if (user == None):
        return 'not_found', None
    else:
        return 'ok', user



