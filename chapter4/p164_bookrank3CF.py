#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor
from re import compile
from time import ctime
from urllib.request import urlopen as uopen

REGEX = compile(b"#([\d,]+) in Books ")
AMZN = "http://amazon.com/dp/"
ISBNs = {
    '0132269937': "Core Python Programming",
    '0132356139': "Python Web Development with Django",
    '0137143419': "Python Fundamentals"
}


def get_ranking(isbn):
    with uopen("{0}{1}".format(AMZN, isbn)) as page:
        return str(REGEX.findall(page.read())[0], 'utf-8')


def _main():
    print("At", ctime(), "on Amazon...")
    with ThreadPoolExecutor(3) as executor:
        for isbn, ranking in zip(ISBNs, executor.map(get_ranking, ISBNs)):
            print("- '{}' ranked {}".format(ISBNs[isbn], ranking))
    print("all DONE at:", ctime())


if __name__ == "__main__":
    _main()
