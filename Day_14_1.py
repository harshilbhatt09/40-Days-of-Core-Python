def flat_list(list1):
    list2 = [j for i in list1 for j in i]
    return list2


print(flat_list([[1, 2, 3, 4, 5, 6]]))
