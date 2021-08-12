#!/usr/bin/env python3

with open("vlanconfig.cfg","r") as configfile:
    print(configfile.read())

    configlist = configfile.readlines()
    print(configlist)

    for x in configlist:
        print(x)
