import requests  
import json

data = {'token':'hHbm4niaPt'}
r = requests.post('http://challenge.code2040.org/api/haystack', data=json.dumps(data))
		
jsonData = r.json()

haystack = jsonData['result']['haystack']
needle = jsonData['result']['needle']



def myhaystack(needle,haystack):
    length = len(haystack) - 1
    for i in xrange(length):
        if haystack[i] == needle:
            return i
result = myhaystack(needle,haystack)

data3 = {'token': 'hHbm4niaPt', 'needle': result}
r3 = requests.post('http://challenge.code2040.org/api/validateneedle', data=json.dumps(data3))
jsonData3 = r3.json()
print(jsonData3)

