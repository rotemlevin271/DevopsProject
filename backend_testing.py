import requests

from FinalProject.db_connector import get_user
# Post request to add new user
res = requests.post('http://127.0.0.1:5000/users/1', json={"user_name":"john"})
if res.ok:
    print(res.json())

# Get request to check if user exists
res2 = requests.get('http://127.0.0.1:5000/data/1')
if res2.ok:
    print(res2.json())

# check posted data is stored in DB
# user_name = get_user(1)
# if user_name == 'john':
#     print('john is under id number 1')
# else:
#     print('john was not stored under id 1')