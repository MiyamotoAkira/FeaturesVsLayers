from models import models
from store import store

def bill_months(user_id, months):
    user = store.memory_store.get_user(user_id)
    if (user == None):
        return 'not found', 'user has not been found'
    else:
        user.months += months
        return 'ok', months


def validate_bill(user_id, data):
    try:
        months = int(data['months'])
    except:
        return 'fail', 'The number of months must be a number'

    if (months < 1):
        return 'fail', 'You need to bill at least one month'

    return bill_months(user_id, months)
