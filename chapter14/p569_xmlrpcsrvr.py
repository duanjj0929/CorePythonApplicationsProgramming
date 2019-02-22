#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import operator
import time
from urllib.request import urlopen
from xmlrpc.server import SimpleXMLRPCServer

# TODO - 13练习后再处理这里
# import twapi  # twapi.py form the "Web Services" chapter

server = SimpleXMLRPCServer(('localhost', 8888))
server.register_introspection_functions()

FUNCs = ('add', 'sub', 'mul', 'truediv', 'floordiv', 'mod')
for f in FUNCs:
    server.register_function(getattr(operator, f))
server.register_function(pow)


class SpecialServices(object):
    def now_int(self):
        return time.time()

    def now_str(self):
        return time.ctime()

    def timestamp(self, s):
        return '[{}] {}'.format(time.ctime(), s)

    def stock(self, s):
        url = 'http://quote.yahoo.com/d/quotes.csv?s=%s&f=l1c1p2d1t1'
        u = urlopen(url % s)
        res = csv.reader(u).next()
        u.close()
        return res

    def forex(self, s='usd', t='eur'):
        url = 'http://quote.yahoo.com/d/quotes.csv?s=%s%s=X&f=nl1d1t1'
        u = urlopen(url % (s, t))
        res = csv.reader(u).next()
        u.close()
        return res

    def status(self):
        # t = twapi.Twitter('twython')
        # res = t.verify_credentials()
        # status = twapi.ResultsWrapper(res.status)
        # return status.text
        pass

    def twweet(self, s):
        # t = twapi.Twitter('twython')
        # res = t.update_status(s)
        # return res.created_at
        pass


server.register_instance(SpecialServices())

try:
    print('Welcome to PotpourriServ v0.1\n(Use ^C to exit)')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')
