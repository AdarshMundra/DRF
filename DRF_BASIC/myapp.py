import requests
import json
URL =" http://127.0.0.1:8000/api/stucreate/"
data ={
    "stuName":"new",
    "roll":104,
    "city":"demo"
}
json_data = json.dumps(data)
r = requests.post(url =URL ,data =json_data)
# data =r.json()
# print(data)
print(r)