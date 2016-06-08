import requests
import time
import const

t1 = time.time()

for i in range(100):
    
    r = requests.get("http://%s:5000/off" % const.TARGET_IP)
    r = requests.get("http://%s:5000/status" % const.TARGET_IP)

t2 = time.time()
print("Czas requestu: %s ms" % (1000*(t2-t1)/100))

