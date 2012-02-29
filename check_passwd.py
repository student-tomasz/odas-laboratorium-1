#!/usr/bin/env python
import posix
import string

uid = posix.getuid()
login = ''
passwd = open('passwd')

for line in passwd.readlines():
    rec = string.split(line, ':')
    if int(rec[2]) == uid:
        login = rec[0]
        break
if login:
    print "%d -> %s" % (uid, login)
else:
    print "%d -> noname" % uid
