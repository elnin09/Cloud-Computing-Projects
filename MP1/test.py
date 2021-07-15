import requests
import json

url = 'https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp1'

payload = {
		'ip_address1': "3.82.106.176:5000", 
		'ip_address2': "54.83.154.0:5000" ,
		'load_balancer' : "mp1-364195164.us-east-1.elb.amazonaws.com",
		'submitterEmail':  "swapnildarmora@gmail.com",
		'secret':  "dCLLVOWlxVnItfst"
		}

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)