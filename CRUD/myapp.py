import requests
import json

URL = "http://127.0.0.1:8000/crud/studentapi/"

def get_data(id=None):
    data1 = {}
    if id is not None:
        data1 = {'id': id}
    json_data = json.dumps(data1)
    r = requests.get( url=URL, data=json_data)
    data = r.json()
    print(data)
    # print(r)

get_data(2)
