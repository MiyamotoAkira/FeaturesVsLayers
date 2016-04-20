from data import models

def encode_data_user(o):
    if (isinstance(o, models.DataUser)):
        o_dict = {'user_id':o.user_id, 'username':o.username, 'email':o.email}
        return o_dict
