while True:
    try:
        print("Lets divide x by y!")
        x = int(input("Whats is the number value of x? "))
        y = int(input("Whats is the number value of y? "))
        print("The value of x/y: ", x/y)
    except ZeroDivisionError as zerr:
        print("Handling run-time error:", zerr)

    except Exception as err:
        print("We did not anticipate that:", err)
