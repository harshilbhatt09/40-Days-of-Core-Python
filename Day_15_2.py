def your_age():
    names_age = {"jane": 23, "kerry": 45, "tim": 34, "peter": 27}
    name = input("What is your name? ").lower()

    if name in names_age:
        print(
            "Hi, {name}, you are {names_age} years old.".format(name, names_age[name])
        )
    else:
        age = int(input("How old are you? "))

        names_age[name] = age

        print("Hi, {name}, you are {names_age} years old.".format(name, age))


your_age()
