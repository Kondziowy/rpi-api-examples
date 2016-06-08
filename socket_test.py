import socket
import time
import const

s = socket.socket(socket.AF_INET)
s.connect((const.TARGET_IP, 4501))
s.setsockopt( socket.IPPROTO_TCP, socket.TCP_NODELAY, 1 )
t1 = time.time()
for _ in range(100):
    s.send("off")
    s.send("sta")
t2 = time.time()
print("Czas wywolania: %s ms" % (1000*(t2-t1)))
s.close()
