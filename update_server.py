import requests
import time
import common
import const

while True:
    cmd = requests.get("http://%s/get_command" % const.remote_server).text
    print "Got command %s" % cmd
    if cmd == "on":
        common.on()
    if cmd == "off":
        common.off()
    status = common.status()
    print "Sending status %s" % status
    requests.post("http://%s/update_status" % const.remote_server, data={"status": status})
    time.sleep(5)
