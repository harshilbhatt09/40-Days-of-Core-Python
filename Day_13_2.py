import emoji


def Python_snakes(num):
    for i in range(1, num + 1):
        print(emoji.emojize(":snake:") * i)


Python_snakes(int(input("Enter number of rows: ")))
