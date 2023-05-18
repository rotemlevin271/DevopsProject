import requests

from FinalProject.db_connector import get_user
# Post request to add new user
res = requests.post('http://127.0.0.1:5000/users/2', json={"user_name":"kobi"})
if res.ok:
    print(res.json())
# just for testing I added the else
else:
    print('user already exists')

# Get request to check if user exists
res = requests.get('http://127.0.0.1:5000/users/2')
if res.ok:
    print(res.json())

# check posted data is stored in DB
user_name = get_user(1)
if user_name == 'john':
    print('john is under id number 1')
else:
    print('john was not stored under id 1')