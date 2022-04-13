import os
from time import gmtime, strftime, sleep
from urllib import request
import json

SLEEP_SEC = 30
while True:
    sleep(SLEEP_SEC)
    with os.popen("ip addr") as f:
        ip_str = '<br>'.join(list(f))
        req = request.Request('http://example.com', method="POST")
        req.add_header('Content-Type', 'application/json')
        ip_str += "<br>" + strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
        data = {
            "ip": ip_str
        }
        data = json.dumps(data)
        r = request.urlopen(req, data=data.encode())
        print(r.read())
