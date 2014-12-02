import requests  
import json

data = {'token':'hHbm4niaPt'}
r = requests.post('http://challenge.code2040.org/api/getstring', data=json.dumps(data))
		
jsonData = r.json()


test_string = jsonData['result']

def reverse(string):
	output = ''
	for i in range(len(string)-1,-1,-1):
		output = output + string[i]
	return output
result = reverse(test_string)

data2 = {'token':'hHbm4niaPt', 'string': result}
r2= requests.post('http://challenge.code2040.org/api/validatestring', data=json.dumps(data2))
jsonData2 = r2.json()
print(jsonData2)
