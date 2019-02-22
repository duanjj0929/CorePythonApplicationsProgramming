#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from xmlrpc.client import ServerProxy

server = ServerProxy('http://localhost:8888')
print('Current time in seconds after epoch: {}'.format(server.now_int()))
print('Current time as a string: {}'.format(server.now_str()))
print('Area of circle of radius 5: {}'.format(
    server.mul(math.pi, server.pow(5, 2))))
# stock = server.stock('goog')
# print('Latest Google stock price: %s (%s / %s) as of %s at %s' % tuple(stock))
# forex = server.forex()
# print('Latest foreign exchange rate from %s: %s as of %s at %s' % tuple(forex))
# forex = server.forex('eur', 'usd')
# print('Latest foreign exchange rate from %s: %s as of %s at %s' % tuple(forex))
# print('Latest Twitter status:', server.status())

# add/sub/mul/truediv/floordiv/mod/pow
a = 5
b = 2
print('{} + {} = {}'.format(a, b, server.add(a, b)))
print('{} - {} = {}'.format(a, b, server.sub(a, b)))
print('{} * {} = {}'.format(a, b, server.mul(a, b)))
print('{} / {} = {}'.format(a, b, server.truediv(a, b)))
print('{} // {} = {}'.format(a, b, server.floordiv(a, b)))
print('{} % {} = {}'.format(a, b, server.mod(a, b)))
print('pow({}, {}) = {}'.format(a, b, server.pow(a, b)))

# timestamp
print('{}'.format(server.timestamp('abc')))
