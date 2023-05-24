import os
import signal

from flask import Flask

from FinalProject.db_connector import get_user

app = Flask(__name__)


@app.route("/users/get_user_data/<user_id>")
def get_user_name(user_id):

    user_name = get_user(user_id)

    if user_name == 'error_no_such_id':
        return "<H1 id='error'>" + "no such user :" + user_id + "</H1>"
    else:
        return "<H1 id='user'>" + user_name + "</H1>", 200 # status code

@app.route('/stop_server')
def stop_server():
    try:
        os.kill(os.getpid(), signal.CTRL_C_EVENT)
        return f'Server stopped'
    except Exception as e:
        return f"Error stopping server: {str(e)}"


# host is pointing at local machine address
# debug is used for more detailed logs + hot swapping
# the desired port - feel free to change
app.run(host='127.0.0.1', debug=True, port=5001)


