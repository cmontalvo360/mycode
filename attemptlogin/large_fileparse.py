#!/usr/bin/env python3

loginfail = 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as keyfile:
    for line in keyfile:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
print("The number of failed log in attempts is", loginfail)
