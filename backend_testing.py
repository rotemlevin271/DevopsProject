import requests
from db_connector import get_user

print("stating the backend tesing...")

try:
    # Post request to add new user
    res = requests.post('http://127.0.0.1:5000/users/2', json={"user_name":"kobi"})
    if res.ok:
        print(res.json())
    # just for testing I added the else
    else:
        print('user already exists')

    # Get request to check if user exists
    res2 = requests.get('http://127.0.0.1:5000/users/2')
    if res2.ok:
        print(res2.json())

    # check posted data is stored in DB
    user_name = get_user(1)
    if user_name == 'john':
        print('john is under id number 1')
    else:
        print('john was not stored under id 1')
except Exception as e:
    print(f"Backend testing failed with the following error {e}") 
