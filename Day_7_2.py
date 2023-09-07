names = [
    "Joseph",
    "Nathan",
    "Sasha",
    "Kelly",
    "Muhammad",
    "Jabulani",
    "Sera",
    "Patel",
    "Sera",
]
dict1 = {}
count = 0
for i in names:
    if i[0].lower() == "s":
        count += 1
        dict1[i] = count
print(dict1)
