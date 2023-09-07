def swap_values(list1):
    if type(list1) != list:
        print("Error")
    else:
        temp = []
        tempo = list1[0]
        list1[0] = list1[-1]
        list1[-1] = tempo
        print(list1)


swap_values([1, 6, 3, 9, 8, 5])
