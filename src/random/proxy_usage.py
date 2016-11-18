import socket

import socks

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

# from tornado import ioloop, httpclient

from urllib.request import Request, urlopen

# req = Request('http://127.0.0.1:8000',
#               headers={
#                   'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0'
#               })
# print(urlopen(req).read())


from urllib.parse import urlparse
from threading import Thread
import sys
from queue import Queue
import http

concurrent = 1000
i = 0


def doWork():
    while True:
        url = q.get()
        status, url = getStatus(url)
        doSomethingWithResult(status, url)
        q.task_done()


def getStatus(ourl):
    try:
        url = urlparse(ourl)
        conn = http.client.HTTPConnection(url.netloc)
        conn.request("HEAD", url.path)
        res = conn.getresponse()
        return res.status, ourl
    except:
        return "error", ourl


def doSomethingWithResult(status, url):
    req = Request(url,
                  headers={
                      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:49.0) Gecko/20100101 Firefox/49.0'
                  })
    with urlopen(req) as response:
        response.read()
        print(url.split('?')[-1])
    pass

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()

try:
    for i in range(100):
        q.put('http://127.0.0.1:8000')
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
