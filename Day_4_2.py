words1 = ["Hate", "love", "hi"]
count = 0
list1 = []
for i in words1:
    count = len(i)
    list1.append(count)
list1.sort()
for j in list1:
    for k in list1:
        if j != k:
            print(list1[-1])
            break
print("0")

# words1 = ["Hate", "love", "1234", "hi"]
# b = []
