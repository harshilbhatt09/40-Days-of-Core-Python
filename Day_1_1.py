import math

num = int(input("Enter the number: "))
if num % 5 == 0:
    print(math.sqrt(num))
else:
    print(num % 5)
