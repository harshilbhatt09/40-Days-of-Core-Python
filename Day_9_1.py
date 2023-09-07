str_num = input("Enter number: ")
odd_list = [int(i) for i in str_num if int(i) % 2 != 0]
odd_list.sort()
print(odd_list[-1])
