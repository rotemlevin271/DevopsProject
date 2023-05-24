import os
import signal
from flask import Flask, request, jsonify
import db_connector


app = Flask(__name__)


# supported methods
@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        user_name = db_connector.get_user(user_id)
        if user_name != 'error_no_such_id':
            return jsonify({'status': 'ok', 'user name': user_name}), 200
        else:
            return jsonify({'status': 'error', 'reason': 'no such id'}), 500
    #

    elif request.method == 'POST':

        # getting the json data payload from request
        request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        user_name = request_data.get('user_name')
        # connecting to the db and creating the user
        result = db_connector.add_user(user_name, user_id)
        if result != 1:
            return jsonify({'status': 'ok', 'user added': user_name}), 200
            print("ok")
        else:
            return jsonify({'status': 'error', 'reason': 'user with this id already exists '}), 500
            print("not ok")


    elif request.method == 'PUT':

        request_data = request.json
        user_name = request_data.get('user_name')

        result = db_connector.update_user(user_name, user_id)
        if result != 1:
            return jsonify({'status': 'ok', 'user updated': user_name}), 200
        else:
            return jsonify({'status': 'error', 'reason': 'no such id'}), 500
    #

    elif request.method == 'DELETE':

        result = db_connector.del_user(user_id)
        if result != 1:
            return jsonify({'status': 'ok', 'user deleted': user_id}), 200
        else:
            return jsonify({'status': 'error', 'reason': 'no such id'}), 500

@app.route('/stop_server')
def stop_server():
    try:
        os.kill(os.getpid(), signal.CTRL_C_EVENT)
        return f'Server stopped'
    except Exception as e:
        return f"Error stopping server: {str(e)}"


app.run(host='127.0.0.1', debug=True, port=5000)

