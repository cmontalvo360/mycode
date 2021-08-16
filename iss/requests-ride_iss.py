#!/usr/bin/python3

import requests

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    groundctrl = requests.get(MAJORTOM)

    helmetson = groundctrl.json()

    print("\nConverted Python Data")
    print(helmetson)

    print("\n\nPeople in space: ", helmetson["number"])
    people = helmetson["people"]
    print(people)

if __name__ == "__main__":
    main()
