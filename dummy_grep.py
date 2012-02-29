#!/usr/bin/env python
import string
import sys

text = sys.argv[1]
counter = 0

for line in sys.stdin.readlines():
    if string.count(line, text):
        print line
        counter += 1

print "znaleziono %d linii zawierajacych %s" % (counter, text)
