from data import models
from data import access

def check_business_user_creation(data):
    _, user = access.store.read_by_email(data['email'])
    if (user == None):
        return  access.store.create(data)
    else:
        return 'fail', 'There is already an user with that email'
    

def check_business_user_request(data):
    return access.store.read(data)

def check_business_bill(user_id, months):
    return access.store.bill_months(user_id, months)

def check_business_payment(user_id, months):
    _, months_to_pay = access.store.months_to_pay(user_id)
    if (months_to_pay < months):
        return 'fail', 'you cannot overpay'
    else:
        return access.store.pay_months(user_id, months)
