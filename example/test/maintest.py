import requests
import json

base_url = "http://localhost:12346"
headers = {'User-Agent':'testclient/1.0', 'Accept':'*/*', 'Content-Type':'application/json'}

def process():
    user_id = create_user()
    user = read_user(user_id)
    months_billed = bill(user_id)
    months_payed = pay(user_id)

    print(user_id)
    print(user)


def create_user():
    payload = {'username': 'Jorge', 'email':'SomePlace', 'password':'password'}
    r = requests.post(base_url + '/users', headers=headers, data=json.dumps(payload))
    value = r.json()
    return value['user_id']

    
def read_user(user_id):
    r = requests.get(base_url+ '/users/' + str(user_id), headers=headers)
    return r.json()

def bill(user_id):
    r = requests.post(base_url + '/users/' + str(user_id) + '/bill', headers=headers, data='{"months":2}')
    print(r.text)
    return r.text

def pay(user_id):
    r = requests.post(base_url + '/users/' + str(user_id) + '/payment', headers=headers, data='{"months":1}')
    print(r.text)
    return r.text
                     
    
if __name__ == "__main__" :
    process()
