#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import BytesIO as StringIO
from pprint import pprint
from xml.etree import ElementTree
from urllib.request import urlopen

with urlopen('http://news.google.com/news?topic=h&output=rss') as g:
    f = StringIO(g.read())
    tree = ElementTree.parse(f)


def topnews(count=5):
    pair = [None, None]
    for elmt in tree.getiterator():
        if elmt.tag == 'title':
            skip = elmt.text.startswith('Top stories')
            if skip:
                continue
            pair[0] = elmt.text
        if elmt.tag == 'link':
            if skip:
                continue
            pair[1] = elmt.text
        if pair[0] and pair[1]:
            count -= 1
            yield (tuple(pair))
            if not count:
                return
            pair = [None, None]


for news in topnews():
    pprint(news)
