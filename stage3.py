import requests  
import json

data = {'token':'hHbm4niaPt'}
r = requests.post('http://challenge.code2040.org/api/prefix', data=json.dumps(data))
		
jsonData = r.json()
pre = jsonData['result']['prefix']
arr = jsonData['result']['array']

 
def prefix(pre,array):
    newarray = []
    for i in xrange(len(array)):
	if array[i][0:3] != pre:
            newarray.append(array[i])
    return newarray
result = prefix(pre,arr)



data3 = {'token': 'hHbm4niaPt', 'array': result}
r3 = requests.post('http://challenge.code2040.org/api/validateprefix', data=json.dumps(data3))
jsonData3 = r3.json()
print(jsonData3)

