import requests  
import json
import dateutil.parser
import datetime
import iso8601

data = {'token':'hHbm4niaPt'}
r = requests.post('http://challenge.code2040.org/api/time', data=json.dumps(data))
		
jsonData = r.json()
date = jsonData['result']['datestamp']
inter = jsonData['result']['interval']


def datestamp(interval, thedate):
	
	interval = int(interval)

	date = iso8601.parse_date(thedate)
	interval = datetime.timedelta(0, interval)
	
	final = date + interval

	final = final.isoformat()
	
	format1 = final.split('+')[0]
	format1 += '.000Z'
	return format1 
result = datestamp(inter, date)

data3 = {'token': 'hHbm4niaPt', 'datestamp': result}
r3 = requests.post('http://challenge.code2040.org/api/validatetime', data=json.dumps(data3))
jsonData3 = r3.json()
print(jsonData3)
