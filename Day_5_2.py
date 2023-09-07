students = [
    "Male",
    "Female",
    "female",
    "male",
    "male",
    "male",
    "female",
    "male",
    "Female",
    "Male",
    "Female",
    "Male",
    "female",
]
malecount = 0
femalecount = 0
for i in students:
    if i.lower() == "male":
        malecount += 1
    elif i.lower() == "female":
        femalecount += 1
list1 = [("Male", malecount), ("Female", femalecount)]
print(list1)
