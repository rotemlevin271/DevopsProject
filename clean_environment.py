import requests

requests.get('http://127.0.0.1:5000/stop_server')
# for the third part of the project we dont use the frontend
# requests.get('http://127.0.0.1:5001/stop_server')

try:
    response = requests.get('http://127.0.0.1:5000/stop_server')
    response.raise_for_status()
    print("Server at http://127.0.0.1:5000 stopped successfully.")
except requests.RequestException as e:
    print(f"Error stopping server at http://127.0.0.1:5000: {str(e)}")

# try:
#     response = requests.get('http://127.0.0.1:5001/stop_server')
#     response.raise_for_status()
#     print("Server at http://127.0.0.1:5001 stopped successfully.")
# except requests.RequestException as e:
#     print(f"Error stopping server at http://127.0.0.1:5001: {str(e)}")
