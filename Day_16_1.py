def sum_list(nums):
    total = 0
    for num in nums:
        if isinstance(num, list):
            total += sum_list(num)
        else:
            total += num
    return total


print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))
