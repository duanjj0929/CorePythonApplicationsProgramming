#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from distutils.log import warn as printf

DATA = (
    (9, 'Web Clients and Servers', 'base64, urllib'),
    (10, 'Web Programming: CGI & WSGI', 'cgi, time, wsgiref'),
    (13, 'Web Services', 'urllib, twython'),
)

BOOK_DATA_CSV = 'bookdata.csv'

printf('*** WRITING CSV DATA')
with open(BOOK_DATA_CSV, 'w', encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    for record in DATA:
        writer.writerow(record)

printf('*** REVIEW OF SAVED DATA')
with open(BOOK_DATA_CSV, 'r', encoding="utf-8", newline='') as f:
    reader = csv.reader(f)
    for chap, title, modpkgs in reader:
        printf('Chapter {}: {} (featuring {})'.format(chap, title, modpkgs))
