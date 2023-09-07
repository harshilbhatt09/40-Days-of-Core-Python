list1 = ["1", "3", "5"]
sum = 0
list2 = [int(i) for i in list1]
for i in list1:
    sum += int(i)
print(list2)
print(f"Sum is : {sum}")
