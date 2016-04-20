from models import models
from store import store


def validate_payment(user_id, data):
    try:
        months = int(data['months'])
    except:
        return 'fail', 'The number of months must be a number'

    if (months < 1):
        return 'fail', 'You need to pay at least one month'

    return check_business_payment(user_id, months)


def months_to_pay(user_id):
    user = store.memory_store.get_user(user_id)
    if (user == None):
        return 'not found', None
    else:
        return 'ok', user.months

    
def pay_months(user_id, months):
    user = store.memory_store.get_user(user_id)
    if (user_id == None):
        return 'not found', 'not such user'
    else:
        user.months = user.months - months
        return 'ok', months

    
def check_business_payment(user_id, months):
    _, months_in_arreas = months_to_pay(user_id)
    if (months_in_arreas < months):
        return 'fail', 'you cannot overpay'
    else:
        return pay_months(user_id, months)


