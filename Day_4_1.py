def only_floats(a, b):
    if type(a) == type(20.0) and type(b) == type(20.0):
        print("2")
    elif type(a) == type(20.0):
        print("1")
    elif type(b) == type(20.0):
        print("1")
    else:
        print("0")


only_floats(12.1, 23)
