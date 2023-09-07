register = {"Michael": "yes", "John": "no", "Peter": "yes", "Mary": "yes"}
list1 = list(register.values())
count = 0
for i in list1:
    if i == "yes":
        count += 1
print(count)
