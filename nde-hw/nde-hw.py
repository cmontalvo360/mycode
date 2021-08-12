#!/usr/bin/env python3

items = input("What items do you have in your garage?")

garage_items = items.split()

for item in garage_items:
    print(f"{item} was found at the dog park")

