list1 = [0, 1, 4, 6, 0, 5, 0, 7, 9]
list1.sort()
count = 0
for i in list1:
    if i == 0:
        list1.append(i)
        count += 1
        for j in range(count):
            del list1[j]
print(list1)
