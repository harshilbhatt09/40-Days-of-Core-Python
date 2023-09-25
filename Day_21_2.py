def even_or_average():
    nums = []
    for i in range(5):
        a = int(input("Enter number: "))
        nums.append(a)
    list2 = [i for i in nums if i % 2 == 0]
    list2.sort()
    if len(list2) != 0:
        return list2[-1]
    else:
        sum = 0
        for i in nums:
            sum = sum + i
        return sum / 5


print(even_or_average())
