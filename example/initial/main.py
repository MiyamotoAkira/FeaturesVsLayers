from flask import Flask
from flask import request
from flask import json
from flask import Response
import sys

app = Flask(__name__)


class DataUser:
    def __init__(self, user_id, username, email, password):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.months = 0


def encode_data_user(o):
    if (isinstance(o, DataUser)):
        o_dict = {'user_id':o.user_id, 'username':o.username, 'email':o.email}
        return o_dict


class MemoryStore :
    def __init__ (self):
        self.users = {}

    def create(self, user):
        user_id = len(self.users)
        data_user = DataUser(user_id, user['username'], user['email'], user['password'])
        self.users[str(user_id)] = data_user
        return data_user
    
    def read(self, user_id):
        if (user_id in self.users):
            return self.users[user_id]
        else:
            return None

    def bill_months(self, user_id, months):
        if (user_id in self.users):
            self.users[user_id].months += months

            
    def pay_months(self, user_id, months):
        if (user_id in self.users):
            self.users[user_id].months = self.users[user_id].months - months

        
data_store = MemoryStore()

@app.route("/users", methods=['POST'])
def create_user():
   user = request.get_json()
   created_user = data_store.create(user)
   json_user = json.dumps(created_user, default = encode_data_user)
   response = Response(response=json_user, content_type='application/json', status='201')
   return response


@app.route("/users/<user_id>", methods=['GET'])
def read_user(user_id):
    user_in_data = data_store.read(user_id)
    user = json.dumps(user_in_data, default = encode_data_user)
    response = Response(response=user, content_type='application/json', status='200')
    return response

@app.route("/users/<user_id>/payment", methods=['POST'])
def pay(user_id):
    months = int(request.get_json()['months'])
    data_store.pay_months(user_id, months)
    return Response(response=json.dumps(months), content_type='application/json', status='200')
    
@app.route("/users/<user_id>/bill", methods=['POST'])
def bill(user_id):
    json_data = request.get_json()
    months = int(json_data['months'])
    data_store.bill_months(user_id, months)
    return Response(response=json.dumps(months), content_type='application/json', status='200')


if __name__ == "__main__":
    app.run(port=12346)
