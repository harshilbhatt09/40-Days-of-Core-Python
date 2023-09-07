list1 = [1, 2, 9, 3, 85, 62, 59]
even = [i for i in list1 if i % 2 == 0]
odd = [j for j in list1 if j % 2 != 0]
even.sort()
odd.sort()
print(even[-1] - odd[0])
