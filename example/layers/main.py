from flask import Flask
from flask import Response
from flask import request
from flask import json
from validation import validators
from utils import transformers

app = Flask(__name__)

@app.route("/users", methods=['POST'])
def create_user():
    print('hello')
    data = request.get_json()
    print(data)
    result, data = validators.validate_user_creation(data)
    if (result == 'ok'):
        return Response(response=json.dumps(data, default=transformers.encode_data_user), content_type='application/json', status='201')
    else:
        return Response(response=data, content_type='plain/text', status='400')

    
@app.route("/users/<user_id>", methods=['GET'])
def read_user(user_id):
    result, data = validators.validate_user_request(user_id)
    if (result == 'ok'):
        return Response(response=json.dumps(data, default=transformers.encode_data_user), content_type='application/json', status='200')
    else:
        return Response(response=data, content_type='plain/text', status='400')


@app.route("/users/<user_id>/payment", methods=['POST'])
def pay(user_id):
    data = request.get_json()
    result, data = validators.validate_payment(user_id, data)
    if (result == 'ok'):
        return Response(response=str(data), content_type='plain/text', status='200')
    else:
        return Response(response=data, content_type='plain/text', status='400')


@app.route("/users/<user_id>/bill", methods=['POST'])
def bill(user_id):
    data = request.get_json()
    result, data = validators.validate_bill(user_id, data)
    if (result == 'ok'):
        return Response(response=str(data), content_type='plain/text', status='200')
    else:
        return Response(response=data,content_type='plain/text', status='400')

if __name__ == "__main__":
    app.run(debug=True,port=12346)
