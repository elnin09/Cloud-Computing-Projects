import requests
import json
import uuid

url = "https://seorwrpmwh.execute-api.us-east-1.amazonaws.com/prod/mp2"

payload = {
	"graphApi": "https://plv4nvznma.execute-api.us-east-1.amazonaws.com/prod",
	"botName": "CityDistance",
	"botAlias": "distancelex",
	"identityPoolId": "us-east-1:0d4444f1-fb41-4e9e-a149-1d3b7022d0e0",
	"accountId": "548698799745",
	"submitterEmail": "swapnildarmora@gmail.com",
	"secret": "BtNsBsd4dF1Yt4AR",
	"region": "us-east-1"
    }

r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)