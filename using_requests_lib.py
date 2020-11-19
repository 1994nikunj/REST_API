import json

import requests

REST_GET_URL_1 = 'https://reqres.in/api/users/1'
REST_GET_URL_2 = 'https://postman-echo.com/get?foo1=bar1&foo2=bar2'
response = requests.get(url=REST_GET_URL_2)
status = response.status_code

print('Status Code:', status)
if status == 200:
    json_response = json.dumps(response.json(), indent=4)
    print(json_response)
