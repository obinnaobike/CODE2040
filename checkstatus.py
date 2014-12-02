import requests  
import json

data = {'token':'hHbm4niaPt'}
r = requests.post('http://challenge.code2040.org/api/status', data=json.dumps(data))
jsonData = r.json()

print(jsonData) 

