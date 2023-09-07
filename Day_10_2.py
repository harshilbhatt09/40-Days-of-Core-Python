list1 = [1000000, 23562895, 32459775512, 95659661548]
list2 = ["{:,}" for i in list1]
result = [list2[i].format(list1[i]) for i in range(len(list1))]
print(result)
