from business_logic import business_rules

def validate_user_creation(data):
    if (len(data['username']) == 0):
        return 'fail', 'Username cannot be empty'
    elif (len(data['email']) == 0):
        return 'fail', 'Email cannot be empty'

    elif (len(data['password']) == 0):
        return 'fail', 'Password cannot be empty'
    else:
        return business_rules.check_business_user_creation(data)
    

def validate_user_request(data):
    try:
        int(data)
    except:
        return 'fail', 'An invalid user id has been passed'

    return business_rules.check_business_user_request(data)

def validate_payment(user_id, data):
    try:
        months = int(data['months'])
    except:
        return 'fail', 'The number of months must be a number'

    if (months < 1):
        return 'fail', 'You need to pay at least one month'

    return business_rules.check_business_payment(user_id, months)

def validate_bill(user_id, data):
    try:
        months = int(data['months'])
    except:
        return 'fail', 'The number of months must be a number'

    if (months < 1):
        return 'fail', 'You need to bill at least one month'

    return business_rules.check_business_bill(user_id, months)
