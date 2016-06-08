import requests
import json
import const

r = requests.get("http://%s:5000/status" % const.TARGET_IP)

d = json.loads(r.text)

print d["humidity"]
