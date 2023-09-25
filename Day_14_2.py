Teachers_name = input("Enter Teacher's name: ")
number_of_periods = int(input("Enter number of periods: "))


def your_salary(name, num, rate=20):
    if num >= 100:
        num2 = num - 100
        print(f"Teacher : {name}")
        print(f"Periods : {num}")
        print(f"Gross Salary : {(100 * rate) + (num2 * (rate + 5))}")
    else:
        print(f"Teacher : {name}")
        print(f"Periods : {num}")
        print(f"Gross Salary : {num * rate}")


your_salary(Teachers_name, number_of_periods)
