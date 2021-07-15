import requests
import json

url = 'https://ikm2evu584.execute-api.us-east-1.amazonaws.com/test/mp11-autograder'

payload = {
			"submitterEmail": "swapnildarmora@gmail.com", # <insert your coursera account email>,
			"secret": "ee0d9sArwukuEQCd", # <insert your secret token from coursera>,
			# "partId" : "G6U3L"
			"dbApi": "https://plv4nvznma.execute-api.us-east-1.amazonaws.com/prod"
		}
print(json.dumps(payload))
r = requests.post(url, data=json.dumps(payload))

print(r.status_code, r.reason)
print(r.text)