def age_in_minutes(year):
    if type(year) != int:
        print("Error")
        year = int(input("Enter number: "))
        age_in_minutes(year)
    elif len(str(year)) != 4:
        print("Enter four digit number")
        year = int(input("Enter number: "))
        age_in_minutes(year)
    elif year < 1900 or year > 2023:
        print("Enter number between 1900 and 2023")
        year = int(input("Enter number: "))
        age_in_minutes(year)
    else:
        print("You are {:,} minutes old".format((2023 - year) * 12 * 30 * 24 * 60))


year = int(input("Enter born year: "))
age_in_minutes(year)
